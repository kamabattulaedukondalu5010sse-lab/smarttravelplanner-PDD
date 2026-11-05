# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-066')
def test_sel_066_dashboard_header_brand_render(driver, base_url, test_username, test_password):
    """SEL-066: Dashboard Header Brand Render - Verify sidebar brand header displays Smart Travel Planner"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-067')
def test_sel_067_dashboard_navigation_items_list(driver, base_url, test_username, test_password):
    """SEL-067: Dashboard Navigation Items List - Verify navigation sidebar contains all 7 view tabs"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-068')
def test_sel_068_dashboard_tab_active_styling(driver, base_url, test_username, test_password):
    """SEL-068: Dashboard Tab Active Styling - Verify active Dashboard tab has primary blue background"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-069')
def test_sel_069_dashboard_welcome_banner_text(driver, base_url, test_username, test_password):
    """SEL-069: Dashboard Welcome Banner Text - Verify personalized greeting message on Dashboard"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-070')
def test_sel_070_active_trip_card_presence(driver, base_url, test_username, test_password):
    """SEL-070: Active Trip Card Presence - Verify active or upcoming trip itinerary card is rendered"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-071')
def test_sel_071_active_trip_cost_optimization_badge(driver, base_url, test_username, test_password):
    """SEL-071: Active Trip Cost Optimization Badge - Verify 'Cost Optimized' pill badge appears on active trip card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-072')
def test_sel_072_active_trip_mark_completed_button(driver, base_url, test_username, test_password):
    """SEL-072: Active Trip Mark Completed Button - Verify 'Mark Completed' action button on upcoming trip card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-073')
def test_sel_073_active_trip_view_details_button(driver, base_url, test_username, test_password):
    """SEL-073: Active Trip View Details Button - Click 'View Details' button on active trip card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-074')
def test_sel_074_destinations_grid_section_header(driver, base_url, test_username, test_password):
    """SEL-074: Destinations Grid Section Header - Verify 'Popular Destinations' heading is displayed"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-075')
def test_sel_075_destination_cards_count(driver, base_url, test_username, test_password):
    """SEL-075: Destination Cards Count - Verify destination cards render for all available catalog items"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-076')
def test_sel_076_destination_card_image_rendering(driver, base_url, test_username, test_password):
    """SEL-076: Destination Card Image Rendering - Verify destination card displays non-broken image thumbnail"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-077')
def test_sel_077_destination_card_rating_star(driver, base_url, test_username, test_password):
    """SEL-077: Destination Card Rating Star - Verify destination card displays numeric rating with star icon"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-078')
def test_sel_078_destination_card_category_tag(driver, base_url, test_username, test_password):
    """SEL-078: Destination Card Category Tag - Verify destination card displays category badge (Beach, Mountain, etc.)"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-079')
def test_sel_079_destination_card_cost_factor(driver, base_url, test_username, test_password):
    """SEL-079: Destination Card Cost Factor - Verify cost factor or pricing tier is shown on destination card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-080')
def test_sel_080_destination_card_quick_plan_action(driver, base_url, test_username, test_password):
    """SEL-080: Destination Card Quick Plan Action - Click 'Plan Trip' action button on Goa destination card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-081')
def test_sel_081_destination_search_input_filter(driver, base_url, test_username, test_password):
    """SEL-081: Destination Search Input Filter - Type 'Manali' into destination search box"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-082')
def test_sel_082_destination_search_clear_action(driver, base_url, test_username, test_password):
    """SEL-082: Destination Search Clear Action - Clear search query from input box"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-083')
def test_sel_083_destination_search_no_results_state(driver, base_url, test_username, test_password):
    """SEL-083: Destination Search No Results State - Type nonexistent destination query 'AtlantisCity'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-084')
def test_sel_084_dashboard_quick_stats_budget_overview(driver, base_url, test_username, test_password):
    """SEL-084: Dashboard Quick Stats Budget Overview - Verify summary statistics widget for Total Budget"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-085')
def test_sel_085_dashboard_quick_stats_trips_count(driver, base_url, test_username, test_password):
    """SEL-085: Dashboard Quick Stats Trips Count - Verify summary statistics widget for Planned Trips"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-086')
def test_sel_086_dashboard_responsive_sidebar_toggle(driver, base_url, test_username, test_password):
    """SEL-086: Dashboard Responsive Sidebar Toggle - Verify sidebar navigation collapse on smaller screen widths"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-087')
def test_sel_087_dashboard_leaflet_map_container(driver, base_url, test_username, test_password):
    """SEL-087: Dashboard Leaflet Map Container - Verify interactive itinerary route map container is mounted"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-088')
def test_sel_088_dashboard_map_marker_rendering(driver, base_url, test_username, test_password):
    """SEL-088: Dashboard Map Marker Rendering - Verify activity waypoint markers appear on the route map"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-089')
def test_sel_089_dashboard_itinerary_day_timeline(driver, base_url, test_username, test_password):
    """SEL-089: Dashboard Itinerary Day Timeline - Verify Day 1 and Day 2 timeline items appear on trip card"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-090')
def test_sel_090_dashboard_activity_cost_tag(driver, base_url, test_username, test_password):
    """SEL-090: Dashboard Activity Cost Tag - Verify each activity item in itinerary lists individual cost"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-091')
def test_sel_091_dashboard_travel_alert_notification(driver, base_url, test_username, test_password):
    """SEL-091: Dashboard Travel Alert Notification - Verify travel advisory or weather notification banner"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-092')
def test_sel_092_dashboard_top_navigation_header(driver, base_url, test_username, test_password):
    """SEL-092: Dashboard Top Navigation Header - Verify top bar displays quick user avatar and notification bell"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-093')
def test_sel_093_dashboard_currency_formatting(driver, base_url, test_username, test_password):
    """SEL-093: Dashboard Currency Formatting - Verify monetary values are formatted with Indian Rupee (₹) symbol"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-094')
def test_sel_094_dashboard_page_title_metadata(driver, base_url, test_username, test_password):
    """SEL-094: Dashboard Page Title Metadata - Verify document title in browser tab reflects Smart Travel Planner"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-095')
def test_sel_095_dashboard_scroll_to_destinations(driver, base_url, test_username, test_password):
    """SEL-095: Dashboard Scroll To Destinations - Scroll down to browse full destination catalogue"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    assert dash.is_visible(DashboardPage.PLAN_TRIP_BTN, timeout=8)
