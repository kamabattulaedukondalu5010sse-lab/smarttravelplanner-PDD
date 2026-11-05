from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignupPage(BasePage):
    HEADER_TITLE = (By.XPATH, "//h2[contains(text(), 'Create Account')]")
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder*='name' i]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_ALERT = (By.CSS_SELECTOR, "div[style*='FEE2E2']")
    LOGIN_LINK = (By.XPATH, "//button[contains(text(), 'Log In')]")

    def register(self, name, email, password):
        if name is not None:
            self.type_text(self.NAME_INPUT, name)
        if email is not None:
            self.type_text(self.EMAIL_INPUT, email)
        if password is not None:
            self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        if self.is_visible(self.ERROR_ALERT, timeout=3):
            return self.get_text(self.ERROR_ALERT)
        return ""
