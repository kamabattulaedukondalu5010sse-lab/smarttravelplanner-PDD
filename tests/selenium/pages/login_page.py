from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators matching React frontend (App.jsx)
    HEADER_TITLE = (By.XPATH, "//h2[contains(text(), 'Welcome Back!') or contains(text(), 'Create Account')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SIGNUP_SWITCH_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign Up')]")
    LOGIN_SWITCH_BUTTON = (By.XPATH, "//button[contains(text(), 'Log In')]")
    ERROR_ALERT = (By.CSS_SELECTOR, "div[style*='FEE2E2']")
    DASHBOARD_CONTAINER = (By.XPATH, "//button[contains(., 'Dashboard')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Log Out')]")

    def login(self, email, password):
        if email is not None:
            self.type_text(self.EMAIL_INPUT, email)
        if password is not None:
            self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def switch_to_signup(self):
        self.click(self.SIGNUP_SWITCH_BUTTON)

    def switch_to_login(self):
        self.click(self.LOGIN_SWITCH_BUTTON)

    def get_error_message(self):
        if self.is_visible(self.ERROR_ALERT, timeout=3):
            return self.get_text(self.ERROR_ALERT)
        return ""

    def is_dashboard_visible(self):
        return self.is_visible(self.DASHBOARD_CONTAINER, timeout=5)

    def wait_for_dashboard(self):
        return self.find(self.DASHBOARD_CONTAINER, timeout=10)

    def logout(self):
        if self.is_visible(self.LOGOUT_BUTTON, timeout=3):
            self.click(self.LOGOUT_BUTTON)
