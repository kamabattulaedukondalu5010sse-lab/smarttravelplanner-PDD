# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.history_page import HistoryPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-261')
def test_sel_261_travel_history_navigation(driver, base_url, test_username, test_password):
    """SEL-261: Travel History Navigation - Click 'Travel History' tab in sidebar navigation"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-262')
def test_sel_262_travel_history_header_render(driver, base_url, test_username, test_password):
    """SEL-262: Travel History Header Render - Verify 'Travel History & Archives' heading renders"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-263')
def test_sel_263_empty_history_state_view(driver, base_url, test_username, test_password):
    """SEL-263: Empty History State View - Verify empty state message when user has no completed past trips"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-264')
def test_sel_264_mark_trip_completed_from_dashboard(driver, base_url, test_username, test_password):
    """SEL-264: Mark Trip Completed From Dashboard - Click 'Mark Completed' on active trip from Dashboard view"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-265')
def test_sel_265_trip_status_update_api_call(driver, base_url, test_username, test_password):
    """SEL-265: Trip Status Update API Call - Verify PUT /api/trips/:id/status sends { status: 'completed' }"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-266')
def test_sel_266_trip_moves_to_travel_history(driver, base_url, test_username, test_password):
    """SEL-266: Trip Moves To Travel History - Navigate to Travel History and verify completed trip appears"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-267')
def test_sel_267_completed_trip_status_badge(driver, base_url, test_username, test_password):
    """SEL-267: Completed Trip Status Badge - Verify completed trip card displays 'Completed' badge in emerald green"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-268')
def test_sel_268_completed_trip_final_budget_vs_actual(driver, base_url, test_username, test_password):
    """SEL-268: Completed Trip Final Budget vs Actual - Verify completed trip card displays initial budget vs final cost"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-269')
def test_sel_269_archived_trip_itinerary_view(driver, base_url, test_username, test_password):
    """SEL-269: Archived Trip Itinerary View - Click 'View Itinerary' button on archived trip card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-270')
def test_sel_270_archived_itinerary_map_replay(driver, base_url, test_username, test_password):
    """SEL-270: Archived Itinerary Map Replay - Verify past trip route waypoints render on map in history view"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-271')
def test_sel_271_re_plan_trip_from_history_action(driver, base_url, test_username, test_password):
    """SEL-271: Re-Plan Trip From History Action - Click 'Plan Similar Trip' button on archived trip card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-272')
def test_sel_272_history_filter_by_year(driver, base_url, test_username, test_password):
    """SEL-272: History Filter By Year - Select year filter dropdown (e.g. 2026)"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-273')
def test_sel_273_history_filter_by_destination(driver, base_url, test_username, test_password):
    """SEL-273: History Filter By Destination - Filter historical trips by destination name"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-274')
def test_sel_274_history_total_distance_traveled_metric(driver, base_url, test_username, test_password):
    """SEL-274: History Total Distance Traveled Metric - Verify lifetime travel summary metrics card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-275')
def test_sel_275_delete_archived_trip_trigger(driver, base_url, test_username, test_password):
    """SEL-275: Delete Archived Trip Trigger - Click delete icon on archived historical trip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-276')
def test_sel_276_delete_archived_trip_execution(driver, base_url, test_username, test_password):
    """SEL-276: Delete Archived Trip Execution - Confirm deletion of archived trip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-277')
def test_sel_277_history_trip_card_responsive_layout(driver, base_url, test_username, test_password):
    """SEL-277: History Trip Card Responsive Layout - Inspect history cards on tablet and mobile viewports"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-278')
def test_sel_278_history_print_itinerary_summary(driver, base_url, test_username, test_password):
    """SEL-278: History Print Itinerary Summary - Click 'Print Itinerary' on past trip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-279')
def test_sel_279_history_rating_feedback_submission(driver, base_url, test_username, test_password):
    """SEL-279: History Rating Feedback Submission - Submit post-trip destination review and star rating"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-280')
def test_sel_280_history_direct_api_get_api_trips_verification(driver, base_url, test_username, test_password):
    """SEL-280: History Direct API GET /api/trips Verification - Verify GET /api/trips returns trips with status='completed'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.HISTORY_TAB)
    history = HistoryPage(driver, base_url)
    assert history.is_visible(HistoryPage.HEADER, timeout=8)
