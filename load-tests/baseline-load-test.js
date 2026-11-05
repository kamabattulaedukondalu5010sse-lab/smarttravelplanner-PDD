import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// Custom metrics for granular reporting
const failureRate = new Rate('failed_requests');
const apiResponseTime = new Trend('api_response_time');

/**
 * ============================================================================
 * BASELINE LOAD TEST CONFIGURATION
 * ============================================================================
 * - 100 Virtual Users (VUs) running concurrently
 * - Continuous duration: 1 minute (60s)
 * - Expected throughput: ~100 to 150 requests/second
 * - Total requests: ~6,000 to 9,000 requests in 60s
 * ============================================================================
 */
export const options = {
  scenarios: {
    baseline_load: {
      executor: 'constant-vus',
      vus: 100,
      duration: '1m',
    },
  },
  thresholds: {
    // 1. Error Rate: Less than 1% failed requests
    http_req_failed: ['rate<0.01'],
    failed_requests: ['rate<0.01'],

    // 2. Response Time SLA Thresholds
    // 95% of requests must complete under 500ms
    http_req_duration: ['p(95)<500', 'avg<300'],
    api_response_time: ['p(95)<500', 'max<1500'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'http://127.0.0.1:5000';

export default function () {
  const jsonHeaders = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  // 1. Destination Discovery API (Lightweight read endpoint)
  group('1. Public Destinations Feed', function () {
    const res = http.get(`${BASE_URL}/api/destinations`, { headers: jsonHeaders });
    
    apiResponseTime.add(res.timings.duration);
    const passed = check(res, {
      'Destinations status is 200': (r) => r.status === 200,
      'Response has destinations data': (r) => r.body && r.body.length > 0,
      'Response time < 500ms': (r) => r.timings.duration < 500,
    });

    failureRate.add(!passed);
  });

  // Short realistic user think time between actions (0.5s - 1s)
  sleep(0.5);

  // 2. User Authentication (Login endpoint)
  group('2. User Authentication API', function () {
    const payload = JSON.stringify({
      email: 'john@example.com',
      password: 'anypassword',
    });

    const res = http.post(`${BASE_URL}/api/auth/login`, payload, { headers: jsonHeaders });
    
    apiResponseTime.add(res.timings.duration);
    const passed = check(res, {
      'Login status is 200': (r) => r.status === 200,
      'Token present in response': (r) => {
        try {
          return JSON.parse(r.body).token !== undefined;
        } catch (e) {
          return false;
        }
      },
    });

    failureRate.add(!passed);
  });

  // Pacing sleep to simulate realistic human click stream while maintaining steady VU concurrency
  sleep(0.5);
}
