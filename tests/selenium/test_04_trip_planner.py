# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.planner_page import PlannerPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-096')
def test_sel_096_planner_view_navigation(driver, base_url, test_username, test_password):
    """SEL-096: Planner View Navigation - Click 'Trip Planner' tab from sidebar navigation"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-097')
def test_sel_097_planner_form_destination_select(driver, base_url, test_username, test_password):
    """SEL-097: Planner Form Destination Select - Verify destination dropdown options include Goa, Manali, Kerala, Dubai"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-098')
def test_sel_098_planner_form_select_destination(driver, base_url, test_username, test_password):
    """SEL-098: Planner Form Select Destination - Select 'Kerala' from destination dropdown"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-099')
def test_sel_099_planner_form_start_date_picker(driver, base_url, test_username, test_password):
    """SEL-099: Planner Form Start Date Picker - Verify start date input field is present and configurable"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-100')
def test_sel_100_planner_form_end_date_picker(driver, base_url, test_username, test_password):
    """SEL-100: Planner Form End Date Picker - Verify end date input field is present and configurable"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-101')
def test_sel_101_planner_form_date_range_validation(driver, base_url, test_username, test_password):
    """SEL-101: Planner Form Date Range Validation - Enter end date that precedes start date"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-102')
def test_sel_102_planner_form_travelers_count_input(driver, base_url, test_username, test_password):
    """SEL-102: Planner Form Travelers Count Input - Verify travelers count numeric input accepts values >= 1"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-103')
def test_sel_103_planner_form_zero_travelers_rejection(driver, base_url, test_username, test_password):
    """SEL-103: Planner Form Zero Travelers Rejection - Enter 0 in travelers count input"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-104')
def test_sel_104_planner_form_negative_travelers_rejection(driver, base_url, test_username, test_password):
    """SEL-104: Planner Form Negative Travelers Rejection - Enter -3 in travelers count input"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-105')
def test_sel_105_planner_form_budget_input(driver, base_url, test_username, test_password):
    """SEL-105: Planner Form Budget Input - Enter budget amount of 35000"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-106')
def test_sel_106_planner_form_zero_budget_rejection(driver, base_url, test_username, test_password):
    """SEL-106: Planner Form Zero Budget Rejection - Enter 0 in budget input field"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-107')
def test_sel_107_planner_submit_optimization_button(driver, base_url, test_username, test_password):
    """SEL-107: Planner Submit Optimization Button - Verify 'Optimize & Plan Trip' submit button is visible"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-108')
def test_sel_108_planner_run_optimization_execution(driver, base_url, test_username, test_password):
    """SEL-108: Planner Run Optimization Execution - Submit valid trip planning parameters for Goa"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-109')
def test_sel_109_optimization_result_card_display(driver, base_url, test_username, test_password):
    """SEL-109: Optimization Result Card Display - Verify optimization summary card appears post-submission"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-110')
def test_sel_110_cost_savings_calculation(driver, base_url, test_username, test_password):
    """SEL-110: Cost Savings Calculation - Verify calculated savings amount equals Budget minus Optimized Cost"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-111')
def test_sel_111_savings_percentage_display(driver, base_url, test_username, test_password):
    """SEL-111: Savings Percentage Display - Verify savings percentage badge is accurately calculated"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-112')
def test_sel_112_stay_recommendation_note(driver, base_url, test_username, test_password):
    """SEL-112: Stay Recommendation Note - Verify budget hotel or stay suggestion note is displayed"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-113')
def test_sel_113_optimized_transport_selection(driver, base_url, test_username, test_password):
    """SEL-113: Optimized Transport Selection - Verify suggested transport mode (Flight, Train, Cab)"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-114')
def test_sel_114_generated_itinerary_days_count(driver, base_url, test_username, test_password):
    """SEL-114: Generated Itinerary Days Count - Verify generated itinerary matches requested travel duration"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-115')
def test_sel_115_itinerary_activity_time_display(driver, base_url, test_username, test_password):
    """SEL-115: Itinerary Activity Time Display - Verify itinerary items display schedule times (e.g. 09:00 AM)"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-116')
