import os
import sys
import pytest
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

SCREENSHOTS_DIR = os.path.join(BASE_DIR, "reports", "screenshots")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

@pytest.fixture(scope="session")
def app_package():
    return os.getenv("APP_PACKAGE", "com.smarttravelplanner.mobile")

@pytest.fixture(scope="session")
def app_activity():
    return os.getenv("APP_ACTIVITY", "com.smarttravelplanner.mobile.MainActivity")

@pytest.fixture(scope="session")
def apk_path():
    default_apk = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "mobile", "build", "app", "outputs", "flutter-apk", "app-debug.apk"))
    return os.getenv("APK_PATH", default_apk)

@pytest.fixture(scope="session")
def driver(app_package, app_activity, apk_path):
    """
    Initializes Appium 2.x UiAutomator2 driver session for Flutter Android app.
    """
    from appium import webdriver
    from appium.options.android import UiAutomator2Options

    server_url = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
    options.app_package = app_package
    options.app_activity = app_activity
    options.no_reset = True
    options.auto_grant_permissions = True
    options.new_command_timeout = 180

    if os.path.exists(apk_path):
        options.app = apk_path

    try:
        driver_instance = webdriver.Remote(server_url, options=options)
    except Exception as e:
        pytest.skip(f"Appium server or Android emulator not available: {e}")
        return

    driver_instance.implicitly_wait(4)
    yield driver_instance

    try:
        driver_instance.quit()
    except Exception:
        pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("/", "_").replace(":", "_")
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)
            try:
                driver_instance.save_screenshot(filepath)
                extra = getattr(report, "extra", [])
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    extra.append(pytest_html.extras.image(filepath))
                    report.extra = extra
            except Exception:
                pass
