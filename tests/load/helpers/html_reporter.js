export function generateHtmlReport(data, profile) {
  const metrics = data.metrics || {};
  const httpReqs = metrics.http_reqs ? metrics.http_reqs.values.count : 0;
  const httpRate = metrics.http_reqs ? metrics.http_reqs.values.rate.toFixed(2) : 0;
  const failRate = metrics.http_req_failed ? (metrics.http_req_failed.values.rate * 100).toFixed(2) : 0;
  const durationP95 = metrics.http_req_duration ? metrics.http_req_duration.values['p(95)'].toFixed(2) : 0;
  const durationMed = metrics.http_req_duration ? metrics.http_req_duration.values.med.toFixed(2) : 0;
  const durationAvg = metrics.http_req_duration ? metrics.http_req_duration.values.avg.toFixed(2) : 0;

  const isPassed = parseFloat(failRate) < 1.0 && parseFloat(durationP95) < 500.0;
  const statusColor = isPassed ? "#10B981" : "#EF4444";
  const statusText = isPassed ? "PASSED (GREEN)" : "FAILED (RED)";

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Smart Travel Planner - k6 Load Test Report</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 2rem; background: #0F172A; color: #F8FAFC; }
    .container { max-width: 1000px; margin: 0 auto; }
    .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 1.5rem; margin-bottom: 2rem; }
    .badge { padding: 0.5rem 1rem; border-radius: 9999px; font-weight: 700; background: ${statusColor}; color: #ffffff; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem; margin-bottom: 2rem; }
    .card { background: #1E293B; border: 1px solid #334155; border-radius: 12px; padding: 1.5rem; }
    .card-title { color: #94A3B8; font-size: 0.875rem; font-weight: 600; text-transform: uppercase; margin-bottom: 0.5rem; }
    .card-value { font-size: 2rem; font-weight: 800; color: #38BDF8; }
    table { width: 100%; border-collapse: collapse; background: #1E293B; border-radius: 12px; overflow: hidden; margin-top: 1rem; }
    th, td { padding: 1rem; text-align: left; border-bottom: 1px solid #334155; }
    th { background: #0F172A; color: #94A3B8; font-size: 0.875rem; text-transform: uppercase; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div>
        <h1 style="margin: 0; font-size: 1.75rem;">k6 Load Testing Report</h1>
        <p style="margin: 0.5rem 0 0 0; color: #94A3B8;">Smart Travel Planner - Profile: <strong>${profile}</strong></p>
      </div>
      <div class="badge">${statusText}</div>
    </div>

    <div class="grid">
      <div class="card">
        <div class="card-title">Total HTTP Requests</div>
        <div class="card-value">${httpReqs}</div>
      </div>
      <div class="card">
        <div class="card-title">Request Rate</div>
        <div class="card-value">${httpRate} /s</div>
      </div>
      <div class="card">
        <div class="card-title">p(95) Duration</div>
        <div class="card-value">${durationP95} ms</div>
      </div>
      <div class="card">
        <div class="card-title">Failure Rate</div>
        <div class="card-value" style="color: ${parseFloat(failRate) < 1.0 ? '#10B981' : '#EF4444'}">${failRate}%</div>
      </div>
    </div>

    <h2 style="font-size: 1.25rem; margin-top: 2rem;">Threshold Validation Results</h2>
    <table>
      <thead>
        <tr>
          <th>Metric</th>
          <th>Threshold</th>
          <th>Actual Value</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>http_req_failed</strong></td>
          <td>rate &lt; 0.01 (1.00%)</td>
          <td>${failRate}%</td>
          <td style="color: ${parseFloat(failRate) < 1.0 ? '#10B981' : '#EF4444'}; font-weight: 700;">${parseFloat(failRate) < 1.0 ? 'PASSED' : 'FAILED'}</td>
        </tr>
        <tr>
          <td><strong>http_req_duration</strong></td>
          <td>p(95) &lt; 500ms</td>
          <td>${durationP95} ms</td>
          <td style="color: ${parseFloat(durationP95) < 500.0 ? '#10B981' : '#EF4444'}; font-weight: 700;">${parseFloat(durationP95) < 500.0 ? 'PASSED' : 'FAILED'}</td>
        </tr>
        <tr>
          <td><strong>http_req_duration (avg)</strong></td>
          <td>N/A</td>
          <td>${durationAvg} ms</td>
          <td>INFORMATIONAL</td>
        </tr>
        <tr>
          <td><strong>http_req_duration (med)</strong></td>
          <td>N/A</td>
          <td>${durationMed} ms</td>
          <td>INFORMATIONAL</td>
        </tr>
      </tbody>
    </table>
  </div>
</body>
</html>`;
}
