# Selenium Web E2E Testing Guide - Smart Travel Planner

## 1. Overview
The Selenium testing suite implements **300 automated web E2E test cases** (`SEL-001` through `SEL-300`) designed to validate the Smart Travel Planner React single-page application.

## 2. Technology Stack
- **Language**: Python 3.10+
- **Framework**: pytest, pytest-xdist, pytest-html
- **Browser Automation**: Selenium WebDriver (Headless Chrome)
- **Architecture**: Page Object Model (POM)
- **Synchronization**: Explicit Waits (`WebDriverWait`, `expected_conditions`)
- **Reporting**: JUnit XML (`junit.xml`), pytest-HTML report (`report.html`), screenshot captures on failure

## 3. Test Coverage Matrix (300 Test Cases)
- `SEL-001` to `SEL-035`: Authentication & Login
- `SEL-036` to `SEL-065`: Registration & Form Validation
- `SEL-066` to `SEL-095`: Dashboard Navigation & Metric Cards
- `SEL-096` to `SEL-135`: Trip Planner & Budget Optimizer
- `SEL-136` to `SEL-170`: Bookings Management & Modals
- `SEL-171` to `SEL-205`: Expense Tracker & Financial Categories
- `SEL-206` to `SEL-235`: User Profile & Personal Information
- `SEL-236` to `SEL-260`: Settings & Preferences
- `SEL-261` to `SEL-280`: Travel History & Status Lifecycle
- `SEL-281` to `SEL-300`: UI Responsiveness, Cross-Tab & Resilience

## 4. Environment Variables
| Variable | Description | Default |
|---|---|---|
| `BASE_URL` | Web frontend target URL | `http://127.0.0.1:3000` |
| `TEST_USERNAME` | Standard test user email | `john@example.com` |
| `TEST_PASSWORD` | Standard test user password | `123456` |
| `HEADLESS` | Run Chrome in headless mode | `true` |

## 5. Local Execution

```bash
# 1. Install dependencies
pip install -r tests/selenium/requirements.txt

# 2. Start Backend & Frontend
cd backend && npm start &
cd frontend && npm run dev -- --port 3000 &

# 3. Execute full suite with JUnit and HTML reports
pytest tests/selenium -v --html=tests/selenium/reports/report.html --junitxml=tests/selenium/reports/junit.xml

# 4. Execute with 4 parallel shards
pytest tests/selenium -n 4 -v
```

## 6. GitHub Actions Execution
Executed independently by `.github/workflows/selenium-tests.yml`:
- Starts MongoDB service container.
- Builds and starts Express API and Vite React frontend.
- Runs 4 parallel sharded jobs for ultra-fast execution.
- Captures failure screenshots, browser logs, JUnit XML, and HTML report.
- Uploads artifact `selenium-test-results`.

## 7. Troubleshooting
- **Chrome not found**: Ensure `google-chrome-stable` or `browser-actions/setup-chrome` is active.
- **Connection Refused**: Verify frontend server is listening on port 3000 and backend is responding on port 5000.
