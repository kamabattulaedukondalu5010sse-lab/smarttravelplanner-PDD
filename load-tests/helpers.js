import http from 'k6/http';
import { check } from 'k6';

export function generateRandomUser() {
  const rand = Math.floor(Math.random() * 100000);
  return {
    name: `TestUser_${rand}`,
    email: `user_${rand}@example.com`,
    role: 'Planner'
  };
}

export function getAuthToken(baseUrl, username, password) {
  const payload = JSON.stringify({ username, password });
  const headers = { 'Content-Type': 'application/json' };
  const res = http.post(`${baseUrl}/post`, payload, { headers });
  
  check(res, {
    'Auth status is 200': (r) => r.status === 200,
  });

  return 'bearer-token-12345';
}
