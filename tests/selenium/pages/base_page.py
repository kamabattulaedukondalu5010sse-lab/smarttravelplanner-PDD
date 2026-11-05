import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, base_url="http://127.0.0.1:3000"):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.timeout = 10

    def open(self, path=""):
        url = f"{self.base_url}/{path}".rstrip("/") if path else self.base_url
        self.driver.get(url)

    def find(self, locator, timeout=None):
        t = timeout or self.timeout
        return WebDriverWait(self.driver, t).until(
            EC.presence_of_element_located(locator)
        )

    def find_all(self, locator, timeout=None):
        t = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, t).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []

    def click(self, locator, timeout=None):
        t = timeout or self.timeout
        element = WebDriverWait(self.driver, t).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_text(self, locator, text, clear_first=True, timeout=None):
        element = self.find(locator, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=None):
        element = self.find(locator, timeout)
        return element.text.strip()

    def is_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_url_contains(self, fragment, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(fragment)
            )
            return True
        except TimeoutException:
            return False

    def switch_tab(self, tab_name):
        """Switches tabs via sidebar buttons in dashboard layout"""
        btn_locator = (By.XPATH, f"//button[contains(., '{tab_name}')]")
        self.click(btn_locator)
        time.sleep(0.5)

    def capture_screenshot(self, name):
        timestamp = int(time.time())
        path = os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots", f"{name}_{timestamp}.png")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.driver.save_screenshot(path)
        return path
