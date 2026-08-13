import http from 'k6/http';
import { check } from 'k6';

export function generateRandomUser() {
  const rand = Math.floor(Math.random() * 1000000);
  return {
    name: `LoadTestUser_${rand}`,
    email: `loaduser_${rand}@example.com`,
    password: 'Password123!'
  };
}

export function generateRandomTripDates() {
  const futureDay = Math.floor(Math.random() * 20) + 1;
  const startMonth = Math.floor(Math.random() * 3) + 6; // June - August
  const startStr = `2026-0${startMonth}-${futureDay < 10 ? '0' + futureDay : futureDay}`;
  const endDay = futureDay + 4;
  const endStr = `2026-0${startMonth}-${endDay < 10 ? '0' + endDay : endDay}`;

  return {
    startDate: startStr,
    endDate: endStr
  };
}

export function logIfError(res) {
  if (res.status < 200 || res.status >= 300) {
    const bodySnippet = res.body ? String(res.body).substring(0, 250) : 'empty body';
    console.log(`[CI DIAGNOSTIC] HTTP ${res.status} on ${res.request.method} ${res.url} - Response: ${bodySnippet}`);
  }
}
