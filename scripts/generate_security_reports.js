const path = require('path');
const fs = require('fs');

// Dynamically resolve exceljs
const frameworkModulesPath = 'C:\\Projects\\smartTravelPlanner\\smartTravelPlanner\\selenium-framework\\node_modules';
const ExcelJS = require(path.join(frameworkModulesPath, 'exceljs'));

// Comprehensive Datasets
const findingsData = [
  {
    id: 'SEC-001',
    severity: 'Critical',
    type: 'Authentication Bypass via Hardcoded Backdoor Credentials',
    cwe: 'CWE-798 / CWE-287',
    owasp: 'API2:2023 Broken Authentication',
    file: 'backend/src/controllers/authController.js (Lines 188-193, 227-233)',
    endpoint: 'POST /api/auth/login',
    desc: 'The login controller includes hardcoded password bypasses where supplying passwords like "123456", "anypassword", "SecretPassword123!", or "SuperSecret123!" evaluates as valid credentials for ANY registered user email.',
    scenario: 'An attacker targets the admin or any user email (e.g. john@example.com, admin@smarttravel.com). By entering the target email and the hardcoded password "123456" or "anypassword", the bcrypt verification is bypassed and a valid JWT bearer token with full user identity is returned.',
    impact: 'Complete account takeover of any user in the system without knowing their actual password.',
    fix: 'Remove all hardcoded password bypass checks immediately. Enforce strict bcrypt.compare(password, user.password) for all authentication requests.',
    status: 'Open'
  },
  {
    id: 'SEC-002',
    severity: 'Critical',
    type: 'Insecure Direct Object Reference (IDOR) - Deletion of Any User Records',
    cwe: 'CWE-639 / CWE-284',
    owasp: 'API1:2023 Broken Object Level Authorization',
    file: 'backend/src/controllers/tripController.js (Lines 342-368)',
    endpoint: 'DELETE /api/trips/:id',
    desc: 'The deleteTrip controller looks up the trip by ID and executes Trip.findByIdAndDelete(tripId) along with cascading deletion of bookings and expenses without checking if the trip belongs to req.user.id.',
    scenario: 'Attacker logs in with their own account, enumerates or intercepts another user\'s tripId, and sends DELETE /api/trips/<target_tripId>. The trip and all associated bookings and expenses are permanently deleted.',
    impact: 'Unauthorized permanent data loss, service disruption, and violation of multi-tenant isolation.',
    fix: 'Enforce ownership verification: const trip = await Trip.findOne({ _id: tripId, userId: req.user.id }); if (!trip) return res.status(404).json({ message: "Trip not found or unauthorized" });',
    status: 'Open'
  },
  {
    id: 'SEC-003',
    severity: 'Critical',
    type: 'Insecure Direct Object Reference (IDOR) - Information Disclosure of Any User Trips',
    cwe: 'CWE-639 / CWE-200',
    owasp: 'API1:2023 Broken Object Level Authorization',
    file: 'backend/src/controllers/tripController.js (Lines 324-338)',
    endpoint: 'GET /api/trips/:id',
    desc: 'The getTripById endpoint retrieves any trip by its MongoDB ObjectId or mock ID without validating that the authenticated requester owns the trip.',
    scenario: 'Attacker iterates through trip IDs or obtains another user\'s tripId from a shared link or prediction. Calling GET /api/trips/<id> returns destination, dates, budget, hotel name, and complete daily itinerary.',
    impact: 'Mass exposure of personally identifiable travel itineraries, dates, locations, and personal travel plans.',
    fix: 'Filter queries strictly by authenticated user ID: Trip.findOne({ _id: tripId, userId: req.user.id }).',
    status: 'Open'
  },
  {
    id: 'SEC-004',
    severity: 'High',
    type: 'Insecure Direct Object Reference (IDOR) - Unauthorized Modification of Trip Status',
    cwe: 'CWE-639 / CWE-284',
    owasp: 'API1:2023 Broken Object Level Authorization',
    file: 'backend/src/controllers/tripController.js (Lines 371-395)',
    endpoint: 'PUT /api/trips/:id/status',
    desc: 'Allows modifying the status of any trip (e.g. marking as "completed" or "upcoming") without checking that the authenticated user owns the trip.',
    scenario: 'Attacker sends PUT /api/trips/<victim_tripId>/status with {"status": "completed"}, mutating state of victim\'s active trips.',
    impact: 'Unauthorized state tampering across tenant boundaries.',
    fix: 'Enforce ownership check: Trip.findOneAndUpdate({ _id: tripId, userId: req.user.id }, { status }, { new: true }).',
    status: 'Open'
  },
  {
    id: 'SEC-005',
    severity: 'High',
    type: 'Insecure Direct Object Reference (IDOR) - Unauthorized Access to Bookings',
    cwe: 'CWE-639 / CWE-200',
    owasp: 'API1:2023 Broken Object Level Authorization',
    file: 'backend/src/controllers/bookingController.js (Lines 118-132)',
    endpoint: 'GET /api/bookings/trip/:tripId',
    desc: 'The getBookingsByTrip handler queries Booking.find({ tripId }) without validating that tripId belongs to req.user.id.',
    scenario: 'Attacker queries GET /api/bookings/trip/<victim_tripId> and retrieves full booking reference numbers, passenger details, costs, and confirmation status.',
    impact: 'Exposure of confidential reservation codes (PNR), hotel booking details, and payment amounts.',
    fix: 'Validate trip ownership prior to fetching bookings: const trip = await Trip.findOne({ _id: tripId, userId: req.user.id }); if (!trip) return res.status(403).json(...);',
    status: 'Open'
  },
  {
    id: 'SEC-006',
    severity: 'High',
    type: 'Insecure Direct Object Reference (IDOR) - Manipulation & Reading of Expenses',
    cwe: 'CWE-639 / CWE-284',
    owasp: 'API1:2023 Broken Object Level Authorization',
    file: 'backend/src/controllers/expenseController.js (Lines 10-90)',
    endpoint: 'POST /api/expenses, GET /api/expenses/trip/:tripId',
    desc: 'Endpoints for adding expenses and viewing expense statistics do not check if tripId belongs to req.user.id.',
    scenario: 'Attacker can post arbitrary expenses to another user\'s trip budget or read an itemized financial log and analytics for another user\'s vacation.',
    impact: 'Unauthorized modification of financial budget logs and exposure of private spending records.',
    fix: 'Verify tripId ownership before creating or fetching expenses.',
    status: 'Open'
  },
  {
    id: 'SEC-007',
    severity: 'High',
    type: 'Weak Default Fallback JWT Secret in Production Code',
    cwe: 'CWE-798 / CWE-326',
    owasp: 'API2:2023 Broken Authentication',
    file: 'backend/src/middleware/auth.js (Line 2) & authController.js (Line 7)',
    endpoint: 'All Authenticated Endpoints',
    desc: 'const JWT_SECRET = process.env.JWT_SECRET || "secret12345"; If the environment variable is missing or misconfigured, the server silently falls back to a trivial, guessable secret.',
    scenario: 'An attacker offline forges a JWT token with { "id": "admin_user_id" } signed with the known secret "secret12345" and accesses any protected API.',
    impact: 'Trivial authentication bypass and arbitrary user impersonation.',
    fix: 'Enforce that JWT_SECRET is explicitly required on startup. If process.env.JWT_SECRET is absent or under 32 characters, refuse to start the server.',
    status: 'Open'
  },
  {
    id: 'SEC-008',
    severity: 'High',
    type: 'Plaintext Cloud Database & API Secrets in Local Config / Version Control',
    cwe: 'CWE-312 / CWE-522',
    owasp: 'API8:2023 Security Misconfiguration',
    file: 'backend/.env & backend/src/config/mockDb.js',
    endpoint: 'Server Configuration & Database',
    desc: 'The backend/.env file contains a live MongoDB Atlas connection URI with embedded administrative credentials (mongodb+srv://...:lZ9O0YgiZvNMBceA@...) and Razorpay test API keys.',
    scenario: 'Any developer or process with read access to the repo can connect directly to the production MongoDB Atlas cluster, bypassing all API controls and dumping the entire database.',
    impact: 'Total compromise of the cloud database infrastructure and payment integration keys.',
    fix: 'Rotate database credentials immediately in MongoDB Atlas. Use environment variables injected via secret management systems (GitHub Secrets, AWS Secrets Manager).',
    status: 'Open'
  },
  {
    id: 'SEC-009',
    severity: 'Medium',
    type: 'NoSQL Regular Expression Injection & ReDoS',
    cwe: 'CWE-943 / CWE-1333',
    owasp: 'API8:2023 Security Misconfiguration',
    file: 'backend/src/controllers/destinationController.js (Line 13)',
    endpoint: 'GET /api/destinations?search=',
    desc: 'The search query parameter is passed unescaped directly into a MongoDB regex query: { name: { $regex: search, $options: "i" } }.',
    scenario: 'Attacker supplies ReDoS patterns like ?search=((a+)+)+$ or regex wildcard operators to cause catastrophic CPU spikes and denial of service.',
    impact: 'Server denial of service (ReDoS) and potential pattern-based data extraction.',
    fix: 'Escape special regex characters using lodash.escapeRegExp or search.replace(/[.*+?^${}()|[\\]\\\\]/g, "\\\\$&").',
    status: 'Open'
  },
  {
    id: 'SEC-010',
    severity: 'Medium',
    type: 'Missing Rate Limiting on Authentication Endpoints',
    cwe: 'CWE-307 / CWE-770',
    owasp: 'API4:2023 Unrestricted Resource Consumption',
    file: 'backend/src/index.js & routes/authRoutes.js',
    endpoint: 'POST /api/auth/login, POST /api/auth/signup',
    desc: 'There is no rate limiting or brute-force protection middleware (such as express-rate-limit) installed or configured on login or registration.',
    scenario: 'An attacker uses an automated tool (e.g. Hydra, Burp Intruder) to send 10,000 login requests per minute to crack passwords or flood the database with bogus user registrations.',
    impact: 'Account compromise through password guessing, CPU starvation from bcrypt hashing, and resource exhaustion.',
    fix: 'Implement express-rate-limit with a maximum of 5 to 10 login attempts per 15 minutes per IP address.',
    status: 'Open'
  },
  {
    id: 'SEC-011',
    severity: 'Medium',
    type: 'Excessive Data Exposure & Automatic Fallback Profile Leakage',
    cwe: 'CWE-200 / CWE-213',
    owasp: 'API3:2023 Broken Object Property Level Authorization',
    file: 'backend/src/controllers/authController.js (Lines 282-295)',
    endpoint: 'GET /api/auth/user',
    desc: 'In getUser, if the requested user ID is not found, the code automatically falls back to finding and returning John Doe\'s user record (john@example.com) or mockUsers[0].',
    scenario: 'When an unassociated or deleted user requests /api/auth/user, the API inadvertently returns another user\'s personal record, avatar, and phone number.',
    impact: 'Unintended information disclosure and privacy violation.',
    fix: 'Return a clean 404 Not Found immediately if req.user.id does not match an existing record.',
    status: 'Open'
  },
  {
    id: 'SEC-012',
    severity: 'Low',
    type: 'Missing Security HTTP Headers & Wildcard CORS Policy',
    cwe: 'CWE-942 / CWE-1021',
    owasp: 'API8:2023 Security Misconfiguration',
    file: 'backend/src/index.js (Lines 23-24)',
    endpoint: 'Global Express Middleware',
    desc: 'app.use(cors()) permits cross-origin requests from all domains (*). Standard defensive HTTP headers (Helmet: HSTS, X-Content-Type-Options, CSP) are not configured.',
    scenario: 'Third-party malicious websites can perform cross-origin AJAX requests or embed the application in malicious iframes (clickjacking).',
    impact: 'Increased susceptibility to clickjacking, MIME sniffing, and untrusted cross-origin communications.',
    fix: 'Add helmet() middleware and restrict CORS origin to trusted frontend domains.',
    status: 'Open'
  },
  {
    id: 'SEC-013',
    severity: 'Low',
    type: 'Verbose Internal Logging to Console & Unhandled Rejections',
    cwe: 'CWE-209 / CWE-778',
    owasp: 'API8:2023 Security Misconfiguration',
    file: 'backend/src/index.js (Lines 43-44) & Controllers',
    endpoint: 'Global Server Logging',
    desc: 'Database connection strings and raw error objects are logged directly to process.stdout using console.log and console.error without redaction.',
    scenario: 'Log files or centralized log aggregators capture internal server stack traces and credentials.',
    impact: 'Information disclosure to operators or centralized logging services.',
    fix: 'Implement a structured logging framework (e.g. Winston) with automated secret masking and sanitize production error responses.',
    status: 'Open'
  }
];

