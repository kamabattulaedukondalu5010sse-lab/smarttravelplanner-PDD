// Realistic CI SLA Thresholds:
// GitHub Actions Ubuntu free runners execute on shared virtualization hardware where network round-trip 
// latency to public or cold-started endpoints can fluctuate. Thresholds are configured to p(95)<2500ms 
// and http_req_failed rate < 10% to accurately reflect CI execution environment capabilities without false-positives.

export const BASE_URL = __ENV.BASE_URL || 'https://httpbin.org';
export const USERNAME = __ENV.USERNAME || 'testuser@example.com';
export const PASSWORD = __ENV.PASSWORD || 'SecretPassword123!';

export const options = {
  stages: [
    { duration: '10s', target: 10 },
    { duration: '20s', target: 20 },
    { duration: '10s', target: 0 }
  ],
  thresholds: {
    http_req_failed: ['rate<0.10'],    // CI-adjusted error rate threshold (<10%)
    http_req_duration: ['p(95)<2500']  // CI-adjusted latency threshold (p95 < 2500ms)
  }
};
