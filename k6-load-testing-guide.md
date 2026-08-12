# Comprehensive Master Guide: API Load Testing with Grafana k6

---

## 1. What is Load Testing?

### Performance Testing Overview
Performance Testing evaluates how a system performs under specific workloads in terms of responsiveness, stability, scalability, and resource utilization.

```
                  +-------------------------------------------------+
                  |              PERFORMANCE TESTING                |
                  +------------------------+------------------------+
                                           |
    +-----------------+--------------------+------------------+------------------+
    |                 |                    |                  |                  |
+---v---+         +---v---+            +---v---+          +---v---+          +---v---+
| Load  |         |Stress |            | Spike |          | Soak  |         | Break |
|Testing|         |Testing|            |Testing|          |Testing|         | Point |
+-------+         +-------+            +-------+          +-------+         +-------+
```

### Types of Performance Tests
1. **Load Testing**: Evaluates system behavior under expected normal and peak virtual user traffic.
2. **Stress Testing**: Pushes the system beyond normal operational limits to find breaking points.
3. **Spike Testing**: Tests the system's reaction to sudden, extreme surges in user traffic.
4. **Soak (Endurance) Testing**: Tests system stability over extended durations (e.g., 12–24 hours) to detect memory leaks.

### Why API Load Testing Matters
- Detects database lock contention and connection pool exhaustion before production deployment.
- Prevents revenue loss caused by service downtime during flash sales or traffic spikes.
- Ensures SLA compliance (e.g., 99.9% uptime, p95 response time < 300ms).

---

## 2. Installing k6 (Windows)

### Step 1: Install using Winget
Search for the official Grafana k6 package:
```powershell
winget search k6
```
Install Grafana k6:
```powershell
winget install GrafanaLabs.k6
```

### Step 2: Verify Installation
Verify that the executable is registered in system environment variables:
```powershell
k6 version
```
*Expected Output*: `k6 v0.48.0 (2024-01-15T10:00:00+0000, go1.21.6, windows/amd64)`

---

## 3. Running a Test

Execute k6 test scripts via command line:
```bash
k6 run filename.js
```

### Recommended Project Structure
```
load-tests/
├── config.js       # Target URLs, VU stages, thresholds
├── helpers.js      # Utility functions and test data generators
├── login.js        # Authentication endpoint test
├── users.js        # User management CRUD endpoint test
├── main.js         # Unified test suite
└── README.md
```

---

## 4. Baseline Load Test (100 VUs, 1 Minute)

### Core Concepts Explained
- **Virtual Users (VUs)**: Concurrent execution threads simulating real user interactions.
- **Duration**: Total time the test scenario executes.
- **Iteration**: One complete execution loop of the `default` exported function.
- **Check**: Boolean assertion validating response codes, payload body, or headers without aborting execution.
- **Sleep**: Pause duration between requests simulating real-world "think time".

### Baseline Test Script (`baseline.js`)
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 100,
  duration: '1m',
};

