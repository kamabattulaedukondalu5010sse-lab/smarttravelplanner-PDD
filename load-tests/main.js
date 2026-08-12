import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { BASE_URL, USERNAME, PASSWORD } from './config.js';
import { generateRandomUser } from './helpers.js';

export const options = {
  stages: [
    { duration: '10s', target: 10 },
    { duration: '20s', target: 30 },
    { duration: '10s', target: 0 }
  ],
  thresholds: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<1500']
  }
};

export default function () {
  const authParams = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer sample_jwt_token_123'
    }
  };

  // Step 1: Authentication API
  group('1. Authentication API', function () {
    const res = http.post(`${BASE_URL}/post`, JSON.stringify({
      username: USERNAME,
      password: PASSWORD
    }), {
      headers: { 'Content-Type': 'application/json' }
    });

    check(res, {
      'Auth status 200': (r) => r.status === 200
    });
  });

  sleep(1);

  // Step 2: Get Users API
  group('2. Get Users API', function () {
    const res = http.get(`${BASE_URL}/get`, authParams);
    check(res, {
      'Get Users status 200': (r) => r.status === 200
    });
  });

  sleep(1);

  // Step 3: Create User API
  group('3. Create User API', function () {
    const payload = generateRandomUser();
    const res = http.post(`${BASE_URL}/post`, JSON.stringify(payload), authParams);
    check(res, {
      'Create User status 200': (r) => r.status === 200
    });
  });

  sleep(1);

  // Step 4: Update User API
  group('4. Update User API', function () {
    const payload = { name: 'Updated Name', role: 'Senior Planner' };
    const res = http.put(`${BASE_URL}/put`, JSON.stringify(payload), authParams);
    check(res, {
      'Update User status 200': (r) => r.status === 200
    });
  });

  sleep(1);

  // Step 5: Delete User API
  group('5. Delete User API', function () {
    const res = http.del(`${BASE_URL}/delete`, null, authParams);
    check(res, {
      'Delete User status 200': (r) => r.status === 200
    });
  });

  sleep(1);
}