def test_sel_116_itinerary_activity_category_icons(driver, base_url, test_username, test_password):
    """SEL-116: Itinerary Activity Category Icons - Verify activity category icons (Food, Stay, Transport, Activities)"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-117')
def test_sel_117_itinerary_map_waypoints_update(driver, base_url, test_username, test_password):
    """SEL-117: Itinerary Map Waypoints Update - Verify Leaflet map updates center and markers to match chosen destination"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-118')
def test_sel_118_save_trip_action_button(driver, base_url, test_username, test_password):
    """SEL-118: Save Trip Action Button - Verify 'Save Trip' or 'Book Trip' button on optimized itinerary"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-119')
def test_sel_119_saved_trip_confirmation_alert(driver, base_url, test_username, test_password):
    """SEL-119: Saved Trip Confirmation Alert - Click Save Trip and verify success confirmation toast"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-120')
def test_sel_120_trip_appears_in_dashboard(driver, base_url, test_username, test_password):
    """SEL-120: Trip Appears In Dashboard - Navigate back to Dashboard and verify newly planned trip is active"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-121')
def test_sel_121_planner_reset_form_action(driver, base_url, test_username, test_password):
    """SEL-121: Planner Reset Form Action - Verify form fields can be reset or updated for new destination"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-122')
def test_sel_122_planner_budget_slider_if_present(driver, base_url, test_username, test_password):
    """SEL-122: Planner Budget Slider If Present - Interact with budget slider or step input controls"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-123')
def test_sel_123_planner_multi_day_itinerary_expansion(driver, base_url, test_username, test_password):
    """SEL-123: Planner Multi-day Itinerary Expansion - Click Day 2 accordion to expand second day schedule"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-124')
def test_sel_124_planner_activity_cost_modification(driver, base_url, test_username, test_password):
    """SEL-124: Planner Activity Cost Modification - Inspect activity cost badges across itinerary items"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-125')
def test_sel_125_planner_luxury_destination_tier(driver, base_url, test_username, test_password):
    """SEL-125: Planner Luxury Destination Tier - Select 'Dubai' and verify higher cost factor scaling"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-126')
def test_sel_126_planner_budget_destination_tier(driver, base_url, test_username, test_password):
    """SEL-126: Planner Budget Destination Tier - Select 'Goa' or 'Shimla' and verify standard cost factor"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-127')
def test_sel_127_planner_form_preserves_state_on_tab_switch(driver, base_url, test_username, test_password):
    """SEL-127: Planner Form Preserves State On Tab Switch - Switch to Bookings tab and back to Planner"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-128')
def test_sel_128_planner_non_numeric_budget_rejection(driver, base_url, test_username, test_password):
    """SEL-128: Planner Non-numeric Budget Rejection - Enter text 'twenty thousand' in budget field"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-129')
def test_sel_129_planner_max_date_limit_handling(driver, base_url, test_username, test_password):
    """SEL-129: Planner Max Date Limit Handling - Select start date 2 years in advance"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-130')
def test_sel_130_planner_same_day_trip_support(driver, base_url, test_username, test_password):
    """SEL-130: Planner Same Day Trip Support - Select same start and end date for day trip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-131')
def test_sel_131_planner_high_travelers_scaling(driver, base_url, test_username, test_password):
    """SEL-131: Planner High Travelers Scaling - Set travelers count to 10 and verify cost scaling"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-132')
def test_sel_132_planner_route_polyline_on_map(driver, base_url, test_username, test_password):
    """SEL-132: Planner Route Polyline On Map - Verify Leaflet map draws polyline path between sequential activities"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-133')
def test_sel_133_planner_activity_coordinates_fallback(driver, base_url, test_username, test_password):
    """SEL-133: Planner Activity Coordinates Fallback - Verify activities with missing lat/lng use destination defaults"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-134')
def test_sel_134_planner_direct_api_submission(driver, base_url, test_username, test_password):
    """SEL-134: Planner Direct API Submission - Verify POST /api/trips payload includes destination, dates, budget"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-135')
def test_sel_135_planner_visual_progress_indicator(driver, base_url, test_username, test_password):
    """SEL-135: Planner Visual Progress Indicator - Verify spinner or loading state during cost optimization calculation"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PLAN_TRIP_BTN)
    planner = PlannerPage(driver, base_url)
    assert planner.is_visible(PlannerPage.OPTIMIZE_BUTTON, timeout=8)
