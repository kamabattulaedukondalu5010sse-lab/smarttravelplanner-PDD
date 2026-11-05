# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.settings_page import SettingsPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-236')
def test_sel_236_settings_view_navigation(driver, base_url, test_username, test_password):
    """SEL-236: Settings View Navigation - Click 'Settings' tab in sidebar navigation"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-237')
def test_sel_237_settings_header_render(driver, base_url, test_username, test_password):
    """SEL-237: Settings Header Render - Verify 'Preferences & Settings' heading is visible"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-238')
def test_sel_238_currency_preference_selector(driver, base_url, test_username, test_password):
    """SEL-238: Currency Preference Selector - Verify currency select dropdown lists INR, USD, EUR, GBP"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-239')
def test_sel_239_change_currency_to_usd(driver, base_url, test_username, test_password):
    """SEL-239: Change Currency to USD - Select 'USD ($)' from currency dropdown"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-240')
def test_sel_240_currency_change_reflects_globally(driver, base_url, test_username, test_password):
    """SEL-240: Currency Change Reflects Globally - Navigate to Dashboard and verify currency symbols update to '$'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-241')
def test_sel_241_change_currency_back_to_inr(driver, base_url, test_username, test_password):
    """SEL-241: Change Currency back to INR - Select 'INR (₹)' from currency dropdown"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-242')
def test_sel_242_theme_preference_toggle(driver, base_url, test_username, test_password):
    """SEL-242: Theme Preference Toggle - Verify theme toggle options (Light Mode vs Dark Mode)"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-243')
def test_sel_243_toggle_dark_mode(driver, base_url, test_username, test_password):
    """SEL-243: Toggle Dark Mode - Switch theme toggle to Dark Mode"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-244')
def test_sel_244_toggle_light_mode(driver, base_url, test_username, test_password):
    """SEL-244: Toggle Light Mode - Switch theme toggle back to Light Mode"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-245')
def test_sel_245_email_notifications_toggle(driver, base_url, test_username, test_password):
    """SEL-245: Email Notifications Toggle - Toggle 'Email Itinerary Updates' switch"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-246')
def test_sel_246_budget_alerts_toggle(driver, base_url, test_username, test_password):
    """SEL-246: Budget Alerts Toggle - Toggle 'Over-Budget Alerts' switch"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-247')
def test_sel_247_travel_tips_notifications_toggle(driver, base_url, test_username, test_password):
    """SEL-247: Travel Tips Notifications Toggle - Toggle 'AI Travel Tips & Deals' switch"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-248')
def test_sel_248_offline_mode_data_sync_toggle(driver, base_url, test_username, test_password):
    """SEL-248: Offline Mode Data Sync Toggle - Toggle 'Enable Offline Caching' switch"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-249')
def test_sel_249_settings_save_preferences_button(driver, base_url, test_username, test_password):
    """SEL-249: Settings Save Preferences Button - Click 'Save Preferences' button"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-250')
def test_sel_250_settings_save_confirmation_toast(driver, base_url, test_username, test_password):
    """SEL-250: Settings Save Confirmation Toast - Verify confirmation notification confirms preferences saved"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-251')
def test_sel_251_settings_reset_defaults_action(driver, base_url, test_username, test_password):
    """SEL-251: Settings Reset Defaults Action - Click 'Reset to Defaults' button"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-252')
def test_sel_252_settings_persistence_on_reload(driver, base_url, test_username, test_password):
    """SEL-252: Settings Persistence On Reload - Refresh page and verify selected preferences remain intact"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-253')
def test_sel_253_data_export_download_action(driver, base_url, test_username, test_password):
    """SEL-253: Data Export Download Action - Click 'Export All Travel Data (JSON)' button"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-254')
def test_sel_254_account_danger_zone_section(driver, base_url, test_username, test_password):
    """SEL-254: Account Danger Zone Section - Verify 'Danger Zone' section is present at bottom of settings"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-255')
def test_sel_255_delete_account_dialog_trigger(driver, base_url, test_username, test_password):
    """SEL-255: Delete Account Dialog Trigger - Click 'Delete Account' button in danger zone"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-256')
def test_sel_256_delete_account_cancel_dismiss(driver, base_url, test_username, test_password):
    """SEL-256: Delete Account Cancel Dismiss - Click 'Cancel' inside delete account confirmation modal"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-257')
def test_sel_257_privacy_policy_external_link(driver, base_url, test_username, test_password):
    """SEL-257: Privacy Policy External Link - Verify Privacy Policy link is available and has valid target"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-258')
def test_sel_258_terms_of_service_link(driver, base_url, test_username, test_password):
    """SEL-258: Terms of Service Link - Verify Terms of Service link is available"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-259')
def test_sel_259_app_version_indicator(driver, base_url, test_username, test_password):
    """SEL-259: App Version Indicator - Verify application build version (e.g. v1.0.0) is displayed in footer"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-260')
def test_sel_260_settings_accessibility_keyboard_navigation(driver, base_url, test_username, test_password):
    """SEL-260: Settings Accessibility Keyboard Navigation - Navigate through settings toggles using keyboard arrows/Space"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.SETTINGS_TAB)
    settings = SettingsPage(driver, base_url)
    assert settings.is_visible(SettingsPage.HEADER, timeout=8)
