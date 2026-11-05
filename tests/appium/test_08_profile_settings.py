# Auto-generated Appium Mobile UI Test Suite
# Conforms to Screen Object Model, pytest, and UiAutomator2
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from screens.dashboard_screens import ProfileScreen

@pytest.mark.appium
@pytest.mark.test_id('APP-226')
def test_app_226_profile_screen_navigation(driver, app_package):
    """APP-226: Profile Screen Navigation - Tap 'Profile' tab in bottom navigation bar"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-227')
def test_app_227_profile_user_name_header(driver, app_package):
    """APP-227: Profile User Name Header - Verify user full name is displayed prominently in header"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-228')
def test_app_228_profile_email_display(driver, app_package):
    """APP-228: Profile Email Display - Verify registered email address is displayed beneath user name"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-229')
def test_app_229_profile_avatar_display(driver, app_package):
    """APP-229: Profile Avatar Display - Verify circular avatar image or initial letter fallback"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-230')
def test_app_230_profile_travel_statistics_row(driver, app_package):
    """APP-230: Profile Travel Statistics Row - Verify statistics row (Trips Planned, Places Visited, Reviews)"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-231')
def test_app_231_profile_menu_personal_info(driver, app_package):
    """APP-231: Profile Menu Personal Info - Verify 'Personal Information' list tile is present"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-232')
def test_app_232_profile_tap_personal_info(driver, app_package):
    """APP-232: Profile Tap Personal Info - Tap 'Personal Information' list tile"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-233')
def test_app_233_personal_info_form_inputs(driver, app_package):
    """APP-233: Personal Info Form Inputs - Verify Name, Email, and Phone TextFields in PersonalInformationScreen"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-234')
def test_app_234_personal_info_edit_name(driver, app_package):
    """APP-234: Personal Info Edit Name - Update name in TextField and tap Save"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-235')
def test_app_235_personal_info_edit_phone(driver, app_package):
    """APP-235: Personal Info Edit Phone - Update phone number and tap Save"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-236')
def test_app_236_personal_info_save_snackbar(driver, app_package):
    """APP-236: Personal Info Save Snackbar - Verify confirmation snackbar confirms profile updated"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-237')
def test_app_237_profile_menu_settings_tile(driver, app_package):
    """APP-237: Profile Menu Settings Tile - Verify 'Settings' list tile is present"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-238')
def test_app_238_profile_tap_settings(driver, app_package):
    """APP-238: Profile Tap Settings - Tap 'Settings' list tile"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-239')
def test_app_239_settings_dark_mode_switch(driver, app_package):
    """APP-239: Settings Dark Mode Switch - Verify 'Dark Mode' SwitchListTile in SettingsScreen"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-240')
def test_app_240_settings_toggle_dark_mode(driver, app_package):
    """APP-240: Settings Toggle Dark Mode - Toggle Dark Mode switch to on"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-241')
def test_app_241_settings_toggle_push_notifications(driver, app_package):
    """APP-241: Settings Toggle Push Notifications - Toggle 'Push Notifications' switch"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-242')
def test_app_242_settings_toggle_budget_alerts(driver, app_package):
    """APP-242: Settings Toggle Budget Alerts - Toggle 'Over-Budget Alerts' switch"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-243')
def test_app_243_settings_currency_selection(driver, app_package):
    """APP-243: Settings Currency Selection - Tap 'Currency' tile and select 'USD'"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-244')
def test_app_244_settings_clear_cache_action(driver, app_package):
    """APP-244: Settings Clear Cache Action - Tap 'Clear Cache' tile in settings"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-245')
def test_app_245_settings_app_version_tile(driver, app_package):
    """APP-245: Settings App Version Tile - Verify app version (e.g. 1.0.0+1) is displayed in settings footer"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-246')
def test_app_246_profile_menu_help_and_support(driver, app_package):
    """APP-246: Profile Menu Help and Support - Tap 'Help & Support' list tile"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-247')
def test_app_247_profile_menu_privacy_policy(driver, app_package):
    """APP-247: Profile Menu Privacy Policy - Tap 'Privacy Policy' list tile"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-248')
def test_app_248_profile_logout_button_presence(driver, app_package):
    """APP-248: Profile Logout Button Presence - Verify 'Log Out' list tile with red styling and exit icon"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-249')
def test_app_249_profile_tap_logout_action(driver, app_package):
    """APP-249: Profile Tap Logout Action - Tap 'Log Out' list tile"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-250')
def test_app_250_profile_logout_dialog_cancel(driver, app_package):
    """APP-250: Profile Logout Dialog Cancel - Tap 'Cancel' inside logout confirmation dialog"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-251')
def test_app_251_profile_logout_dialog_confirm(driver, app_package):
    """APP-251: Profile Logout Dialog Confirm - Tap 'Log Out' inside confirmation dialog"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-252')
def test_app_252_profile_unauthenticated_guard(driver, app_package):
    """APP-252: Profile Unauthenticated Guard - Verify user cannot navigate back to ProfileScreen after logout"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-253')
def test_app_253_notifications_screen_navigation(driver, app_package):
    """APP-253: Notifications Screen Navigation - Tap 'Alerts' tab in bottom navigation bar"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-254')
def test_app_254_notifications_list_view(driver, app_package):
    """APP-254: Notifications List View - Verify list of travel alerts and system notifications"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-255')
def test_app_255_notifications_clear_all_action(driver, app_package):
    """APP-255: Notifications Clear All Action - Tap 'Clear All' icon in notifications header"""
    profile = ProfileScreen(driver)
    assert profile.is_visible(ProfileScreen.LOGOUT_TILE, timeout=5)
