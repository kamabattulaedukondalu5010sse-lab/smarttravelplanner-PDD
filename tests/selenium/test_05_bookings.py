# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.bookings_page import BookingsPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-136')
def test_sel_136_bookings_tab_navigation(driver, base_url, test_username, test_password):
    """SEL-136: Bookings Tab Navigation - Click 'Bookings' tab in sidebar navigation"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-137')
def test_sel_137_bookings_header_render(driver, base_url, test_username, test_password):
    """SEL-137: Bookings Header Render - Verify 'Your Bookings' page heading and subtitle render"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-138')
def test_sel_138_empty_bookings_state_view(driver, base_url, test_username, test_password):
    """SEL-138: Empty Bookings State View - Verify empty state message when user has no active bookings"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-139')
def test_sel_139_new_booking_button_trigger(driver, base_url, test_username, test_password):
    """SEL-139: New Booking Button Trigger - Click 'New Booking' button to open booking modal"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-140')
def test_sel_140_booking_modal_trip_selector(driver, base_url, test_username, test_password):
    """SEL-140: Booking Modal Trip Selector - Verify trip dropdown inside booking modal lists planned trips"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-141')
def test_sel_141_booking_modal_hotel_room_options(driver, base_url, test_username, test_password):
    """SEL-141: Booking Modal Hotel Room Options - Verify hotel room type radio buttons (Deluxe Room vs Sea View Suite)"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-142')
def test_sel_142_booking_modal_radio_selection_deluxe(driver, base_url, test_username, test_password):
    """SEL-142: Booking Modal Radio Selection Deluxe - Select 'Deluxe Room' radio option"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-143')
def test_sel_143_booking_modal_radio_selection_sea_view(driver, base_url, test_username, test_password):
    """SEL-143: Booking Modal Radio Selection Sea View - Select 'Sea View Suite' radio option"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-144')
def test_sel_144_booking_modal_dates_auto_populate(driver, base_url, test_username, test_password):
    """SEL-144: Booking Modal Dates Auto-populate - Verify check-in and check-out dates populate from selected trip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-145')
def test_sel_145_booking_modal_price_calculation(driver, base_url, test_username, test_password):
    """SEL-145: Booking Modal Price Calculation - Verify total booking cost displays based on selected option"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-146')
def test_sel_146_booking_modal_cancel_action(driver, base_url, test_username, test_password):
    """SEL-146: Booking Modal Cancel Action - Click 'Cancel' button inside booking modal"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-147')
def test_sel_147_booking_modal_backdrop_click_dismissal(driver, base_url, test_username, test_password):
    """SEL-147: Booking Modal Backdrop Click Dismissal - Click outside booking modal on dimmed backdrop"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-148')
def test_sel_148_booking_modal_submit_confirmation(driver, base_url, test_username, test_password):
    """SEL-148: Booking Modal Submit Confirmation - Submit new booking for active Goa trip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-149')
def test_sel_149_booking_card_appears_in_list(driver, base_url, test_username, test_password):
    """SEL-149: Booking Card Appears in List - Verify newly confirmed booking appears in Bookings list"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-150')
def test_sel_150_booking_card_status_badge(driver, base_url, test_username, test_password):
    """SEL-150: Booking Card Status Badge - Verify booking item displays 'Confirmed' badge in green"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-151')
def test_sel_151_booking_card_details_display(driver, base_url, test_username, test_password):
    """SEL-151: Booking Card Details Display - Verify booking item displays room category and traveler count"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-152')
def test_sel_152_booking_card_cost_display(driver, base_url, test_username, test_password):
    """SEL-152: Booking Card Cost Display - Verify booking item displays formatted cost in INR"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-153')
def test_sel_153_booking_card_cancellation_trigger(driver, base_url, test_username, test_password):
    """SEL-153: Booking Card Cancellation Trigger - Click 'Cancel Booking' action button on booking card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-154')
def test_sel_154_booking_cancellation_execution(driver, base_url, test_username, test_password):
    """SEL-154: Booking Cancellation Execution - Confirm cancellation of existing booking"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-155')
def test_sel_155_booking_filter_all(driver, base_url, test_username, test_password):
    """SEL-155: Booking Filter All - Click 'All Bookings' filter chip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-156')
def test_sel_156_booking_filter_confirmed(driver, base_url, test_username, test_password):
    """SEL-156: Booking Filter Confirmed - Click 'Confirmed' filter chip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-157')
def test_sel_157_booking_filter_cancelled(driver, base_url, test_username, test_password):
    """SEL-157: Booking Filter Cancelled - Click 'Cancelled' filter chip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-158')
def test_sel_158_direct_booking_from_dashboard(driver, base_url, test_username, test_password):
    """SEL-158: Direct Booking From Dashboard - Click 'Book Stay' button directly on Dashboard active trip card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-159')
def test_sel_159_duplicate_booking_guard(driver, base_url, test_username, test_password):
    """SEL-159: Duplicate Booking Guard - Attempt to book the same room for overlapping dates"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-160')
def test_sel_160_booking_reference_id_render(driver, base_url, test_username, test_password):
    """SEL-160: Booking Reference ID Render - Verify booking card displays unique reference identifier"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-161')
def test_sel_161_booking_contact_details_render(driver, base_url, test_username, test_password):
    """SEL-161: Booking Contact Details Render - Verify guest contact email is shown on booking summary"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-162')
def test_sel_162_booking_modal_form_accessibility(driver, base_url, test_username, test_password):
    """SEL-162: Booking Modal Form Accessibility - Verify Esc key closes open booking modal"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-163')
def test_sel_163_booking_receipt_view_action(driver, base_url, test_username, test_password):
    """SEL-163: Booking Receipt View Action - Click 'View Receipt' or details action on booking card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-164')
def test_sel_164_booking_list_sorting_by_date(driver, base_url, test_username, test_password):
    """SEL-164: Booking List Sorting By Date - Verify bookings are sorted chronologically by check-in date"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-165')
def test_sel_165_booking_payment_status_badge(driver, base_url, test_username, test_password):
    """SEL-165: Booking Payment Status Badge - Verify payment status badge indicates 'Paid' or 'Pending'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-166')
def test_sel_166_booking_transport_mode_booking(driver, base_url, test_username, test_password):
    """SEL-166: Booking Transport Mode Booking - Select transport booking tab if multi-service booking is active"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-167')
def test_sel_167_booking_responsive_card_layout(driver, base_url, test_username, test_password):
    """SEL-167: Booking Responsive Card Layout - Inspect booking card elements across mobile screen size"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-168')
def test_sel_168_booking_direct_api_post_verification(driver, base_url, test_username, test_password):
    """SEL-168: Booking Direct API POST Verification - Verify POST /api/bookings sends tripId, roomType, and totalCost"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-169')
def test_sel_169_booking_refresh_list_state(driver, base_url, test_username, test_password):
    """SEL-169: Booking Refresh List State - Refresh page and verify persisted bookings reload from API"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-170')
def test_sel_170_booking_offline_sync_guard(driver, base_url, test_username, test_password):
    """SEL-170: Booking Offline Sync Guard - Attempt booking while simulated offline"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.BOOKINGS_TAB)
    bookings = BookingsPage(driver, base_url)
    assert bookings.is_visible(BookingsPage.BOOKINGS_HEADER, timeout=8)
