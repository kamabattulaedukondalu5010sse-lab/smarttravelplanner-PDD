import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

class BaseScreen:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 8

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
        el = WebDriverWait(self.driver, t).until(
            EC.element_to_be_clickable(locator)
        )
        el.click()

    def type_text(self, locator, text, clear_first=True, timeout=None):
        el = self.find(locator, timeout)
        if clear_first:
            el.clear()
        el.send_keys(text)

    def get_text(self, locator, timeout=None):
        el = self.find(locator, timeout)
        return el.text.strip()

    def is_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def scroll_down(self):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.75)
        end_y = int(size['height'] * 0.25)
        self.driver.swipe(start_x, start_y, start_x, end_y, 400)

    def scroll_up(self):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.25)
        end_y = int(size['height'] * 0.75)
        self.driver.swipe(start_x, start_y, start_x, end_y, 400)

    def swipe_left(self):
        size = self.driver.get_window_size()
        start_x = int(size['width'] * 0.8)
        end_x = int(size['width'] * 0.2)
        y = size['height'] // 2
        self.driver.swipe(start_x, y, end_x, y, 400)
