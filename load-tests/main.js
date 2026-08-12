import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { BASE_URL, USERNAME, PASSWORD } from './config.js';
import { generateRandomUser } from './helpers.js';

export const options = {
  stages: [
    { duration: '30s', target: 20 },
    { duration: '1m', target: 100 },
    { duration: '30s', target: 0 }
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'http_req_duration{scenario:default}': ['p(90)<400']
  }
};

export default function () {
  let authToken = '';
  let createdUserId = '';

  // Step 1: Authentication API
  group('1. Authentication API', function () {
    const res = http.post(`${BASE_URL}/api/v1/auth/login`, JSON.stringify({
      username: USERNAME,
      password: PASSWORD
    }), {
      headers: { 'Content-Type': 'application/json' }
    });

    check(res, {
      'Auth status 200': (r) => r.status === 200,
      'Response time < 300ms': (r) => r.timings.duration < 300
    });

    authToken = res.json('token') || 'dummy-token';
  });

  const authParams = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${authToken}`
    }
  };

  sleep(1);

  // Step 2: Get Users API
  group('2. Get Users API', function () {
    const res = http.get(`${BASE_URL}/api/v1/users`, authParams);
    check(res, {
      'Get Users status 200': (r) => r.status === 200
    });
  });

  sleep(1);

  // Step 3: Create User API
  group('3. Create User API', function () {
    const payload = generateRandomUser();
    const res = http.post(`${BASE_URL}/api/v1/users`, JSON.stringify(payload), authParams);
    check(res, {
      'Create User status 200/201': (r) => r.status === 200 || r.status === 201
    });

    createdUserId = res.json('id') || '101';
  });

  sleep(1);

  // Step 4: Update User API
  group('4. Update User API', function () {
    const payload = { name: 'Updated Name', role: 'Senior Planner' };
    const res = http.put(`${BASE_URL}/api/v1/users/${createdUserId}`, JSON.stringify(payload), authParams);
    check(res, {
      'Update User status 200': (r) => r.status === 200
    });
  });

  sleep(1);

  // Step 5: Delete User API
  group('5. Delete User API', function () {
    const res = http.del(`${BASE_URL}/api/v1/users/${createdUserId}`, null, authParams);
    check(res, {
      'Delete User status 200/204': (r) => r.status === 200 || r.status === 204
    });
  });

  sleep(1);
}
