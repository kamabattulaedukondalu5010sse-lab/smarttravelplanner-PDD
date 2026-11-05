import http from 'k6/http';
import { check, sleep } from 'k6';
import { getAuthToken, getAuthHeaders } from '../helpers/auth.js';

export function runSmokeScenario(baseUrl) {
  // 1. Root health check
  const resRoot = http.get(`${baseUrl}/`);
  check(resRoot, {
    'LOAD-001: Root returns 200': (r) => r.status === 200,
    'LOAD-001: Root has status or message': (r) => r.body.includes('Smart Travel') || r.body.includes('status')
  });

  // 2. Auth login baseline
  const token = getAuthToken(baseUrl);
  check(token, {
    'LOAD-002: Valid JWT token acquired': (t) => t && t.length > 5
  });

  const authHeaders = getAuthHeaders(token);

  // 3. Destinations baseline
  const resDest = http.get(`${baseUrl}/api/destinations`);
  check(resDest, {
    'LOAD-005: Destinations status 200': (r) => r.status === 200,
    'LOAD-005: Destinations array is non-empty': (r) => Array.isArray(r.json()) && r.json().length > 0
  });

  // 4. Destination search filter
  const resSearch = http.get(`${baseUrl}/api/destinations?search=Goa`);
  check(resSearch, {
    'LOAD-006: Search Goa returns 200': (r) => r.status === 200,
    'LOAD-006: Search returns matching items': (r) => r.body.toLowerCase().includes('goa')
  });

  // 5. User profile
  const resProfile = http.get(`${baseUrl}/api/auth/user`, authHeaders);
  check(resProfile, {
    'LOAD-011: User profile status 200': (r) => r.status === 200,
    'LOAD-011: User profile has email': (r) => r.json('email') !== undefined
  });

  // 6. User trips list
  const resTrips = http.get(`${baseUrl}/api/trips`, authHeaders);
  check(resTrips, {
    'LOAD-014: Trips list status 200': (r) => r.status === 200,
    'LOAD-014: Trips is array': (r) => Array.isArray(r.json())
  });

  // 7. User bookings list
  const resBookings = http.get(`${baseUrl}/api/bookings`, authHeaders);
  check(resBookings, {
    'LOAD-021: Bookings list status 200': (r) => r.status === 200
  });

  // 8. Trip planning POST
  const tripPayload = JSON.stringify({
    destination: 'Goa',
    startDate: '2026-06-01',
    endDate: '2026-06-05',
    travelersCount: 2,
    budget: 25000
  });
  const resCreateTrip = http.post(`${baseUrl}/api/trips`, tripPayload, authHeaders);
  check(resCreateTrip, {
    'LOAD-017: Create trip status 200 or 201': (r) => r.status === 200 || r.status === 201
  });

  sleep(1);
}
