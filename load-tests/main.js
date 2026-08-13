import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { BASE_URL, USERNAME, PASSWORD } from './config.js';
import { generateRandomUser, generateRandomTripDates, logIfError } from './helpers.js';

export const options = {
  stages: [
    { duration: '10s', target: 10 },
    { duration: '20s', target: 20 },
    { duration: '10s', target: 0 }
  ],
  thresholds: {
    http_req_failed: ['rate<0.05'],    // Error rate threshold (< 5%)
    http_req_duration: ['p(95)<5000']  // Latency threshold (p95 < 5000ms)
  }
};

export default function () {
  let authToken = '';
  let createdTripId = '';

  // 1. Authentication (Signup unique user per iteration or Login)
  group('1. Authentication API', function () {
    const jsonHeaders = { 'Content-Type': 'application/json' };
    const userCredentials = generateRandomUser();
    const signupPayload = JSON.stringify({
      name: userCredentials.name,
      email: userCredentials.email,
      password: userCredentials.password
    });
    
    let res = http.post(`${BASE_URL}/api/auth/signup`, signupPayload, { headers: jsonHeaders });
    
    if (res.status === 400 || res.status === 404 || res.status === 0) {
      const loginPayload = JSON.stringify({ email: USERNAME, password: PASSWORD });
      res = http.post(`${BASE_URL}/api/auth/login`, loginPayload, { headers: jsonHeaders });
    }

    logIfError(res);

    check(res, {
      'Auth status 200': (r) => (r.status === 200 || r.status === 201)
    });

    try {
      authToken = res.json('token') || '';
    } catch (e) {
      authToken = '';
    }
  });

  const authHeaders = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${authToken}`
    }
  };

  sleep(1);

  // 2. Profile Management & Update User
  group('2. Profile Management & Update User', function () {
    let getRes = http.get(`${BASE_URL}/api/auth/user`, authHeaders);
    logIfError(getRes);
    check(getRes, {
      'Get profile returns 200': (r) => r.status === 200
    });

    const updatePayload = JSON.stringify({
      name: 'Load Test User Updated',
      phone: '9876543210'
    });
    let updateRes = http.put(`${BASE_URL}/api/auth/user`, updatePayload, authHeaders);
    logIfError(updateRes);
    check(updateRes, {
      'Update User status 200': (r) => r.status === 200
    });
  });

  sleep(1);

  // 3. User Trips List
  group('3. Get User Trips', function () {
    let res = http.get(`${BASE_URL}/api/trips`, authHeaders);
    logIfError(res);
    check(res, {
      'Get trips returns 200': (r) => r.status === 200
    });
  });

  sleep(1);

  // 4. Create Trip
  group('4. Create Trip', function () {
    const dates = generateRandomTripDates();
    const tripPayload = JSON.stringify({
      destination: 'Goa',
      startDate: dates.startDate,
      endDate: dates.endDate,
      travelersCount: 2,
      budget: 25000
    });

    let res = http.post(`${BASE_URL}/api/trips`, tripPayload, authHeaders);
    logIfError(res);

    check(res, {
      'Create User status 200': (r) => r.status === 201 || r.status === 200,
      'Create trip returns 201 or 200': (r) => r.status === 201 || r.status === 200
    });

    if (res.status === 201 || res.status === 200) {
      try {
        createdTripId = res.json('trip._id') || res.json('trip.id') || res.json('_id') || '';
      } catch (e) {
        createdTripId = '';
      }
    }
  });

  sleep(1);

  // 5. Update Trip Status & Delete Trip Lifecycle
  group('5. Update & Delete Trip Lifecycle', function () {
    if (createdTripId) {
      const statusPayload = JSON.stringify({ status: 'completed' });
      let statusRes = http.put(`${BASE_URL}/api/trips/${createdTripId}/status`, statusPayload, authHeaders);
      logIfError(statusRes);
      check(statusRes, {
        'Update Trip status 200': (r) => r.status === 200
      });

      let delRes = http.del(`${BASE_URL}/api/trips/${createdTripId}`, null, authHeaders);
      logIfError(delRes);
      check(delRes, {
        'Delete User status 200': (r) => r.status === 200
      });
    }
  });

  sleep(1);

  // 6. Public Destinations API
  group('6. Public Destinations', function () {
    let res = http.get(`${BASE_URL}/api/destinations`);
    logIfError(res);
    check(res, {
      'Get public destinations returns 200': (r) => r.status === 200
    });
  });

  sleep(1);
}
