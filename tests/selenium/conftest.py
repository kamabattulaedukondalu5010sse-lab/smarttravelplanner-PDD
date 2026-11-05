import os
import sys
import pytest
from datetime import datetime

# Add project root and selenium dir to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

SCREENSHOTS_DIR = os.path.join(BASE_DIR, "reports", "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://127.0.0.1:3000").rstrip("/")

@pytest.fixture(scope="session")
def test_username():
    return os.getenv("TEST_USERNAME", "john@example.com")

@pytest.fixture(scope="session")
def test_password():
    return os.getenv("TEST_PASSWORD", "123456")

@pytest.fixture(scope="function")
def driver(request):
    """
    Creates and configures headless Chrome WebDriver.
    Falls back gracefully or logs error if Chrome binary is not available.
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service

    chrome_options = Options()
    is_headless = os.getenv("HEADLESS", "true").lower() == "true"
    if is_headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-extensions")

    # In CI runners or Linux, specify chromium-browser if needed
    chrome_bin = os.getenv("CHROME_BIN")
    if chrome_bin and os.path.exists(chrome_bin):
        chrome_options.binary_location = chrome_bin

    try:
        driver_instance = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        # Try using webdriver-manager if standard path fails
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            service = Service(ChromeDriverManager().install())
            driver_instance = webdriver.Chrome(service=service, options=chrome_options)
        except Exception:
            raise RuntimeError(f"Unable to initialize Chrome WebDriver: {e}")

    driver_instance.implicitly_wait(5)
    yield driver_instance

    try:
        driver_instance.quit()
    except Exception:
        pass

@pytest.fixture(scope="function")
def authenticated_driver(driver, base_url, test_username, test_password):
    """
    Logs in and yields authenticated driver at dashboard view.
    """
    from pages.login_page import LoginPage
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    login_page.wait_for_dashboard()
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver") or item.funcargs.get("authenticated_driver")
        if driver_instance:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("/", "_").replace(":", "_")
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)
            try:
                driver_instance.save_screenshot(filepath)
                # Attach to pytest-html if available
                extra = getattr(report, "extra", [])
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    extra.append(pytest_html.extras.image(filepath))
                    report.extra = extra
            except Exception:
                pass
