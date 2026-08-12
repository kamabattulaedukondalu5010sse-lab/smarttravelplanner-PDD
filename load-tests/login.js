import http from 'k6/http';
import { check, sleep } from 'k6';
import { BASE_URL, USERNAME, PASSWORD } from './config.js';

export const options = {
  vus: 20,
  duration: '15s',
  thresholds: {
    http_req_duration: ['p(95)<1500'],
    http_req_failed: ['rate<0.05']
  }
};

export default function () {
  const url = `${BASE_URL}/post`;
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
    'Response timing acceptable': (r) => r.timings.duration < 2000
  });

  sleep(1);
}
