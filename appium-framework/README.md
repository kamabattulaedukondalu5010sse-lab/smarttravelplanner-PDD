# React Native Android Appium 2.x E2E Automation Framework

An enterprise-grade, production-ready Mobile Automation Framework built with **Appium 2.x**, **JavaScript (Node.js)**, **Mocha**, **Chai**, **Winston Logger**, **ExcelJS**, and **Mochawesome**.

---

## 🚀 Features
- **Appium 2.x Driver**: Built on `UiAutomator2` with native support for React Native widgets (located via `ValueKey`, `Semantics Label`, `Accessibility ID`, `Widget Text`).
- **Auto APK Installation**: Configured with `APK_PATH`, `APP_PACKAGE`, and `APP_ACTIVITY`.
- **Smart AI Testing Engine**: Dynamic screen widget discovery, automated test scenario generation, and navigation path exploration.
- **Page Object Model (POM)**: Clean abstraction of UI pages and reusable gesture interactions.
- **Gesture Support**: W3C Actions for Tap, Double Tap, Long Press, Scroll, Swipe, Drag & Drop, Pinch, and Zoom.
- **Dual Reporting System**:
  - `React_Native_E2E_Report.xlsx`: 4-sheet Excel report (Summary, Test Cases, Failed Tests, Execution Logs).
  - `reports/html/index.html`: Mochawesome HTML report with pass/fail charts and device details.
- **Failure Analysis**: Automatic screenshots, Logcat logs, and stack traces stored under `reports/failures/`.
- **CI/CD Integration**: Ready-to-use `.github/workflows/react-native-appium.yml` workflow.

---

## 📁 Directory Structure
```
appium-framework/
├── app/                        # Target APK binaries (app-release.apk)
├── config/                     # Driver capabilities & server configuration
├── pages/                      # Page Object classes (BasePage, LoginPage, FormPage)
├── utilities/                  # GestureUtils, ExcelReporter, Logger, SmartAITester
├── tests/                      # Mocha test suites (auth, forms, ai)
├── reports/                    # Generated Excel reports, HTML reports, and failure screenshots
├── logs/                       # Winston execution and failure log files
├── .mocharc.json               # Mocha configuration
├── package.json
└── README.md
```

---

## 🛠 Setup & Execution Instructions

### Prerequisites
1. **Node.js** (v18+)
2. **Java Development Kit (JDK 17+)**
3. **Android SDK & Android Emulator / Real Device**
4. **Appium 2.x Server**:
   ```bash
   npm install -g appium
   appium driver install uiautomator2
   ```

### Installation
```bash
cd appium-framework
npm install
```

### Running Tests
```bash
# Run all test suites
npm test

# Run authentication suite only
npm run test:auth

# Run form validation suite only
npm run test:forms

# Run Smart AI testing module only
npm run test:ai
```

---

## 📊 Environment Configuration
Set environment variables or update `config/driver.config.js`:
- `APK_PATH`: `./app/app-release.apk`
- `APP_PACKAGE`: `com.company.app`
- `APP_ACTIVITY`: `com.company.app.MainActivity`
- `DEVICE_NAME`: `Android Emulator`
- `PLATFORM_VERSION`: `13.0`
