# Grafana k6 API Load Testing Suite

An enterprise performance testing suite built with **Grafana k6** for benchmarking API throughput, latency, error rates, and response time percentiles under heavy concurrent virtual user load.

---

## 📁 Directory Structure
```
load-tests/
├── config.js       # Thresholds, VU stages, environment variables
├── helpers.js      # Random data generation & token helper
├── login.js        # Authentication API load test scenario
├── users.js        # User CRUD API load test scenario
├── main.js         # Unified multi-API workflow scenario (Login -> Get -> Create -> Update -> Delete)
└── README.md
```

---

## 🚀 Quick Start Instructions

### Run Baseline Load Test (100 VUs)
```bash
k6 run main.js
```

### Run with Environment Variables
```bash
k6 run -e BASE_URL=https://staging.api.example.com -e USERNAME=admin@example.com -e PASSWORD=SecretPass main.js
```

### Export Results to HTML Report
```bash
k6 run --out json=summary.json main.js
```
