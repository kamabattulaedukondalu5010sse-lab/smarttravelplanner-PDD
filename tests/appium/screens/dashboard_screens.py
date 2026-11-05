from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class DashboardScreen(BaseScreen):
    BOTTOM_NAV_HOME = (AppiumBy.XPATH, "//*[@text='Home']")
    BOTTOM_NAV_EXPLORE = (AppiumBy.XPATH, "//*[@text='Explore']")
    BOTTOM_NAV_TRIPS = (AppiumBy.XPATH, "//*[@text='Trips']")
    BOTTOM_NAV_ALERTS = (AppiumBy.XPATH, "//*[@text='Alerts']")
    BOTTOM_NAV_PROFILE = (AppiumBy.XPATH, "//*[@text='Profile']")

    PLAN_TRIP_ACTION = (AppiumBy.XPATH, "//*[@text='Plan Trip']")
    BUDGET_TOOL_ACTION = (AppiumBy.XPATH, "//*[@text='Budget Tool']")
    TOP_DESTINATIONS_ACTION = (AppiumBy.XPATH, "//*[@text='Top Destinations']")
    AI_SUGGESTIONS_ACTION = (AppiumBy.XPATH, "//*[@text='AI Suggestions']")
    ACTIVE_TRIP_CARD = (AppiumBy.XPATH, "//*[contains(@text, 'Goa') or contains(@text, 'Trip')]")

    def go_to_home(self):
        self.click(self.BOTTOM_NAV_HOME)

    def go_to_explore(self):
        self.click(self.BOTTOM_NAV_EXPLORE)

    def go_to_trips(self):
        self.click(self.BOTTOM_NAV_TRIPS)

    def go_to_alerts(self):
        self.click(self.BOTTOM_NAV_ALERTS)

    def go_to_profile(self):
        self.click(self.BOTTOM_NAV_PROFILE)

class SearchScreen(BaseScreen):
    SEARCH_INPUT = (AppiumBy.XPATH, "//android.widget.EditText")
    CHIP_ALL = (AppiumBy.XPATH, "//*[@text='All']")
    CHIP_BEACH = (AppiumBy.XPATH, "//*[@text='Beach']")
    CHIP_MOUNTAIN = (AppiumBy.XPATH, "//*[@text='Mountain']")
    DESTINATION_ITEM = (AppiumBy.XPATH, "//*[contains(@text, 'Goa') or contains(@text, 'Manali')]")

    def search(self, query):
        self.type_text(self.SEARCH_INPUT, query)

class PlannerScreen(BaseScreen):
    OPTIMIZE_BUTTON = (AppiumBy.XPATH, "//*[@text='Optimize Trip' or contains(@text, 'Optimize')]")
    BUDGET_INPUT = (AppiumBy.XPATH, "//android.widget.EditText")
    SAVE_TRIP_BUTTON = (AppiumBy.XPATH, "//*[@text='Save Trip']")

class ProfileScreen(BaseScreen):
    LOGOUT_TILE = (AppiumBy.XPATH, "//*[@text='Log Out']")
    SETTINGS_TILE = (AppiumBy.XPATH, "//*[@text='Settings']")
    PERSONAL_INFO_TILE = (AppiumBy.XPATH, "//*[@text='Personal Information']")
