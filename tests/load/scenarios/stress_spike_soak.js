import http from 'k6/http';
import { check, sleep } from 'k6';
import { getAuthToken, getAuthHeaders } from '../helpers/auth.js';

export function runStressScenario(baseUrl) {
  const token = getAuthToken(baseUrl);
  const authHeaders = getAuthHeaders(token);

  // Heavy parallel read & writes
  const resDest = http.get(`${baseUrl}/api/destinations`);
  check(resDest, {
    'LOAD-086: Stress destinations status 200': (r) => r.status === 200
  });

  const resTrips = http.get(`${baseUrl}/api/trips`, authHeaders);
  check(resTrips, {
    'LOAD-087: Stress trips status 200': (r) => r.status === 200
  });

  sleep(0.5);
}

export function runSpikeScenario(baseUrl) {
  // Sudden burst of destination requests
  const res = http.get(`${baseUrl}/api/destinations`);
  check(res, {
    'LOAD-131: Spike destination surge status 200': (r) => r.status === 200
  });
  sleep(0.2);
}

export function runSoakScenario(baseUrl) {
  const token = getAuthToken(baseUrl);
  const authHeaders = getAuthHeaders(token);

  const res = http.get(`${baseUrl}/api/destinations?search=Goa`);
  check(res, {
    'LOAD-171: Soak search status 200': (r) => r.status === 200
  });

  const resTrips = http.get(`${baseUrl}/api/trips`, authHeaders);
  check(resTrips, {
    'LOAD-172: Soak trips status 200': (r) => r.status === 200
  });

  sleep(2);
}
