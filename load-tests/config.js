export const BASE_URL = __ENV.BASE_URL || 'https://httpbin.org';
export const USERNAME = __ENV.USERNAME || 'testuser@example.com';
export const PASSWORD = __ENV.PASSWORD || 'SecretPassword123!';

export const options = {
  stages: [
    { duration: '10s', target: 10 },  // Ramp-up to 10 VUs
    { duration: '20s', target: 30 },  // Steady peak VUs
    { duration: '10s', target: 0 }    // Ramp-down
  ],
  thresholds: {
    http_req_failed: ['rate<0.05'],   // Error rate must be < 5%
    http_req_duration: ['p(95)<1500'] // 95% of requests within 1500ms
  }
};
