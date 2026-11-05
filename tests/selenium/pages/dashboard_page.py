from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    WELCOME_HEADING = (By.XPATH, "//h1[contains(., 'Hello,') or contains(., 'Welcome')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder*='search' i]")
    DESTINATION_CARDS = (By.CSS_SELECTOR, "div[style*='border-radius: 12px']")
    ACTIVE_TRIP_CARD = (By.XPATH, "//div[contains(., 'Itinerary') or contains(., 'Trip')]")
    COST_OPTIMIZED_BADGE = (By.XPATH, "//*[contains(text(), 'Optimized')]")
    PLAN_TRIP_BTN = (By.XPATH, "//button[contains(., 'Trip Planner')]")
    BOOKINGS_TAB = (By.XPATH, "//button[contains(., 'Bookings')]")
    EXPENSES_TAB = (By.XPATH, "//button[contains(., 'Expense Tracker')]")
    PROFILE_TAB = (By.XPATH, "//button[contains(., 'User Profile')]")
    SETTINGS_TAB = (By.XPATH, "//button[contains(., 'Settings')]")
    HISTORY_TAB = (By.XPATH, "//button[contains(., 'Travel History')]")
    LEAFLET_MAP = (By.CSS_SELECTOR, ".leaflet-container, div[id*='map']")

    def search_destination(self, query):
        self.type_text(self.SEARCH_INPUT, query)

    def get_destination_cards_count(self):
        return len(self.find_all(self.DESTINATION_CARDS, timeout=4))

    def is_leaflet_map_present(self):
        return self.is_visible(self.LEAFLET_MAP, timeout=4)