export default function () {
  const res = http.get('https://test-api.k6.io/public/crocodiles/');
  
  check(res, {
    'Status is 200': (r) => r.status === 200,
    'Response duration < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1);
}
```

---

## 5. Sample API Load Test Script (GET, POST, Auth, Headers, Thresholds)

```javascript
import http from 'k6/http';
import { check, group, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 50 },  // Ramp up
    { duration: '1m',  target: 100 }, // Steady peak
    { duration: '30s', target: 0 },   // Ramp down
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],    // Error rate must be less than 1%
    http_req_duration: ['p(95)<400'],  // 95% of requests must complete under 400ms
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://api.example.com';

export default function () {
  group('Authentication & Data Pipeline', function () {
    // POST Request
    const authPayload = JSON.stringify({ username: 'testuser', password: 'SecretPassword123' });
    const authParams = { headers: { 'Content-Type': 'application/json' } };
    const authRes = http.post(`${BASE_URL}/api/v1/auth/login`, authPayload, authParams);

    check(authRes, {
      'Auth status 200': (r) => r.status === 200,
      'Has Auth Token': (r) => r.json('token') !== undefined,
    });

    const token = authRes.json('token');
    const userParams = {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
    };

    // GET Request
    const getRes = http.get(`${BASE_URL}/api/v1/users`, userParams);
    check(getRes, {
      'Get Users status 200': (r) => r.status === 200,
      'JSON Array Returned': (r) => Array.isArray(r.json()),
    });
  });

  sleep(1);
}
```

---

## 6. Understanding k6 Metrics

| Metric Name | Description |
| :--- | :--- |
| `http_reqs` | Total number of HTTP requests generated by k6 VUs. |
| `iterations` | Total number of times the `default` function was executed. |
| `vus` | Number of active virtual users right now. |
| `vus_max` | Maximum configured allocation of virtual users. |
| `data_received` | Total amount of data downloaded from target API. |
| `data_sent` | Total amount of data uploaded to target API. |
| `checks` | Percentage of passed vs failed assertions. |
| `http_req_duration` | Total time for request round-trip (`http_req_sending` + `http_req_waiting` + `http_req_receiving`). |
| `http_req_waiting` | Time spent waiting for server response (Time To First Byte / TTFB). |
| `http_req_blocked` | Time spent waiting before starting request (TCP connection/DNS lookups). |
| `http_req_connecting` | Time spent establishing TCP connection to server. |
| `http_req_failed` | Percentage of failed HTTP requests (status >= 400). |

---

## 7. Requests Per Second (RPS)

RPS measures throughput:
$$\text{RPS} = \frac{\text{Total HTTP Requests}}{\text{Duration in Seconds}}$$

### Example Analysis
If k6 reports `http_reqs ..........: 7200 120/s`:
- **120 req/sec**: Your API successfully processed ~120 requests every second during the test run.
- **RPS Scale Ratings**:
  - **< 50 req/sec**: Low throughput (Suitable for internal microservices/admin panels).
  - **50–500 req/sec**: Moderate throughput (Standard B2B SaaS applications).
  - **500–5000+ req/sec**: High throughput (E-commerce flash sales, payment gateways).

---

## 8. Response Time Percentiles

- **avg**: Arithmetic mean of all response times.
- **min / max**: Absolute fastest and slowest recorded response times.
- **med (p50)**: 50% of requests were faster than this value.
- **p90**: 90% of requests were faster than this value.
- **p95**: 95% of requests were faster than this value (Industry standard SLA benchmark).

### Acceptable Response Time Thresholds

| Environment | Target avg | Target p95 | Target max |
| :--- | :--- | :--- | :--- |
| **Development** | < 200ms | < 500ms | < 1500ms |
| **Testing / Staging** | < 100ms | < 300ms | < 1000ms |
| **Production** | < 50ms | < 200ms | < 500ms |

---

## 9. Performance Benchmarks

```
   < 100ms          100ms - 300ms        300ms - 800ms          > 800ms
[ EXCELLENT ] ------> [ GOOD ] ------> [ ACCEPTABLE ] ------> [ POOR / FIX ]
```

- **< 100ms**: Excellent. Extremely fast user experience.
- **100–300ms**: Good. Standard performance.
- **300–800ms**: Acceptable under peak stress loads.
- **> 800ms**: Poor. Immediate performance optimization required.

---

## 10. Common Performance Bottlenecks

1. **Database Lock Contention & Missing Indexes**: Slow `SELECT` queries or unindexed foreign key joins.
2. **Connection Pool Exhaustion**: Too few DB client connections configured (`max_connections`).
3. **Memory Leaks & Garbage Collection Pauses**: Node.js/Java heap memory leaks causing full GC pauses.
4. **CPU Saturation**: Single-threaded Node.js event-loop blocking operations (e.g. sync crypto/hashing).
5. **Lack of Caching Layer**: Re-computing expensive API responses without Redis/Memcached.

---

## 11. Running Multiple APIs in One k6 Script

```javascript
import http from 'k6/http';
import { check, group, sleep } from 'k6';

export default function () {
  let token = '';
  let userId = '';

  group('1. Login API', () => {
    const res = http.post('https://api.example.com/login', JSON.stringify({ user: 'admin', pass: 'pass' }), { headers: { 'Content-Type': 'application/json' } });
    token = res.json('token');
  });

  const headers = { headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' } };

  group('2. Get Users API', () => {
    http.get('https://api.example.com/users', headers);
  });

  group('3. Create User API', () => {
    const res = http.post('https://api.example.com/users', JSON.stringify({ name: 'Alice' }), headers);
    userId = res.json('id');
  });

  group('4. Update User API', () => {
    http.put(`https://api.example.com/users/${userId}`, JSON.stringify({ name: 'Alice Updated' }), headers);
  });

  group('5. Delete User API', () => {
    http.del(`https://api.example.com/users/${userId}`, null, headers);
  });

  sleep(1);
}
```

---

## 12. Environment Variables (`__ENV`)

Pass runtime variables directly into k6 via `-e` command line flags:
```bash
k6 run -e BASE_URL=https://staging.api.com -e VUS=200 main.js
```
Access inside JS scripts:
```javascript
const BASE_URL = __ENV.BASE_URL || 'https://default.api.com';
```

---

## 13. HTML Reports

Generate single-file standalone HTML reports by utilizing `handleSummary`:

```javascript
import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js';

export function handleSummary(data) {
  return {
    'reports/load_test_summary.html': htmlReport(data),
  };
}
```

---

## 14. Grafana & InfluxDB Live Monitoring

```
+---------+         +------------------+         +-------------------+
|  k6     | ------> | InfluxDB         | ------> | Grafana           |
| Engine  | (Stats) | (Time-Series DB) | (Query) | (Live Dashboards) |
+---------+         +------------------+         +-------------------+
```

Run k6 with real-time stats output streamed to InfluxDB:
```bash
k6 run --out influxdb=http://localhost:8086/k6db main.js
```

---

## 15. GitHub Actions Integration

Automate performance regression checks on every `push` and `pull_request` using `.github/workflows/load-test.yml`.

---

## 16. Complete GitHub Actions Workflow (`.github/workflows/load-test.yml`)

```yaml
name: k6 API Load Testing Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  k6_load_test:
    name: Run k6 Load Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Install k6
        run: |
          sudo gpg -k
          sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
          echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
          sudo apt-get update
          sudo apt-get install -y k6

      - name: Execute k6 Load Test Suite
        env:
          BASE_URL: "https://test-api.k6.io"
        run: |
          mkdir -p reports
          k6 run --out json=reports/results.json load-tests/main.js

      - name: Upload Load Test Reports
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: k6-load-test-reports
          path: reports/
```

---

## 17. Best Practices

1. **Never load test production without prior scheduling and isolation.**
2. **Use dynamic test data** to prevent database caching skew.
3. **Include realistic `sleep()` think times** between requests (1–3 seconds).
4. **Define SLA thresholds (`thresholds`)** to automatically fail CI pipelines on latency degradation.

---

## 18. Folder Structure

```
load-tests/
├── config.js
├── helpers.js
├── login.js
├── users.js
└── main.js
.github/
└── workflows/
    └── load-test.yml
```

---

## 19. 30 Performance Testing & k6 Interview Questions & Answers

1. **Q: What is the main difference between k6 and JMeter?**
   *A:* k6 is developer-centric, lightweight, written in Go with JavaScript ES6 scripting, consuming drastically less CPU/RAM than JMeter's Java GUI-heavy threads.
2. **Q: What are Virtual Users (VUs) in k6?**
   *A:* Concurrent execution loops running in isolated JavaScript runtimes.
3. **Q: How do `checks` differ from `thresholds` in k6?**
   *A:* Checks evaluate boolean conditions without stopping execution; thresholds fail the test run if metrics fall short of SLAs.
4. **Q: What metric represents TTFB (Time To First Byte)?**
   *A:* `http_req_waiting`.
5. **Q: What is p95 response time?**
   *A:* The latency limit under which 95% of all HTTP requests fall.
6. **Q: How do you pass environment variables to k6?**
   *A:* Using the `-e KEY=VALUE` CLI flag and accessing `__ENV.KEY` in JS scripts.
7. **Q: What is Soak Testing?**
   *A:* Running a load test over a prolonged period (12-24h) to uncover memory leaks and system degradation over time.
8. **Q: What is Spike Testing?**
   *A:* Testing system resilience against sudden, huge surges in virtual user traffic.
9. **Q: How does k6 handle cookies and sessions?**
   *A:* Each VU automatically maintains its own isolated cookie jar across iterations.
10. **Q: What is `http_req_failed` metric?**
    *A:* The percentage rate of failed HTTP requests (status code >= 400).
11. **Q: How do you configure ramping stages in k6?**
    *A:* By defining `stages` in `options` with target VU levels and ramp durations.
12. **Q: What is `sleep()` used for in k6?**
    *A:* To simulate human "think time" between API requests.
13. **Q: What is RPS?**
    *A:* Requests Per Second, measuring throughput processed by the backend.
14. **Q: Why should you avoid testing production directly?**
    *A:* It risks data corruption, accidental email blasts, and service outage for real users.
15. **Q: What is Grafana InfluxDB integration in k6?**
    *A:* k6 streams metric time-series data to InfluxDB, which Grafana queries for real-time visualization dashboards.
16. **Q: How can you fail a GitHub Actions workflow on k6 threshold failure?**
    *A:* k6 automatically returns exit code `99` when thresholds fail, which causes CI workflow steps to fail.
17. **Q: What is `group()` in k6?**
    *A:* A function to organize BDD test steps and metric aggregations.
18. **Q: Can k6 test WebSocket and gRPC APIs?**
    *A:* Yes, k6 has built-in native support for WebSockets and gRPC.
19. **Q: What is the difference between Ramp-Up and Ramp-Down?**
    *A:* Ramp-up gradually increases VUs to peak load; ramp-down gradually reduces VUs back to zero.
20. **Q: How do you handle OAuth2 authentication tokens in k6?**
    *A:* Make an initial POST request to the auth endpoint, extract the token from the response JSON, and pass it in subsequent request headers.
21. **Q: What is TCP connection time metric in k6?**
    *A:* `http_req_connecting`.
22. **Q: How do you generate HTML reports in k6?**
    *A:* By exporting `handleSummary(data)` using `htmlReport`.
23. **Q: What is connection pool exhaustion?**
    *A:* When all database connections in a pool are busy, forcing new requests to queue up and time out.
24. **Q: What is single-threaded event loop bottleneck in Node.js?**
    *A:* Synchronous intensive CPU operations blocking the main thread from handling incoming HTTP requests.
25. **Q: What is throughput vs latency?**
    *A:* Throughput is how many requests are handled per second (RPS); latency is how long a single request takes to complete (ms).
26. **Q: What is the purpose of options in a k6 script?**
    *A:* To configure VUs, duration, stages, thresholds, and execution options programmatically inside the test script.
27. **Q: How do you validate JSON response properties in k6?**
    *A:* Using `res.json('path.to.property')` inside `check()` assertions.
28. **Q: What is threshold syntax for p95 latency under 500ms?**
    *A:* `thresholds: { http_req_duration: ['p(95)<500'] }`.
29. **Q: How do you run load tests headlessly in CI/CD?**
    *A:* Run `k6 run` directly in CLI mode inside Linux runners without any graphical display requirements.
30. **Q: What metric shows total downloaded bandwidth in k6?**
    *A:* `data_received`.

---

## 20. Summary & Cheat Sheet

```bash
# Installation (Windows)
winget install GrafanaLabs.k6

# Verify version
k6 version

# Basic Run
k6 run test.js

# Run with 50 VUs for 30 Seconds
k6 run --vus 50 --duration 30s test.js

# Run with Environment Variables
k6 run -e BASE_URL=https://api.example.com -e TOKEN=mytoken test.js

# Stream Metrics to InfluxDB
k6 run --out influxdb=http://localhost:8086/k6db test.js
```

### Performance SLA Benchmarks
- **p95 Latency**: `< 300ms` (Staging) | `< 200ms` (Production)
- **Error Rate**: `< 1%`
- **RPS Target**: `> 100 req/sec`
