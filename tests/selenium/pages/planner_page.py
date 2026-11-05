from selenium.webdriver.common.by import By
from .base_page import BasePage

class PlannerPage(BasePage):
    DESTINATION_SELECT = (By.CSS_SELECTOR, "select, select[name='destination']")
    START_DATE_INPUT = (By.CSS_SELECTOR, "input[type='date']:nth-of-type(1)")
    END_DATE_INPUT = (By.CSS_SELECTOR, "input[type='date']:nth-of-type(2)")
    TRAVELERS_INPUT = (By.CSS_SELECTOR, "input[type='number']:nth-of-type(1)")
    BUDGET_INPUT = (By.CSS_SELECTOR, "input[type='number']:nth-of-type(2)")
    OPTIMIZE_BUTTON = (By.XPATH, "//button[contains(., 'Optimize') or contains(., 'Plan')]")
    RESULT_CARD = (By.XPATH, "//*[contains(text(), 'Optimized Cost') or contains(text(), 'Savings')]")
    SAVINGS_BADGE = (By.XPATH, "//*[contains(text(), 'Saved') or contains(text(), 'Savings')]")

    def plan_trip(self, destination="Goa", budget="25000", travelers="2"):
        if self.is_visible(self.DESTINATION_SELECT, timeout=3):
            # Try to select
            select_el = self.find(self.DESTINATION_SELECT)
            select_el.send_keys(destination)
        if self.is_visible(self.BUDGET_INPUT, timeout=2):
            self.type_text(self.BUDGET_INPUT, budget)
        if self.is_visible(self.TRAVELERS_INPUT, timeout=2):
            self.type_text(self.TRAVELERS_INPUT, travelers)
        self.click(self.OPTIMIZE_BUTTON)

    def is_result_displayed(self):
        return self.is_visible(self.RESULT_CARD, timeout=5)
