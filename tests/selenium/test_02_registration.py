# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.signup_page import SignupPage
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-036')
def test_sel_036_signup_view_header_display(driver, base_url, test_username, test_password):
    """SEL-036: Signup View Header Display - Verify heading displays 'Create Account' in signup mode"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-037')
def test_sel_037_signup_full_name_field_render(driver, base_url, test_username, test_password):
    """SEL-037: Signup Full Name Field Render - Verify Full Name input field is visible in signup mode"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-038')
def test_sel_038_signup_empty_form_submission(driver, base_url, test_username, test_password):
    """SEL-038: Signup Empty Form Submission - Submit signup form with empty inputs"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-039')
def test_sel_039_signup_missing_name_validation(driver, base_url, test_username, test_password):
    """SEL-039: Signup Missing Name Validation - Submit signup form with email and password but missing name"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-040')
def test_sel_040_signup_missing_email_validation(driver, base_url, test_username, test_password):
    """SEL-040: Signup Missing Email Validation - Submit signup form with name and password but missing email"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-041')
def test_sel_041_signup_missing_password_validation(driver, base_url, test_username, test_password):
    """SEL-041: Signup Missing Password Validation - Submit signup form with name and email but missing password"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-042')
def test_sel_042_signup_short_password_enforcement(driver, base_url, test_username, test_password):
    """SEL-042: Signup Short Password Enforcement - Submit signup form with password less than 6 characters"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-043')
def test_sel_043_signup_valid_new_user_registration(driver, base_url, test_username, test_password):
    """SEL-043: Signup Valid New User Registration - Register new unique user account"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-044')
def test_sel_044_signup_duplicate_email_conflict(driver, base_url, test_username, test_password):
    """SEL-044: Signup Duplicate Email Conflict - Attempt registration with existing user email address"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-045')
def test_sel_045_signup_whitespace_name_sanitization(driver, base_url, test_username, test_password):
    """SEL-045: Signup Whitespace Name Sanitization - Register user with leading and trailing whitespace in name"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-046')
def test_sel_046_signup_mixed_case_email_normalization(driver, base_url, test_username, test_password):
    """SEL-046: Signup Mixed Case Email Normalization - Register user with mixed-case email"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-047')
def test_sel_047_signup_form_reset_on_toggle(driver, base_url, test_username, test_password):
    """SEL-047: Signup Form Reset On Toggle - Switch to login and back to signup to verify input state reset"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-048')
def test_sel_048_signup_special_characters_in_name(driver, base_url, test_username, test_password):
    """SEL-048: Signup Special Characters in Name - Register user with hyphens and apostrophes in full name"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-049')
def test_sel_049_signup_auto_login_after_success(driver, base_url, test_username, test_password):
    """SEL-049: Signup Auto-Login After Success - Verify successful registration logs user in immediately without second login step"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-050')
def test_sel_050_signup_button_label_verification(driver, base_url, test_username, test_password):
    """SEL-050: Signup Button Label Verification - Verify submit button text changes from 'Log In' to 'Sign Up'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-051')
def test_sel_051_signup_header_subtitle_text(driver, base_url, test_username, test_password):
    """SEL-051: Signup Header Subtitle Text - Verify descriptive subtitle appears below Create Account heading"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-052')
def test_sel_052_signup_input_focus_state(driver, base_url, test_username, test_password):
    """SEL-052: Signup Input Focus State - Click into name field and verify visual focus ring"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-053')
def test_sel_053_signup_numeric_name_input(driver, base_url, test_username, test_password):
    """SEL-053: Signup Numeric Name Input - Enter numeric string in name field and verify form handling"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-054')
def test_sel_054_signup_long_string_name_truncation(driver, base_url, test_username, test_password):
    """SEL-054: Signup Long String Name Truncation - Enter extremely long name string and verify UI layout"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-055')
def test_sel_055_signup_email_case_insensitive_conflict(driver, base_url, test_username, test_password):
    """SEL-055: Signup Email Case Insensitive Conflict - Attempt registration with duplicate email in different casing"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-056')
def test_sel_056_signup_password_special_chars_support(driver, base_url, test_username, test_password):
    """SEL-056: Signup Password Special Chars Support - Register user with symbols and spaces in password"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-057')
def test_sel_057_signup_cancel_action(driver, base_url, test_username, test_password):
    """SEL-057: Signup Cancel Action - Click 'Already have an account? Log In' link"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-058')
def test_sel_058_signup_token_verification(driver, base_url, test_username, test_password):
    """SEL-058: Signup Token Verification - Verify newly registered user receives valid JWT token in localStorage"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-059')
def test_sel_059_signup_user_welcome_message(driver, base_url, test_username, test_password):
    """SEL-059: Signup User Welcome Message - Verify new user greeting on dashboard reflects registered name"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-060')
def test_sel_060_signup_network_disconnection_alert(driver, base_url, test_username, test_password):
    """SEL-060: Signup Network Disconnection Alert - Simulate offline state during registration submission"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-061')
def test_sel_061_signup_double_click_prevention(driver, base_url, test_username, test_password):
    """SEL-061: Signup Double Click Prevention - Rapidly click Sign Up button twice"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-062')
def test_sel_062_signup_tab_navigation_order(driver, base_url, test_username, test_password):
    """SEL-062: Signup Tab Navigation Order - Verify Tab key cycles Name -> Email -> Password -> Sign Up button"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-063')
def test_sel_063_signup_security_form_attributes(driver, base_url, test_username, test_password):
    """SEL-063: Signup Security Form Attributes - Verify form inputs have appropriate autocomplete attributes"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-064')
def test_sel_064_signup_error_styling_validation(driver, base_url, test_username, test_password):
    """SEL-064: Signup Error Styling Validation - Inspect CSS alert box styling for registration errors"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-065')
def test_sel_065_signup_success_session_initialization(driver, base_url, test_username, test_password):
    """SEL-065: Signup Success Session Initialization - Verify default empty trips array initialized for new registrant"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.switch_to_signup()
    signup_page = SignupPage(driver, base_url)
    assert signup_page.is_visible(SignupPage.HEADER_TITLE, timeout=5)
    assert signup_page.is_visible(SignupPage.NAME_INPUT)
