import http from 'k6/http';
import { check, sleep } from 'k6';
import { BASE_URL, USERNAME, PASSWORD } from './config.js';
import { generateRandomTripDates, logIfError } from './helpers.js';

export const options = {
  vus: 10,
  duration: '15s',
  thresholds: {
    http_req_duration: ['p(95)<2500'],
    http_req_failed: ['rate<0.05']
  }
};

export default function () {
  const jsonHeaders = { 'Content-Type': 'application/json' };
  
  // Obtain auth token via login or signup
  let loginRes = http.post(`${BASE_URL}/api/auth/login`, JSON.stringify({
    email: USERNAME,
    password: PASSWORD
  }), { headers: jsonHeaders });

  let token = '';
  try {
    token = loginRes.json('token') || '';
  } catch (e) {
    token = '';
  }

  if (!token) {
    const signupRes = http.post(`${BASE_URL}/api/auth/signup`, JSON.stringify({
      name: 'Load Test User',
      email: USERNAME,
      password: PASSWORD
    }), { headers: jsonHeaders });
    try {
      token = signupRes.json('token') || '';
    } catch (e) {
      token = '';
    }
  }

  const params = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  };

  // 1. GET User Trips
  let getRes = http.get(`${BASE_URL}/api/trips`, params);
  logIfError(getRes);
  check(getRes, {
    'Get trips returns 200': (r) => r.status === 200
  });

  sleep(1);

  // 2. POST Create Trip
  const dates = generateRandomTripDates();
  const tripPayload = JSON.stringify({
    destination: 'Manali',
    startDate: dates.startDate,
    endDate: dates.endDate,
    travelersCount: 2,
    budget: 30000
  });
  let postRes = http.post(`${BASE_URL}/api/trips`, tripPayload, params);
  logIfError(postRes);
  check(postRes, {
    'Create trip returns 201 or 200': (r) => r.status === 201 || r.status === 200
  });

  sleep(1);
}
