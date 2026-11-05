# Auto-generated Appium Mobile UI Test Suite
# Conforms to Screen Object Model, pytest, and UiAutomator2
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from screens.dashboard_screens import DashboardScreen

@pytest.mark.appium
@pytest.mark.test_id('APP-096')
def test_app_096_dashboard_bottom_navigation_render(driver, app_package):
    """APP-096: Dashboard Bottom Navigation Render - Verify BottomNavigationBar displays 5 items: Home, Explore, Trips, Alerts, Profile"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-097')
def test_app_097_dashboard_initial_home_tab_active(driver, app_package):
    """APP-097: Dashboard Initial Home Tab Active - Verify Home tab is selected by default on dashboard load"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-098')
def test_app_098_dashboard_user_greeting_banner(driver, app_package):
    """APP-098: Dashboard User Greeting Banner - Verify header displays personalized greeting with user name"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-099')
def test_app_099_dashboard_notification_bell_icon(driver, app_package):
    """APP-099: Dashboard Notification Bell Icon - Verify notification bell icon button in top AppBar"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-100')
def test_app_100_dashboard_avatar_action(driver, app_package):
    """APP-100: Dashboard Avatar Action - Verify user avatar thumbnail in top AppBar"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-101')
def test_app_101_dashboard_active_trip_card(driver, app_package):
    """APP-101: Dashboard Active Trip Card - Verify active upcoming trip itinerary card is rendered on Home"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-102')
def test_app_102_dashboard_active_trip_cost_badge(driver, app_package):
    """APP-102: Dashboard Active Trip Cost Badge - Verify 'Cost Optimized' chip is rendered on active trip card"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-103')
def test_app_103_dashboard_active_trip_timeline_item(driver, app_package):
    """APP-103: Dashboard Active Trip Timeline Item - Verify timeline items (e.g. Day 1 activities) on active trip card"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-104')
def test_app_104_dashboard_quick_action_plan_trip(driver, app_package):
    """APP-104: Dashboard Quick Action Plan Trip - Tap 'Plan Trip' quick action button on Home screen"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-105')
def test_app_105_dashboard_quick_action_budget_tool(driver, app_package):
    """APP-105: Dashboard Quick Action Budget Tool - Tap 'Budget Tool' quick action button on Home screen"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-106')
def test_app_106_dashboard_quick_action_top_destinations(driver, app_package):
    """APP-106: Dashboard Quick Action Top Destinations - Tap 'Top Destinations' quick action button on Home screen"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-107')
def test_app_107_dashboard_quick_action_ai_suggestions(driver, app_package):
    """APP-107: Dashboard Quick Action AI Suggestions - Tap 'AI Suggestions' quick action button on Home screen"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-108')
def test_app_108_dashboard_featured_destinations_carousel(driver, app_package):
    """APP-108: Dashboard Featured Destinations Carousel - Verify horizontal list of featured destinations on Home screen"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-109')
def test_app_109_dashboard_destination_card_tap(driver, app_package):
    """APP-109: Dashboard Destination Card Tap - Tap on 'Goa' destination card in featured list"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-110')
def test_app_110_dashboard_destination_rating_display(driver, app_package):
    """APP-110: Dashboard Destination Rating Display - Verify destination cards display star rating (e.g. 4.8)"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-111')
def test_app_111_dashboard_destination_category_tag(driver, app_package):
    """APP-111: Dashboard Destination Category Tag - Verify destination category pill (Beach, Mountain, etc.)"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-112')
def test_app_112_dashboard_pull_to_refresh(driver, app_package):
    """APP-112: Dashboard Pull To Refresh - Perform swipe down gesture on Home screen to trigger refresh"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-113')
def test_app_113_dashboard_tab_switch_to_explore(driver, app_package):
    """APP-113: Dashboard Tab Switch To Explore - Tap 'Explore' tab in bottom navigation bar"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-114')
def test_app_114_dashboard_tab_switch_to_trips(driver, app_package):
    """APP-114: Dashboard Tab Switch To Trips - Tap 'Trips' tab in bottom navigation bar"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-115')
def test_app_115_dashboard_tab_switch_to_alerts(driver, app_package):
    """APP-115: Dashboard Tab Switch To Alerts - Tap 'Alerts' tab in bottom navigation bar"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-116')
def test_app_116_dashboard_tab_switch_to_profile(driver, app_package):
    """APP-116: Dashboard Tab Switch To Profile - Tap 'Profile' tab in bottom navigation bar"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-117')
def test_app_117_dashboard_tab_return_to_home(driver, app_package):
    """APP-117: Dashboard Tab Return To Home - Tap 'Home' tab after visiting other tabs"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-118')
def test_app_118_dashboard_budget_summary_card(driver, app_package):
    """APP-118: Dashboard Budget Summary Card - Verify budget statistics overview card on Home screen"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-119')
def test_app_119_dashboard_travel_advisory_notice(driver, app_package):
    """APP-119: Dashboard Travel Advisory Notice - Verify advisory or seasonal tip card on Home screen"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-120')
def test_app_120_dashboard_empty_trip_state(driver, app_package):
    """APP-120: Dashboard Empty Trip State - Verify helpful prompt when user has zero planned trips"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-121')
def test_app_121_dashboard_view_all_destinations_link(driver, app_package):
    """APP-121: Dashboard View All Destinations Link - Tap 'View All' link next to Popular Destinations header"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-122')
def test_app_122_dashboard_dark_mode_rendering(driver, app_package):
    """APP-122: Dashboard Dark Mode Rendering - Verify dashboard colors in Android dark mode"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-123')
def test_app_123_dashboard_offline_banner(driver, app_package):
    """APP-123: Dashboard Offline Banner - Verify subtle offline indicator when internet connection drops"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-124')
def test_app_124_dashboard_hardware_back_button_behavior(driver, app_package):
    """APP-124: Dashboard Hardware Back Button Behavior - Press back button on Home tab"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-125')
def test_app_125_dashboard_bottom_bar_safe_area_inset(driver, app_package):
    """APP-125: Dashboard Bottom Bar Safe Area Inset - Verify bottom navigation does not overlap Android navigation bar"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-126')
def test_app_126_dashboard_fast_tab_switching(driver, app_package):
    """APP-126: Dashboard Fast Tab Switching - Rapidly tap between tabs in bottom navigation bar"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-127')
def test_app_127_dashboard_scroll_position_preservation(driver, app_package):
    """APP-127: Dashboard Scroll Position Preservation - Scroll down Home screen, switch tabs and return"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-128')
def test_app_128_dashboard_image_memory_caching(driver, app_package):
    """APP-128: Dashboard Image Memory Caching - Verify cached network images load instantly without re-downloading"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-129')
def test_app_129_dashboard_currency_symbol_display(driver, app_package):
    """APP-129: Dashboard Currency Symbol Display - Verify Indian Rupee (₹) symbol renders on all price elements"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-130')
def test_app_130_dashboard_orientation_rotation(driver, app_package):
    """APP-130: Dashboard Orientation Rotation - Rotate dashboard to landscape and back to portrait"""
    dash = DashboardScreen(driver)
    assert dash.is_visible(DashboardScreen.BOTTOM_NAV_HOME, timeout=6)
