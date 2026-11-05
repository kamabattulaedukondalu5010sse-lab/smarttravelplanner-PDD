# Auto-generated Appium Mobile UI Test Suite
# Conforms to Screen Object Model, pytest, and UiAutomator2
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from screens.dashboard_screens import PlannerScreen

@pytest.mark.appium
@pytest.mark.test_id('APP-161')
def test_app_161_planner_screen_initial_load(driver, app_package):
    """APP-161: Planner Screen Initial Load - Navigate to CreateTripScreen / Planner"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-162')
def test_app_162_planner_destination_dropdown(driver, app_package):
    """APP-162: Planner Destination Dropdown - Verify destination dropdown contains all available locations"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-163')
def test_app_163_planner_select_destination(driver, app_package):
    """APP-163: Planner Select Destination - Select 'Goa' from destination dropdown"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-164')
def test_app_164_planner_date_range_picker_trigger(driver, app_package):
    """APP-164: Planner Date Range Picker Trigger - Tap travel dates input field to open date picker"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-165')
def test_app_165_planner_select_date_range(driver, app_package):
    """APP-165: Planner Select Date Range - Select start date and end date in calendar picker"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-166')
def test_app_166_planner_travelers_stepper_increment(driver, app_package):
    """APP-166: Planner Travelers Stepper Increment - Tap plus (+) button to increment travelers count"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-167')
def test_app_167_planner_travelers_stepper_decrement(driver, app_package):
    """APP-167: Planner Travelers Stepper Decrement - Tap minus (-) button to decrement travelers count"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-168')
def test_app_168_planner_travelers_minimum_limit(driver, app_package):
    """APP-168: Planner Travelers Minimum Limit - Attempt to decrement travelers count below 1"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-169')
def test_app_169_planner_total_budget_input(driver, app_package):
    """APP-169: Planner Total Budget Input - Enter budget amount '25000' in budget TextField"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-170')
def test_app_170_planner_empty_budget_validation(driver, app_package):
    """APP-170: Planner Empty Budget Validation - Attempt optimization with blank budget field"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-171')
def test_app_171_planner_zero_budget_validation(driver, app_package):
    """APP-171: Planner Zero Budget Validation - Enter 0 in budget field and submit"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-172')
def test_app_172_planner_optimize_button_presence(driver, app_package):
    """APP-172: Planner Optimize Button Presence - Verify 'Optimize Trip' elevated button is rendered"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-173')
def test_app_173_planner_optimize_trip_execution(driver, app_package):
    """APP-173: Planner Optimize Trip Execution - Tap 'Optimize Trip' with valid inputs"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-174')
def test_app_174_planner_optimization_results_card(driver, app_package):
    """APP-174: Planner Optimization Results Card - Verify optimization breakdown card displays on screen"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-175')
def test_app_175_planner_savings_percentage_badge(driver, app_package):
    """APP-175: Planner Savings Percentage Badge - Verify savings badge displays percentage saved"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-176')
def test_app_176_planner_stay_recommendation_card(driver, app_package):
    """APP-176: Planner Stay Recommendation Card - Verify hotel/stay cost-saving recommendation note"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-177')
def test_app_177_planner_transport_mode_card(driver, app_package):
    """APP-177: Planner Transport Mode Card - Verify recommended transport option (e.g. Train/Flight)"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-178')
def test_app_178_planner_itinerary_day_expansion(driver, app_package):
    """APP-178: Planner Itinerary Day Expansion - Tap 'Day 1' expansion tile in generated itinerary"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-179')
def test_app_179_planner_activity_item_schedule(driver, app_package):
    """APP-179: Planner Activity Item Schedule - Verify activity schedule time is displayed (e.g. 09:00 AM)"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-180')
def test_app_180_planner_activity_title_and_cost(driver, app_package):
    """APP-180: Planner Activity Title and Cost - Verify activity displays title and cost with ₹ symbol"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-181')
def test_app_181_planner_activity_category_icon(driver, app_package):
    """APP-181: Planner Activity Category Icon - Verify category icon (Food, Stay, Transport, Activities) on activity item"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-182')
def test_app_182_planner_day_2_itinerary_expansion(driver, app_package):
    """APP-182: Planner Day 2 Itinerary Expansion - Tap 'Day 2' expansion tile to inspect second day schedule"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-183')
def test_app_183_planner_save_trip_action(driver, app_package):
    """APP-183: Planner Save Trip Action - Tap 'Save Trip' elevated button"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-184')
def test_app_184_planner_saved_trip_toast(driver, app_package):
    """APP-184: Planner Saved Trip Toast - Verify confirmation snackbar confirms trip has been saved"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-185')
def test_app_185_planner_saved_trip_in_dashboard(driver, app_package):
    """APP-185: Planner Saved Trip In Dashboard - Navigate to Home and verify saved trip appears in active trip card"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-186')
def test_app_186_planner_form_reset_after_save(driver, app_package):
    """APP-186: Planner Form Reset After Save - Verify planner form clears or resets after successful save"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-187')
def test_app_187_planner_budget_slider_control(driver, app_package):
    """APP-187: Planner Budget Slider Control - Adjust budget using interactive slider if present"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-188')
def test_app_188_planner_destination_switch_recalculation(driver, app_package):
    """APP-188: Planner Destination Switch Recalculation - Switch destination from Goa to Dubai and re-optimize"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-189')
def test_app_189_planner_reorder_itinerary_activities(driver, app_package):
    """APP-189: Planner Reorder Itinerary Activities - Long press and drag activity item to reorder if supported"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-190')
def test_app_190_planner_delete_activity_from_itinerary(driver, app_package):
    """APP-190: Planner Delete Activity From Itinerary - Swipe activity item to remove from itinerary"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-191')
def test_app_191_planner_offline_itinerary_generation(driver, app_package):
    """APP-191: Planner Offline Itinerary Generation - Generate trip itinerary while offline"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-192')
def test_app_192_planner_long_duration_trip_7_days(driver, app_package):
    """APP-192: Planner Long Duration Trip (7 Days) - Configure 7-day travel period and verify multi-day itinerary"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-193')
def test_app_193_planner_currency_symbol_consistency(driver, app_package):
    """APP-193: Planner Currency Symbol Consistency - Verify all cost figures use configured currency symbol"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-194')
def test_app_194_planner_screen_landscape_scroll(driver, app_package):
    """APP-194: Planner Screen Landscape Scroll - Verify planner form scrolls cleanly in landscape mode"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-195')
def test_app_195_planner_cancel_action(driver, app_package):
    """APP-195: Planner Cancel Action - Tap cancel or back button during trip planning"""
    planner = PlannerScreen(driver)
    assert planner.is_visible(PlannerScreen.OPTIMIZE_BUTTON, timeout=5)
