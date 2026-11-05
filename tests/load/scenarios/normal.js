import http from 'k6/http';
import { check, sleep } from 'k6';
import { getAuthToken, getAuthHeaders } from '../helpers/auth.js';

const DESTINATIONS = ['Goa', 'Manali', 'Kerala', 'Dubai', 'Jaipur', 'Shimla', 'Leh Ladakh'];

export function runNormalScenario(baseUrl) {
  const token = getAuthToken(baseUrl);
  const authHeaders = getAuthHeaders(token);

  // Random destination search
  const dest = DESTINATIONS[Math.floor(Math.random() * DESTINATIONS.length)];
  const resSearch = http.get(`${baseUrl}/api/destinations?search=${dest}`);
  check(resSearch, {
    'LOAD-042: Search destination status 200': (r) => r.status === 200
  });

  // Fetch user profile
  const resProfile = http.get(`${baseUrl}/api/auth/user`, authHeaders);
  check(resProfile, {
    'LOAD-049: Profile status 200': (r) => r.status === 200
  });

  // Fetch trips
  const resTrips = http.get(`${baseUrl}/api/trips`, authHeaders);
  check(resTrips, {
    'LOAD-050: Trips status 200': (r) => r.status === 200
  });

  // Fetch bookings
  const resBookings = http.get(`${baseUrl}/api/bookings`, authHeaders);
  check(resBookings, {
    'LOAD-052: Bookings status 200': (r) => r.status === 200
  });

  sleep(1);
}
