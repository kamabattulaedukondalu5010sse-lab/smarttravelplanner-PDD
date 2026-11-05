from selenium.webdriver.common.by import By
from .base_page import BasePage

class BookingsPage(BasePage):
    BOOKINGS_HEADER = (By.XPATH, "//h2[contains(., 'Booking') or contains(., 'Hotel')]")
    NEW_BOOKING_BUTTON = (By.XPATH, "//button[contains(., 'New Booking') or contains(., 'Book')]")
    BOOKING_CARDS = (By.CSS_SELECTOR, "div[style*='border-radius: 12px']")
    MODAL_SUBMIT = (By.XPATH, "//button[contains(text(), 'Confirm') or contains(text(), 'Book Now')]")
    MODAL_CANCEL = (By.XPATH, "//button[contains(text(), 'Cancel')]")
    RADIO_DELUXE = (By.CSS_SELECTOR, "input[type='radio'][value*='Deluxe' i]")
    RADIO_SEAVIEW = (By.CSS_SELECTOR, "input[type='radio'][value*='Sea' i]")

    def open_new_booking(self):
        if self.is_visible(self.NEW_BOOKING_BUTTON, timeout=3):
            self.click(self.NEW_BOOKING_BUTTON)
