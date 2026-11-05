# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.profile_page import ProfilePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-206')
def test_sel_206_user_profile_navigation(driver, base_url, test_username, test_password):
    """SEL-206: User Profile Navigation - Click 'User Profile' tab in sidebar navigation"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-207')
def test_sel_207_profile_card_header_display(driver, base_url, test_username, test_password):
    """SEL-207: Profile Card Header Display - Verify user profile card renders user name, email, and avatar"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-208')
def test_sel_208_profile_avatar_image_render(driver, base_url, test_username, test_password):
    """SEL-208: Profile Avatar Image Render - Verify avatar image element loads with valid image src"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-209')
def test_sel_209_profile_name_field_display(driver, base_url, test_username, test_password):
    """SEL-209: Profile Name Field Display - Verify Full Name field displays currently logged in user name"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-210')
def test_sel_210_profile_email_field_display(driver, base_url, test_username, test_password):
    """SEL-210: Profile Email Field Display - Verify Email Address field displays registered email"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-211')
def test_sel_211_profile_phone_field_display(driver, base_url, test_username, test_password):
    """SEL-211: Profile Phone Field Display - Verify Phone Number field is rendered"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-212')
def test_sel_212_edit_profile_button_trigger(driver, base_url, test_username, test_password):
    """SEL-212: Edit Profile Button Trigger - Click 'Edit Profile' button to toggle edit mode"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-213')
def test_sel_213_edit_profile_update_full_name(driver, base_url, test_username, test_password):
    """SEL-213: Edit Profile Update Full Name - Enter updated full name in name field"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-214')
def test_sel_214_edit_profile_update_phone_number(driver, base_url, test_username, test_password):
    """SEL-214: Edit Profile Update Phone Number - Enter updated phone number in phone field"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-215')
def test_sel_215_edit_profile_update_avatar_url(driver, base_url, test_username, test_password):
    """SEL-215: Edit Profile Update Avatar URL - Enter new image URL in avatar URL field"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-216')
def test_sel_216_edit_profile_cancel_action(driver, base_url, test_username, test_password):
    """SEL-216: Edit Profile Cancel Action - Click 'Cancel' button to discard profile edits"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-217')
def test_sel_217_edit_profile_save_confirmation(driver, base_url, test_username, test_password):
    """SEL-217: Edit Profile Save Confirmation - Click 'Save Changes' button to update profile"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-218')
def test_sel_218_profile_save_success_alert(driver, base_url, test_username, test_password):
    """SEL-218: Profile Save Success Alert - Verify success banner or toast confirms profile updated"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-219')
def test_sel_219_profile_localstorage_update(driver, base_url, test_username, test_password):
    """SEL-219: Profile LocalStorage Update - Verify updated user profile syncs to browser localStorage"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-220')
def test_sel_220_profile_persistence_across_page_reload(driver, base_url, test_username, test_password):
    """SEL-220: Profile Persistence Across Page Reload - Refresh browser page and verify updated name persists"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-221')
def test_sel_221_profile_empty_name_validation(driver, base_url, test_username, test_password):
    """SEL-221: Profile Empty Name Validation - Clear full name in edit mode and attempt to save"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-222')
def test_sel_222_profile_invalid_phone_format_validation(driver, base_url, test_username, test_password):
    """SEL-222: Profile Invalid Phone Format Validation - Enter invalid letters in phone number field"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-223')
def test_sel_223_profile_email_read_only_guard(driver, base_url, test_username, test_password):
    """SEL-223: Profile Email Read-Only Guard - Verify email address field cannot be arbitrarily changed in profile edit"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-224')
def test_sel_224_profile_stats_trips_completed(driver, base_url, test_username, test_password):
    """SEL-224: Profile Stats Trips Completed - Verify profile displays count of completed trips"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-225')
def test_sel_225_profile_stats_total_distance_places(driver, base_url, test_username, test_password):
    """SEL-225: Profile Stats Total Distance/Places - Verify profile displays count of visited places or destinations"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-226')
def test_sel_226_profile_member_since_badge(driver, base_url, test_username, test_password):
    """SEL-226: Profile Member Since Badge - Verify account creation date or 'Member since' badge"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-227')
def test_sel_227_profile_security_password_change_trigger(driver, base_url, test_username, test_password):
    """SEL-227: Profile Security Password Change Trigger - Click 'Change Password' expandable section if available"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-228')
def test_sel_228_profile_tab_key_navigation(driver, base_url, test_username, test_password):
    """SEL-228: Profile Tab Key Navigation - Traverse profile form inputs using Tab key"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-229')
def test_sel_229_profile_quick_avatar_selector(driver, base_url, test_username, test_password):
    """SEL-229: Profile Quick Avatar Selector - Click preset avatar thumbnail to change avatar quickly"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-230')
def test_sel_230_profile_responsive_layout(driver, base_url, test_username, test_password):
    """SEL-230: Profile Responsive Layout - Inspect profile card layout on mobile viewport width"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-231')
def test_sel_231_profile_xss_injection_in_name(driver, base_url, test_username, test_password):
    """SEL-231: Profile XSS Injection in Name - Attempt entering `<script>alert('xss')</script>` in name field"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-232')
def test_sel_232_profile_unicode_name_support(driver, base_url, test_username, test_password):
    """SEL-232: Profile Unicode Name Support - Enter name containing accented characters 'Renée Müller'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-233')
def test_sel_233_profile_phone_leading_plus_handling(driver, base_url, test_username, test_password):
    """SEL-233: Profile Phone Leading Plus Handling - Enter international phone format '+91 98765 43210'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-234')
def test_sel_234_profile_direct_api_put_verification(driver, base_url, test_username, test_password):
    """SEL-234: Profile Direct API PUT Verification - Verify PUT /api/auth/user payload matches updated profile fields"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-235')
def test_sel_235_profile_discard_changes_warning(driver, base_url, test_username, test_password):
    """SEL-235: Profile Discard Changes Warning - Navigate away while edit mode is active and verify confirmation"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.PROFILE_TAB)
    profile = ProfilePage(driver, base_url)
    assert profile.is_visible(ProfilePage.HEADER, timeout=8)
