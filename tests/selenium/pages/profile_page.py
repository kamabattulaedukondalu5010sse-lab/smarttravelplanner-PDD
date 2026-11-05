from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    HEADER = (By.XPATH, "//h2[contains(., 'Profile')]")
    NAME_FIELD = (By.CSS_SELECTOR, "input[name='name'], input[placeholder*='name' i]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email'], input[placeholder*='email' i]")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name='phone'], input[placeholder*='phone' i]")
    EDIT_BUTTON = (By.XPATH, "//button[contains(., 'Edit')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(., 'Save')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(., 'Cancel')]")
    AVATAR_IMAGE = (By.CSS_SELECTOR, "img[alt*='avatar' i], img[style*='border-radius: 50%']")

    def update_profile(self, name=None, phone=None):
        if self.is_visible(self.EDIT_BUTTON, timeout=3):
            self.click(self.EDIT_BUTTON)
        if name and self.is_visible(self.NAME_FIELD, timeout=2):
            self.type_text(self.NAME_FIELD, name)
        if phone and self.is_visible(self.PHONE_FIELD, timeout=2):
            self.type_text(self.PHONE_FIELD, phone)
        if self.is_visible(self.SAVE_BUTTON, timeout=2):
            self.click(self.SAVE_BUTTON)
