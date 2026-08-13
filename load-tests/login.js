import http from 'k6/http';
import { check, sleep } from 'k6';
import { BASE_URL, USERNAME, PASSWORD } from './config.js';
import { logIfError } from './helpers.js';

export const options = {
  vus: 10,
  duration: '15s',
  thresholds: {
    http_req_duration: ['p(95)<2500'],
    http_req_failed: ['rate<0.05']
  }
};

export default function () {
  const url = `${BASE_URL}/api/auth/login`;
  const payload = JSON.stringify({
    email: USERNAME,
    password: PASSWORD
  });

  const params = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  let res = http.post(url, payload, params);

  // If login fails because user is not registered yet, register user via signup
  if (res.status === 400 || res.status === 404) {
    const signupPayload = JSON.stringify({
      name: 'Load Test User',
      email: USERNAME,
      password: PASSWORD
    });
    res = http.post(`${BASE_URL}/api/auth/signup`, signupPayload, params);
  }

  logIfError(res);

  check(res, {
    'Login returns 200/201 and token': (r) => (r.status === 200 || r.status === 201) && r.json('token') !== undefined
  });

  sleep(1);
}