const endpointData = [
  { id: 'EP-001', url: '/', method: 'GET', auth: 'No', mech: 'None', role: 'Public', file: 'backend/src/index.js', fn: 'Root Health Check', risk: 'Low: Missing Security Headers' },
  { id: 'EP-002', url: '/api/auth/signup', method: 'POST', auth: 'No', mech: 'None', role: 'Public', file: 'backend/src/controllers/authController.js', fn: 'signup', risk: 'Medium: Missing Rate Limiting, Missing Password Policy' },
  { id: 'EP-003', url: '/api/auth/login', method: 'POST', auth: 'No', mech: 'None', role: 'Public', file: 'backend/src/controllers/authController.js', fn: 'login', risk: 'CRITICAL: Hardcoded Backdoor Passwords, Missing Rate Limiting' },
  { id: 'EP-004', url: '/api/auth/user', method: 'GET', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/authController.js', fn: 'getUser', risk: 'Medium: Profile Leakage Fallback' },
  { id: 'EP-005', url: '/api/auth/user', method: 'PUT', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/authController.js', fn: 'updateUser', risk: 'Medium: Unrestricted Avatar URL Input (SSRF risk)' },
  { id: 'EP-006', url: '/api/trips', method: 'POST', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/tripController.js', fn: 'createTrip', risk: 'Low: Missing Negative Budget & Date Boundary Validation' },
  { id: 'EP-007', url: '/api/trips', method: 'GET', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/tripController.js', fn: 'getTrips', risk: 'Low: Properly scoped to req.user.id' },
  { id: 'EP-008', url: '/api/trips/:id', method: 'GET', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/tripController.js', fn: 'getTripById', risk: 'CRITICAL: IDOR - Any user can view any trip by ID' },
  { id: 'EP-009', url: '/api/trips/:id', method: 'DELETE', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/tripController.js', fn: 'deleteTrip', risk: 'CRITICAL: IDOR - Any user can delete any other trip' },
  { id: 'EP-010', url: '/api/trips/:id/status', method: 'PUT', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/tripController.js', fn: 'updateTripStatus', risk: 'HIGH: IDOR - Any user can alter trip status' },
  { id: 'EP-011', url: '/api/bookings', method: 'POST', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/bookingController.js', fn: 'createBooking', risk: 'HIGH: IDOR - Can link bookings to other users trips' },
  { id: 'EP-012', url: '/api/bookings', method: 'GET', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/bookingController.js', fn: 'getUserBookings', risk: 'Low: Scoped to req.user.id' },
  { id: 'EP-013', url: '/api/bookings/trip/:tripId', method: 'GET', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/bookingController.js', fn: 'getBookingsByTrip', risk: 'HIGH: IDOR - Unrestricted trip reservation access' },
  { id: 'EP-014', url: '/api/expenses', method: 'POST', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/expenseController.js', fn: 'addExpense', risk: 'HIGH: IDOR - Post expenses to any trip' },
  { id: 'EP-015', url: '/api/expenses/trip/:tripId', method: 'GET', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/expenseController.js', fn: 'getExpensesByTrip', risk: 'HIGH: IDOR - View all expenses of another user trip' },
  { id: 'EP-016', url: '/api/expenses/trip/:tripId/stats', method: 'GET', auth: 'Yes', mech: 'JWT Bearer', role: 'Authenticated User', file: 'backend/src/controllers/expenseController.js', fn: 'getExpenseStats', risk: 'HIGH: IDOR - Financial statistics leak' },
  { id: 'EP-017', url: '/api/destinations', method: 'GET', auth: 'No', mech: 'None', role: 'Public', file: 'backend/src/controllers/destinationController.js', fn: 'getDestinations', risk: 'MEDIUM: NoSQL Regex Injection & ReDoS via search query' }
];

const dependencyData = [
  {
    cve: 'CVE-2024-52798 / GHSA-jqcg-44mw-7w3h',
    pkg: 'proxy-addr',
    severity: 'Critical',
    cvss: 9.1,
    installed: '2.0.7',
    fixedIn: '>= 2.0.8',
    cwe: 'CWE-290, CWE-348, CWE-697',
    desc: 'proxy-addr is vulnerable to IP address spoofing via IPv4-mapped IPv6 addresses within a trusted subnet. Attackers can forge client IP headers to bypass IP-based access controls.',
    remediation: 'Update Express dependencies or run npm update proxy-addr to pull version 2.0.8 or later.'
  },
  {
    cve: 'GHSA-27r3-jxmh-p828',
    pkg: 'body-parser',
    severity: 'High',
    cvss: 7.5,
    installed: '2.0.0 - 2.3.0',
    fixedIn: '>= 2.4.0',
    cwe: 'CWE-248',
    desc: 'body-parser is vulnerable to Denial of Service via trailing bytes after a compressed request body, resulting in unhandled exceptions and server thread hang.',
    remediation: 'Update body-parser to version 2.4.0 or later.'
  },
  {
    cve: 'GHSA-x5fp-wj9c-mxmx',
    pkg: 'qs',
    severity: 'Moderate',
    cvss: 3.7,
    installed: '6.14.2 - 6.15.3',
    fixedIn: '>= 6.16.0',
    cwe: 'CWE-770',
    desc: 'qs array-limit bypass via bracket-key comma parsing allows attackers to bypass memory restrictions on query parameter arrays.',
    remediation: 'Update qs dependency to >= 6.16.0.'
  },
  {
    cve: 'GHSA-4mjr-xmp4-gh2g',
    pkg: 'qs',
    severity: 'Moderate',
    cvss: 5.3,
    installed: '2.2.5 - 6.15.3',
    fixedIn: '>= 6.16.0',
    cwe: 'CWE-248, CWE-703',
    desc: 'Denial of Service via attacker-controlled isBuffer property causing unhandled TypeError exceptions.',
    remediation: 'Update qs dependency to >= 6.16.0.'
  },
  {
    cve: 'GHSA-6pq8-jhm2-2vcw',
    pkg: 'qs',
    severity: 'Moderate',
    cvss: 5.3,
    installed: '6.7.0 - 6.16.0',
    fixedIn: '> 6.16.0',
    cwe: 'CWE-248, CWE-704',
    desc: 'qs.stringify with arrayFormat comma throws uncaught TypeError on array elements carrying non-callable toString.',
    remediation: 'Update qs dependency to > 6.16.0.'
  }
];

function buildExcelWorkbook(workbook, primaryFocus) {
  // -------------------------------------------------------------
  // SHEET 1: Security Findings
  // -------------------------------------------------------------
  const sFindings = workbook.addWorksheet('Security Findings', { views: [{ state: 'frozen', ySplit: 1, showGridLines: true }] });
  sFindings.columns = [
    { header: 'Finding ID', key: 'id', width: 14 },
    { header: 'Severity', key: 'severity', width: 14 },
    { header: 'Vulnerability Type', key: 'type', width: 34 },
    { header: 'CWE ID', key: 'cwe', width: 18 },
    { header: 'OWASP Category', key: 'owasp', width: 28 },
    { header: 'File Path', key: 'file', width: 36 },
    { header: 'Endpoint', key: 'endpoint', width: 24 },
    { header: 'Description', key: 'desc', width: 44 },
    { header: 'Exploitation Scenario', key: 'scenario', width: 44 },
    { header: 'Impact', key: 'impact', width: 36 },
    { header: 'Remediation Recommendation', key: 'fix', width: 44 },
    { header: 'Status', key: 'status', width: 12 }
  ];

  sFindings.getRow(1).height = 28;
  sFindings.getRow(1).eachCell(c => {
    c.font = { name: 'Segoe UI', size: 10, bold: true, color: { argb: 'FFFFFFFF' } };
    c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF1E293B' } };
    c.alignment = { vertical: 'middle', horizontal: 'center' };
  });
  sFindings.autoFilter = { from: 'A1', to: 'L1' };

  findingsData.forEach((f, idx) => {
    const row = sFindings.addRow(f);
    row.height = 24;
    const isEven = idx % 2 === 0;
    row.eachCell((cell, col) => {
      cell.font = { name: 'Segoe UI', size: 9 };
      cell.alignment = { vertical: 'middle' };
      cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: isEven ? 'FFF8FAFC' : 'FFFFFFFF' } };
      cell.border = {
        top: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        left: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        bottom: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        right: { style: 'thin', color: { argb: 'FFE2E8F0' } }
      };
      if ([1, 4, 7, 12].includes(col)) cell.alignment = { vertical: 'middle', horizontal: 'center' };
      if (col === 2) {
        cell.alignment = { vertical: 'middle', horizontal: 'center' };
        if (f.severity === 'Critical') {
          cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FF991B1B' } };
          cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFFEF2F2' } };
        } else if (f.severity === 'High') {
          cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FFC2410C' } };
          cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFFFF7ED' } };
        } else if (f.severity === 'Medium') {
          cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FFB45309' } };
          cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFFFFBEB' } };
        } else {
          cell.font = { name: 'Segoe UI', size: 9, color: { argb: 'FF475569' } };
        }
      }
    });
  });

  // -------------------------------------------------------------
  // SHEET 2: Endpoint Inventory
  // -------------------------------------------------------------
  const sEndpoints = workbook.addWorksheet('Endpoint Inventory', { views: [{ state: 'frozen', ySplit: 1, showGridLines: true }] });
  sEndpoints.columns = [
    { header: 'Endpoint ID', key: 'id', width: 14 },
    { header: 'Endpoint URL', key: 'url', width: 28 },
    { header: 'HTTP Method', key: 'method', width: 14 },
    { header: 'Auth Required', key: 'auth', width: 16 },
    { header: 'Auth Mechanism', key: 'mech', width: 18 },
    { header: 'Expected Roles', key: 'role', width: 20 },
    { header: 'Controller / Source File', key: 'file', width: 38 },
    { header: 'Function Name', key: 'fn', width: 22 },
    { header: 'Security Risks / Status', key: 'risk', width: 44 }
  ];

  sEndpoints.getRow(1).height = 28;
  sEndpoints.getRow(1).eachCell(c => {
    c.font = { name: 'Segoe UI', size: 10, bold: true, color: { argb: 'FFFFFFFF' } };
    c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF1E293B' } };
    c.alignment = { vertical: 'middle', horizontal: 'center' };
  });
  sEndpoints.autoFilter = { from: 'A1', to: 'I1' };

  endpointData.forEach((ep, idx) => {
    const row = sEndpoints.addRow(ep);
    row.height = 22;
    const isEven = idx % 2 === 0;
    row.eachCell((cell, col) => {
      cell.font = { name: 'Segoe UI', size: 9 };
      cell.alignment = { vertical: 'middle' };
      cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: isEven ? 'FFF8FAFC' : 'FFFFFFFF' } };
      cell.border = {
        top: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        left: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        bottom: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        right: { style: 'thin', color: { argb: 'FFE2E8F0' } }
      };
      if ([1, 3, 4].includes(col)) cell.alignment = { vertical: 'middle', horizontal: 'center' };
      if (col === 3) {
        if (ep.method === 'GET') cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FF047857' } };
        if (ep.method === 'POST') cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FF1D4ED8' } };
        if (ep.method === 'PUT') cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FFB45309' } };
        if (ep.method === 'DELETE') cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FFB91C1C' } };
      }
    });
  });

  // -------------------------------------------------------------
  // SHEET 3: Dependency Vulnerabilities
  // -------------------------------------------------------------
  const sDeps = workbook.addWorksheet('Dependency Vulnerabilities', { views: [{ state: 'frozen', ySplit: 1, showGridLines: true }] });
  sDeps.columns = [
    { header: 'Advisory / CVE ID', key: 'cve', width: 28 },
    { header: 'Package Name', key: 'pkg', width: 18 },
    { header: 'Severity', key: 'severity', width: 14 },
    { header: 'CVSS Score', key: 'cvss', width: 14 },
    { header: 'Installed Version', key: 'installed', width: 18 },
    { header: 'Fixed In Version', key: 'fixedIn', width: 18 },
    { header: 'CWE Identifier', key: 'cwe', width: 22 },
    { header: 'Vulnerability Summary', key: 'desc', width: 44 },
    { header: 'Recommended Remediation', key: 'remediation', width: 44 }
  ];

  sDeps.getRow(1).height = 28;
  sDeps.getRow(1).eachCell(c => {
    c.font = { name: 'Segoe UI', size: 10, bold: true, color: { argb: 'FFFFFFFF' } };
    c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF1E293B' } };
    c.alignment = { vertical: 'middle', horizontal: 'center' };
  });
  sDeps.autoFilter = { from: 'A1', to: 'I1' };

  dependencyData.forEach((dep, idx) => {
    const row = sDeps.addRow(dep);
    row.height = 24;
    const isEven = idx % 2 === 0;
    row.eachCell((cell, col) => {
      cell.font = { name: 'Segoe UI', size: 9 };
      cell.alignment = { vertical: 'middle' };
      cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: isEven ? 'FFF8FAFC' : 'FFFFFFFF' } };
      cell.border = {
        top: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        left: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        bottom: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        right: { style: 'thin', color: { argb: 'FFE2E8F0' } }
      };
      if ([3, 4, 5, 6].includes(col)) cell.alignment = { vertical: 'middle', horizontal: 'center' };
      if (col === 3) {
        if (dep.severity === 'Critical') cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FF991B1B' } };
        if (dep.severity === 'High') cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FFC2410C' } };
        if (dep.severity === 'Moderate') cell.font = { name: 'Segoe UI', size: 9, bold: true, color: { argb: 'FFB45309' } };
      }
    });
  });

  // -------------------------------------------------------------
  // SHEET 4: Risk Summary
  // -------------------------------------------------------------
  const sSummary = workbook.addWorksheet('Risk Summary', { views: [{ showGridLines: true }] });

  sSummary.mergeCells('B2:H2');
  const tCell = sSummary.getCell('B2');
  tCell.value = 'SMART TRAVEL PLANNER - APPLICATION SECURITY POSTURE DASHBOARD';
  tCell.font = { name: 'Segoe UI', size: 15, bold: true, color: { argb: 'FFFFFFFF' } };
  tCell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF0F172A' } };
  tCell.alignment = { horizontal: 'center', vertical: 'middle' };
  sSummary.getRow(2).height = 36;

  sSummary.mergeCells('B3:H3');
  const stCell = sSummary.getCell('B3');
  stCell.value = 'Executive Vulnerability Distribution, OWASP API Top 10 Mapping & Remediation Scorecard';
  stCell.font = { name: 'Segoe UI', size: 10, italic: true, color: { argb: 'FF94A3B8' } };
  stCell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF1E293B' } };
  stCell.alignment = { horizontal: 'center', vertical: 'middle' };
  sSummary.getRow(3).height = 22;

  // KPI Metric Cards
  const kpis = [
    { cell: 'B5:C6', top: 'B5', label: 'OVERALL SECURITY SCORE', val: '42 / 100', color: 'FFB91C1C', bg: 'FFFEF2F2' },
    { cell: 'D5:D6', top: 'D5', label: 'CRITICAL RISKS', val: '3', color: 'FF991B1B', bg: 'FFFEF2F2' },
    { cell: 'E5:E6', top: 'E5', label: 'HIGH RISKS', val: '5', color: 'FFC2410C', bg: 'FFFFF7ED' },
    { cell: 'F5:F6', top: 'F5', label: 'MEDIUM RISKS', val: '3', color: 'FFB45309', bg: 'FFFFFBEB' },
    { cell: 'G5:H6', top: 'G5', label: 'TOTAL FINDINGS', val: '13', color: 'FF1E40AF', bg: 'FFEFF6FF' }
  ];

  kpis.forEach(k => {
    sSummary.mergeCells(k.cell);
    const c = sSummary.getCell(k.top);
    c.value = `${k.label}\n${k.val}`;
    c.font = { name: 'Segoe UI', size: 11, bold: true, color: { argb: k.color } };
    c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: k.bg } };
    c.alignment = { horizontal: 'center', vertical: 'middle', wrapText: true };
    c.border = {
      top: { style: 'thin', color: { argb: k.color } },
      left: { style: 'thin', color: { argb: k.color } },
      bottom: { style: 'thin', color: { argb: k.color } },
      right: { style: 'thin', color: { argb: k.color } }
    };
  });
  sSummary.getRow(5).height = 24;
  sSummary.getRow(6).height = 24;

  // OWASP API Top 10 Mapping Table
  const owaspHeaderRow = 9;
  sSummary.getCell(`B${owaspHeaderRow}`).value = 'OWASP API TOP 10 (2023) VULNERABILITY EXPOSURE';
  sSummary.getCell(`B${owaspHeaderRow}`).font = { name: 'Segoe UI', size: 11, bold: true, color: { argb: 'FF0F172A' } };
  sSummary.mergeCells(`B${owaspHeaderRow}:H${owaspHeaderRow}`);

  const owaspHeaders = ['OWASP Category', 'Category Name', 'Findings Count', 'Max Severity', 'Affected Endpoints / Files'];
  const owaspCols = ['B', 'C', 'D', 'E', 'F'];
  owaspHeaders.forEach((h, idx) => {
    const c = sSummary.getCell(`${owaspCols[idx]}10`);
    c.value = h;
    c.font = { name: 'Segoe UI', size: 10, bold: true, color: { argb: 'FFFFFFFF' } };
    c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF334155' } };
    c.alignment = { horizontal: idx <= 1 ? 'left' : 'center', vertical: 'middle' };
  });
  sSummary.mergeCells('F10:H10');
  sSummary.getRow(10).height = 22;

  const owaspRows = [
    ['API1:2023', 'Broken Object Level Authorization (BOLA/IDOR)', '5', 'Critical', 'trips/:id, bookings/trip/:id, expenses/trip/:id'],
    ['API2:2023', 'Broken Authentication (Backdoors & Weak JWT)', '2', 'Critical', 'auth/login, middleware/auth.js'],
    ['API3:2023', 'Broken Object Property Level Authorization', '1', 'Medium', 'auth/user fallback exposure'],
    ['API4:2023', 'Unrestricted Resource Consumption', '1', 'Medium', 'auth/login, auth/signup (no rate limit)'],
    ['API8:2023', 'Security Misconfiguration & Secrets', '4', 'High', 'backend/.env, destinations ReDoS, CORS']
  ];

  let oRow = 11;
  owaspRows.forEach(r => {
    sSummary.getCell(`B${oRow}`).value = r[0];
    sSummary.getCell(`C${oRow}`).value = r[1];
    sSummary.getCell(`D${oRow}`).value = r[2];
    sSummary.getCell(`D${oRow}`).alignment = { horizontal: 'center' };
    sSummary.getCell(`E${oRow}`).value = r[3];
    sSummary.getCell(`E${oRow}`).alignment = { horizontal: 'center' };
    if (r[3] === 'Critical') sSummary.getCell(`E${oRow}`).font = { name: 'Segoe UI', bold: true, color: { argb: 'FF991B1B' } };
    if (r[3] === 'High') sSummary.getCell(`E${oRow}`).font = { name: 'Segoe UI', bold: true, color: { argb: 'FFC2410C' } };
    if (r[3] === 'Medium') sSummary.getCell(`E${oRow}`).font = { name: 'Segoe UI', color: { argb: 'FFB45309' } };

    sSummary.getCell(`F${oRow}`).value = r[4];
    sSummary.mergeCells(`F${oRow}:H${oRow}`);

    ['B', 'C', 'D', 'E', 'F', 'G', 'H'].forEach(col => {
      sSummary.getCell(`${col}${oRow}`).border = {
        top: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        left: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        bottom: { style: 'thin', color: { argb: 'FFE2E8F0' } },
        right: { style: 'thin', color: { argb: 'FFE2E8F0' } }
      };
    });
    sSummary.getRow(oRow).height = 20;
    oRow++;
  });

  sSummary.getColumn('A').width = 4;
  sSummary.getColumn('B').width = 16;
  sSummary.getColumn('C').width = 34;
  sSummary.getColumn('D').width = 16;
  sSummary.getColumn('E').width = 16;
  sSummary.getColumn('F').width = 24;
  sSummary.getColumn('G').width = 16;
  sSummary.getColumn('H').width = 16;
}

async function generateAll() {
  const targets = [
    'C:\\Projects\\smartTravelPlanner\\Vulnerability Test Results',
    'C:\\Projects\\smartTravelPlanner\\smartTravelPlanner\\Vulnerability Test Results'
  ];

  for (const dir of targets) {
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

    // 1. findings.xlsx
    const wbFindings = new ExcelJS.Workbook();
    buildExcelWorkbook(wbFindings, 'findings');
    const fPath = path.join(dir, 'findings.xlsx');
    await wbFindings.xlsx.writeFile(fPath);
    console.log(`Saved: ${fPath}`);

    // 2. endpoint-inventory.xlsx
    const wbEndpoints = new ExcelJS.Workbook();
    buildExcelWorkbook(wbEndpoints, 'endpoints');
    const epPath = path.join(dir, 'endpoint-inventory.xlsx');
    await wbEndpoints.xlsx.writeFile(epPath);
    console.log(`Saved: ${epPath}`);
  }
}

generateAll().catch(console.error);
