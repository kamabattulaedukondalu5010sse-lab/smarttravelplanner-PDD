# Appium Mobile Android E2E Testing Guide - Smart Travel Planner

## 1. Overview
The Appium testing suite provides **300 automated mobile UI test cases** (`APP-001` through `APP-300`) covering the Flutter Android application for Smart Travel Planner.

## 2. Technology Stack
- **Language**: Python 3.10+
- **Test Framework**: pytest, pytest-html
- **Mobile Driver**: Appium Python Client (Appium 2.x + UiAutomator2)
- **Target OS**: Android (API level 30, x86_64 emulator)
- **Design Pattern**: Screen Object Model (SOM)
- **App Package**: `com.smarttravelplanner.mobile`
- **Main Activity**: `com.smarttravelplanner.mobile.MainActivity`
- **Binary**: `mobile/build/app/outputs/flutter-apk/app-debug.apk`

## 3. Test Coverage Matrix (300 Test Cases)
- `APP-001` to `APP-030`: App Launch & Splash Screen Animation
- `APP-031` to `APP-065`: Mobile Authentication & Sign In
- `APP-066` to `APP-095`: Mobile User Registration & Form Validation
- `APP-096` to `APP-130`: Home Dashboard & Bottom Navigation
- `APP-131` to `APP-160`: Destination Discovery & Search
- `APP-161` to `APP-195`: Trip Planner & Itinerary Viewer
- `APP-196` to `APP-225`: Budget Calculation & Expense Tracking
- `APP-226` to `APP-255`: User Profile & Settings Management
- `APP-256` to `APP-280`: Gestures, Scrolling & UI Orientations
- `APP-281` to `APP-300`: Lifecycle, Background/Foreground & Network Resilience

## 4. Environment Variables
| Variable | Description | Default |
|---|---|---|
| `APPIUM_SERVER_URL` | Appium 2.x server endpoint | `http://127.0.0.1:4723` |
| `APP_PACKAGE` | Android Application ID | `com.smarttravelplanner.mobile` |
| `APP_ACTIVITY` | Main Android Activity | `com.smarttravelplanner.mobile.MainActivity` |
| `APK_PATH` | Path to compiled Flutter APK | `mobile/build/app/outputs/flutter-apk/app-debug.apk` |
| `ANDROID_DEVICE_NAME`| Target emulator device ID | `emulator-5554` |

## 5. Local Execution

```bash
# 1. Install dependencies
pip install -r tests/appium/requirements.txt
npm install -g appium
appium driver install uiautomator2

# 2. Build Flutter APK
cd mobile && flutter build apk --debug

# 3. Start Appium Server
appium --log tests/appium/logs/appium-server.log &

# 4. Launch Emulator & Run Tests
pytest tests/appium -v --html=tests/appium/reports/report.html --junitxml=tests/appium/reports/junit.xml
```

## 6. GitHub Actions Execution
Executed independently by `.github/workflows/appium-tests.yml`:
- Uses Java 17, Android SDK, and Flutter SDK.
- Compiles Flutter Android debug APK.
- Launches lightweight headless Android emulator with hardware acceleration (`/dev/kvm`).
- Starts Appium 2 server with `uiautomator2` driver.
- Runs tests and uploads `appium-test-results` artifact with logs and screenshots.
