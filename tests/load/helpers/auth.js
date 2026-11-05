import http from 'k6/http';
import { check } from 'k6';

export function getAuthToken(baseUrl, email = 'john@example.com', password = 'anypassword') {
  const url = `${baseUrl}/api/auth/login`;
  const payload = JSON.stringify({ email, password });
  const params = {
    headers: { 'Content-Type': 'application/json' },
    timeout: '10s'
  };

  const res = http.post(url, payload, params);
  const success = check(res, {
    'login status is 200': (r) => r.status === 200,
    'login returns token': (r) => r.json('token') !== undefined && r.json('token') !== null
  });

  if (success && res.json('token')) {
    return res.json('token');
  }

  // Fallback simulated token for offline testing
  return 'mock_k6_jwt_token_12345';
}

export function getAuthHeaders(token) {
  return {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  };
}
