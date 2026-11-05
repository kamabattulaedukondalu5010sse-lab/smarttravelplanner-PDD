# Grafana k6 Load Testing Guide - Smart Travel Planner

## 1. Overview
The load testing framework implements **300 performance scenarios** (`LOAD-001` through `LOAD-300`) using Grafana k6 to validate backend scalability, endpoint throughput, latency distribution, and resilience under concurrency.

## 2. Profile Organization
- **Smoke Profile** (`LOAD-001` to `LOAD-040`): Default CI verification. 1-2 VUs for 20-30s. Baseline health and critical endpoint response verification.
- **Normal Load Profile** (`LOAD-041` to `LOAD-085`): Sustained typical production traffic (10-20 VUs).
- **Stress Profile** (`LOAD-086 to LOAD-130`): Traffic ramp-up (30-100 VUs) to discover saturation boundary.
- **Spike Profile** (`LOAD-131 to LOAD-170`): Sudden shock bursts (surge to 40 VUs in 5s).
- **Soak Profile** (`LOAD-171 to LOAD-205`): Extended endurance testing for memory leaks and resource exhaustion.
- **API Benchmarks** (`LOAD-206 to LOAD-240`): TTFB and throughput micro-benchmarks per endpoint.
- **Authentication Under Load** (`LOAD-241 to LOAD-265`): Concurrent JWT issuing and verification.
- **Database Operations** (`LOAD-266 to LOAD-285`): Concurrent read/write aggregation load.
- **High-Volume Payload** (`LOAD-286 to LOAD-300`): Large JSON payload deserialization.

## 3. Configurable Thresholds
- `http_req_failed`: `rate < 0.01` (failure rate strictly under 1%)
- `http_req_duration`: `p(95) < 500ms` (95% of requests complete in < 500ms)

## 4. Local Execution

```bash
# 1. Run Smoke Profile (Default)
k6 run tests/load/main.js

# 2. Run Normal Load Profile
PROFILE=normal VUS=10 DURATION=30s k6 run tests/load/main.js

# 3. Run Stress Profile
PROFILE=stress DURATION=1m k6 run tests/load/main.js

# 4. View Generated Reports
open tests/load/reports/summary.html
```

## 5. GitHub Actions Execution
Executed independently by `.github/workflows/load-tests.yml`:
- Starts backend API with MongoDB service.
- Installs k6 via official GitHub releases action (`grafana/k6-action@v0.4.0`).
- Runs default CI smoke profile (`PROFILE: smoke`, `DURATION: 20s`).
- Supports workflow dispatch inputs for `profile`, `duration`, `virtual_users`, `environment`.
- Generates JSON and HTML performance summaries and publishes to GITHUB_STEP_SUMMARY.
- Uploads `k6-test-results` artifact.
