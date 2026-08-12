import http from 'k6/http';
import { check, sleep } from 'k6';
import { BASE_URL } from './config.js';
import { generateRandomUser } from './helpers.js';

export const options = {
  vus: 30,
  duration: '1m',
  thresholds: {
    http_req_duration: ['p(95)<450'],
    http_req_failed: ['rate<0.01']
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

  // 1. GET Users List
  const getRes = http.get(`${BASE_URL}/api/v1/users`, params);
  check(getRes, {
    'GET /users status is 200': (r) => r.status === 200,
    'Users list is array': (r) => Array.isArray(r.json()) || r.json('data') !== undefined
  });

  sleep(1);

  // 2. POST Create User
  const newUser = generateRandomUser();
  const postRes = http.post(`${BASE_URL}/api/v1/users`, JSON.stringify(newUser), params);
  check(postRes, {
    'POST /users status is 201 or 200': (r) => r.status === 201 || r.status === 200,
    'User ID returned': (r) => r.json('id') !== undefined || r.json('_id') !== undefined
  });

  sleep(1);
}
