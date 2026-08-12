export const BASE_URL = __ENV.BASE_URL || 'https://api.example.com';
export const USERNAME = __ENV.USERNAME || 'testuser@example.com';
export const PASSWORD = __ENV.PASSWORD || 'SecretPassword123!';

export const options = {
  stages: [
    { duration: '30s', target: 20 },  // Ramp-up to 20 VUs
    { duration: '1m', target: 100 },  // Stay at 100 VUs baseline
    { duration: '30s', target: 0 }    // Ramp-down to 0 VUs
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],   // Error rate must be < 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must complete within 500ms
    http_reqs: ['count>100']
  }
};
