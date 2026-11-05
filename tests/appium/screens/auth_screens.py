from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class SplashScreen(BaseScreen):
    APP_TITLE = (AppiumBy.XPATH, "//*[@text='Smart Travel Planner']")
    SUBTITLE = (AppiumBy.XPATH, "//*[contains(@text, 'Intelligent Travel')]")

    def wait_for_transition_to_login(self, timeout=6):
        return self.is_visible((AppiumBy.XPATH, "//*[@text='Welcome Back!' or @text='Login']"), timeout=timeout)

class LoginScreen(BaseScreen):
    HEADER_TITLE = (AppiumBy.XPATH, "//*[@text='Welcome Back!']")
    EMAIL_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[1]")
    PASSWORD_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[2]")
    LOGIN_BUTTON = (AppiumBy.XPATH, "//*[@text='Login' or @text='Log In']")
    SIGNUP_LINK = (AppiumBy.XPATH, "//*[@text='Sign Up']")
    ERROR_SNACKBAR = (AppiumBy.XPATH, "//*[contains(@text, 'Invalid') or contains(@text, 'fill in')]")

    def login(self, email, password):
        if email:
            self.type_text(self.EMAIL_INPUT, email)
        if password:
            self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def navigate_to_signup(self):
        self.click(self.SIGNUP_LINK)

class SignupScreen(BaseScreen):
    HEADER_TITLE = (AppiumBy.XPATH, "//*[@text='Create Account']")
    NAME_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[1]")
    EMAIL_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[2]")
    PHONE_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[3]")
    PASSWORD_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[4]")
    SIGNUP_BUTTON = (AppiumBy.XPATH, "//*[@text='Sign Up']")
    LOGIN_LINK = (AppiumBy.XPATH, "//*[@text='Log In']")

    def signup(self, name, email, phone, password):
        if name:
            self.type_text(self.NAME_INPUT, name)
        if email:
            self.type_text(self.EMAIL_INPUT, email)
        if phone:
            self.type_text(self.PHONE_INPUT, phone)
        if password:
            self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.SIGNUP_BUTTON)
