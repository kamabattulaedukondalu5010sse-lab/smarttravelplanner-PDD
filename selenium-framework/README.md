# Selenium WebDriver React Web E2E Automation Framework

An enterprise-grade, production-ready E2E Automation Framework for React Web Applications built with **Selenium WebDriver**, **Node.js**, **Mocha**, **Chai**, **Winston Logger**, **ExcelJS**, and **Mochawesome**.

---

## 🚀 Key Features
- **Multi-Browser & Cross-Browser Execution**: Full support for Google Chrome, Microsoft Edge, and Mozilla Firefox in both Headed and Headless modes.
- **Dynamic Route Scanner & Dynamic Test Case Generator**:
  - Automatically scans React Router source files (`frontend/src`).
  - Discovers routes and form components automatically.
  - Generates and executes test cases dynamically from validation rules (required fields, email/phone format, min/max length) without hardcoding tests!
- **Page Object Model (POM)**: Decoupled UI page classes (`LoginPage`, `DynamicFormPage`) and reusable wait/JS utilities.
- **Dual Reporting**:
  - `E2E_Report.xlsx`: 4-sheet Excel report (Summary, Test Cases, Failed Tests, Execution Logs).
  - `reports/index.html`: Mochawesome HTML report with pass/fail charts and failure breakdowns.
- **Automatic Failure Handling**: Captures full screenshots, browser console logs, current URL, and stack traces stored under `reports/failures/`.
- **CI/CD Integration**: Pre-configured `.github/workflows/selenium-e2e.yml` workflow.

---

## 📁 Directory Structure
```
selenium-framework/
├── config/                     # Browser options & driver factory (Chrome, Edge, Firefox)
├── pages/                      # Page Objects (BasePage, LoginPage, DynamicFormPage)
├── utilities/                  # WaitUtils, JSUtils, ScreenshotUtils, ExcelReporter, Logger
│   ├── routeScanner.js         # React AST/Regex route scanner
│   └── dynamicTestGenerator.js # Dynamic test generator module
├── tests/                      # E2E test suites (e2e.test.js, dynamicRoutes.test.js)
├── reports/                    # Generated Excel reports, HTML reports, and failure screenshots
├── logs/                       # Winston execution & error logs
├── .mocharc.json
├── package.json
└── README.md
```

---

## 🛠 Setup & Execution Instructions

### Prerequisites
1. **Node.js** (v18+)
2. **Web Browsers**: Chrome, Edge, or Firefox installed locally.

### Installation
```bash
cd selenium-framework
npm install
```

### Running Tests
```bash
# Run all Selenium tests in default headless Chrome
npm test

# Run dynamic React route scanner test suite
npm run test:dynamic

# Run in headed mode or specific browser
BROWSER=firefox HEADLESS=false npm test
BROWSER=edge HEADLESS=true npm test
```
