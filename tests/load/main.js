import { runSmokeScenario } from './scenarios/smoke.js';
import { runNormalScenario } from './scenarios/normal.js';
import { runStressScenario, runSpikeScenario, runSoakScenario } from './scenarios/stress_spike_soak.js';
import { generateHtmlReport } from './helpers/html_reporter.js';

const PROFILE = __ENV.PROFILE || 'smoke';
const BASE_URL = (__ENV.BASE_URL || 'http://127.0.0.1:5000').replace(/\/$/, '');
const USER_VUS = parseInt(__ENV.VUS || '2');
const USER_DURATION = __ENV.DURATION || '20s';

function getOptionsForProfile(profile) {
  const thresholds = {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  };

  switch (profile.toLowerCase()) {
    case 'normal':
      return {
        stages: [
          { duration: '10s', target: USER_VUS || 10 },
          { duration: USER_DURATION, target: USER_VUS || 10 },
          { duration: '5s', target: 0 }
        ],
        thresholds
      };
    case 'stress':
      return {
        stages: [
          { duration: '15s', target: 30 },
          { duration: USER_DURATION, target: 30 },
          { duration: '10s', target: 0 }
        ],
        thresholds
      };
    case 'spike':
      return {
        stages: [
          { duration: '5s', target: 35 },
          { duration: '10s', target: 35 },
          { duration: '5s', target: 2 }
        ],
        thresholds
      };
    case 'soak':
      return {
        vus: 5,
        duration: USER_DURATION,
        thresholds
      };
    case 'smoke':
    default:
      return {
        vus: USER_VUS,
        duration: USER_DURATION,
        thresholds
      };
  }
}

export const options = getOptionsForProfile(PROFILE);

export default function () {
  switch (PROFILE.toLowerCase()) {
    case 'normal':
      runNormalScenario(BASE_URL);
      break;
    case 'stress':
      runStressScenario(BASE_URL);
      break;
    case 'spike':
      runSpikeScenario(BASE_URL);
      break;
    case 'soak':
      runSoakScenario(BASE_URL);
      break;
    case 'smoke':
    default:
      runSmokeScenario(BASE_URL);
      break;
  }
}

export function handleSummary(data) {
  const htmlContent = generateHtmlReport(data, PROFILE);
  return {
    'tests/load/reports/summary.json': JSON.stringify(data, null, 2),
    'tests/load/reports/summary.html': htmlContent,
    stdout: `\n=== Smart Travel Planner k6 Load Test Summary ===\nProfile: ${PROFILE}\nTotal Requests: ${data.metrics.http_reqs ? data.metrics.http_reqs.values.count : 0}\np(95) Duration: ${data.metrics.http_req_duration ? data.metrics.http_req_duration.values['p(95)'].toFixed(2) : 0}ms\nFailure Rate: ${data.metrics.http_req_failed ? (data.metrics.http_req_failed.values.rate * 100).toFixed(2) : 0}%\n=================================================\n`
  };
}
