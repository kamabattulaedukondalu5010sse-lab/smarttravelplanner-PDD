from selenium.webdriver.common.by import By
from .base_page import BasePage

class ExpensesPage(BasePage):
    HEADER = (By.XPATH, "//h2[contains(., 'Expense')]")
    TOTAL_SPEND_CARD = (By.XPATH, "//*[contains(text(), 'Total Spend')]")
    REMAINING_BUDGET_CARD = (By.XPATH, "//*[contains(text(), 'Remaining')]")
    ADD_EXPENSE_BUTTON = (By.XPATH, "//button[contains(., 'Add Expense')]")
    TITLE_INPUT = (By.CSS_SELECTOR, "input[placeholder*='title' i], input[placeholder*='dinner' i]")
    AMOUNT_INPUT = (By.CSS_SELECTOR, "input[type='number']")
    CATEGORY_SELECT = (By.CSS_SELECTOR, "select")
    SUBMIT_EXPENSE = (By.XPATH, "//button[contains(text(), 'Add') or contains(text(), 'Save')]")
    EXPENSE_ROWS = (By.CSS_SELECTOR, "table tbody tr, div[style*='border-bottom']")
    DOUGHNUT_CHART = (By.CSS_SELECTOR, "canvas")

    def add_expense(self, title, amount, category="food"):
        if self.is_visible(self.ADD_EXPENSE_BUTTON, timeout=3):
            self.click(self.ADD_EXPENSE_BUTTON)
            if self.is_visible(self.TITLE_INPUT, timeout=2):
                self.type_text(self.TITLE_INPUT, title)
            if self.is_visible(self.AMOUNT_INPUT, timeout=2):
                self.type_text(self.AMOUNT_INPUT, str(amount))
            if self.is_visible(self.SUBMIT_EXPENSE, timeout=2):
                self.click(self.SUBMIT_EXPENSE)
