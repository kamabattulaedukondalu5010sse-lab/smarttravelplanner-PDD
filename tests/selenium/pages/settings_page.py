from selenium.webdriver.common.by import By
from .base_page import BasePage

class SettingsPage(BasePage):
    HEADER = (By.XPATH, "//h2[contains(., 'Settings') or contains(., 'Preferences')]")
    CURRENCY_SELECT = (By.CSS_SELECTOR, "select")
    SAVE_PREFERENCES_BUTTON = (By.XPATH, "//button[contains(., 'Save')]")
    THEME_TOGGLE = (By.XPATH, "//*[contains(text(), 'Theme') or contains(text(), 'Mode')]")
    EXPORT_DATA_BUTTON = (By.XPATH, "//button[contains(., 'Export')]")

class HistoryPage(BasePage):
    HEADER = (By.XPATH, "//h2[contains(., 'History') or contains(., 'Archive')]")
    COMPLETED_TRIP_CARDS = (By.CSS_SELECTOR, "div[style*='border-radius: 12px']")
    STATUS_BADGE = (By.XPATH, "//*[contains(text(), 'Completed')]")
