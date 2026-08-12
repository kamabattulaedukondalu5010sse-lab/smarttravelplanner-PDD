import http from 'k6/http';
import { check, sleep } from 'k6';
import { BASE_URL, USERNAME, PASSWORD } from './config.js';

export const options = {
  vus: 50,
  duration: '45s',
  thresholds: {
    http_req_duration: ['p(95)<400'],
    http_req_failed: ['rate<0.02']
  }
};

export default function () {
  const url = `${BASE_URL}/api/v1/auth/login`;
  const payload = JSON.stringify({
    username: USERNAME,
    password: PASSWORD
  });

  const params = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  const res = http.post(url, payload, params);

  check(res, {
    'Login response code is 200': (r) => r.status === 200,
    'Response contains access_token': (r) => r.json('token') !== null || r.json('access_token') !== null,
    'Response time under 500ms': (r) => r.timings.duration < 500
  });

  sleep(1);
}
