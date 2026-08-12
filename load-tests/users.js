import http from 'k6/http';
import { check, sleep } from 'k6';
import { BASE_URL } from './config.js';
import { generateRandomUser } from './helpers.js';

export const options = {
  vus: 20,
  duration: '15s',
  thresholds: {
    http_req_duration: ['p(95)<1500'],
    http_req_failed: ['rate<0.05']
  }
};

export default function () {
  const token = __ENV.TOKEN || 'Bearer sample_token_123';
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  };

  // 1. GET Users
  const getRes = http.get(`${BASE_URL}/get`, params);
  check(getRes, {
    'GET /users status is 200': (r) => r.status === 200
  });

  sleep(1);

  // 2. POST User
  const newUser = generateRandomUser();
  const postRes = http.post(`${BASE_URL}/post`, JSON.stringify(newUser), params);
  check(postRes, {
    'POST /users status is 200': (r) => r.status === 200
  });

  sleep(1);
}
