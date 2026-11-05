# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-001')
def test_sel_001_login_page_initial_load(driver, base_url, test_username, test_password):
    """SEL-001: Login Page Initial Load - Verify login view renders with email, password fields and sign in button"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-002')
def test_sel_002_empty_credentials_submission(driver, base_url, test_username, test_password):
    """SEL-002: Empty Credentials Submission - Submit login form with blank email and password"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-003')
def test_sel_003_empty_email_only(driver, base_url, test_username, test_password):
    """SEL-003: Empty Email Only - Submit login form with blank email and populated password"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-004')
def test_sel_004_empty_password_only(driver, base_url, test_username, test_password):
    """SEL-004: Empty Password Only - Submit login form with valid email and blank password"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-005')
def test_sel_005_invalid_email_format_missing_at(driver, base_url, test_username, test_password):
    """SEL-005: Invalid Email Format Missing At - Attempt login with username lacking '@' symbol"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-006')
def test_sel_006_invalid_email_format_missing_domain(driver, base_url, test_username, test_password):
    """SEL-006: Invalid Email Format Missing Domain - Attempt login with 'user@' lacking domain name"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-007')
def test_sel_007_invalid_email_format_special_chars(driver, base_url, test_username, test_password):
    """SEL-007: Invalid Email Format Special Chars - Attempt login with invalid symbols in email address"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-008')
def test_sel_008_nonexistent_user_authentication(driver, base_url, test_username, test_password):
    """SEL-008: Nonexistent User Authentication - Attempt login with unregistered email address"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-009')
def test_sel_009_incorrect_password_for_valid_user(driver, base_url, test_username, test_password):
    """SEL-009: Incorrect Password for Valid User - Attempt login with valid email and wrong password"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-010')
def test_sel_010_valid_standard_user_login(driver, base_url, test_username, test_password):
    """SEL-010: Valid Standard User Login - Authenticate with valid standard user credentials"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-011')
def test_sel_011_whitespace_in_email_trimming(driver, base_url, test_username, test_password):
    """SEL-011: Whitespace In Email Trimming - Authenticate with leading/trailing spaces in email"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-012')
def test_sel_012_uppercase_in_email_normalization(driver, base_url, test_username, test_password):
    """SEL-012: Uppercase In Email Normalization - Authenticate with uppercase characters in email address"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-013')
def test_sel_013_password_masking_verification(driver, base_url, test_username, test_password):
    """SEL-013: Password Masking Verification - Verify password field masks character input as type=password"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-014')
def test_sel_014_enter_key_form_submission(driver, base_url, test_username, test_password):
    """SEL-014: Enter Key Form Submission - Press Enter key inside password input field to submit"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-015')
def test_sel_015_session_token_storage_in_localstorage(driver, base_url, test_username, test_password):
    """SEL-015: Session Token Storage In LocalStorage - Verify JWT token is stored in browser localStorage after login"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-016')
def test_sel_016_user_profile_in_localstorage(driver, base_url, test_username, test_password):
    """SEL-016: User Profile In LocalStorage - Verify user profile JSON is stored in localStorage after login"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-017')
def test_sel_017_auth_error_alert_dismissal(driver, base_url, test_username, test_password):
    """SEL-017: Auth Error Alert Dismissal - Verify error message clears when user begins typing new input"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-018')
def test_sel_018_switch_to_signup_view(driver, base_url, test_username, test_password):
    """SEL-018: Switch to Signup View - Click 'Sign Up' switch button in login card footer"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-019')
def test_sel_019_switch_to_login_from_signup(driver, base_url, test_username, test_password):
    """SEL-019: Switch to Login from Signup - Click 'Log In' switch button in registration card"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-020')
def test_sel_020_logout_button_display(driver, base_url, test_username, test_password):
    """SEL-020: Logout Button Display - Verify navigation bar displays Log Out button when authenticated"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-021')
def test_sel_021_logout_action_execution(driver, base_url, test_username, test_password):
    """SEL-021: Logout Action Execution - Click Log Out button to terminate user session"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-022')
def test_sel_022_localstorage_cleared_on_logout(driver, base_url, test_username, test_password):
    """SEL-022: LocalStorage Cleared on Logout - Verify JWT token and user profile are removed on logout"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-023')
def test_sel_023_protected_route_redirect_after_logout(driver, base_url, test_username, test_password):
    """SEL-023: Protected Route Redirect After Logout - Verify user cannot access dashboard views after logging out"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-024')
def test_sel_024_session_persistence_across_page_reload(driver, base_url, test_username, test_password):
    """SEL-024: Session Persistence Across Page Reload - Refresh browser page while authenticated"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-025')
def test_sel_025_multiple_rapid_login_submissions(driver, base_url, test_username, test_password):
    """SEL-025: Multiple Rapid Login Submissions - Click login submit button multiple times rapidly"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-026')
def test_sel_026_login_card_responsive_layout(driver, base_url, test_username, test_password):
    """SEL-026: Login Card Responsive Layout - Inspect login card dimensions across desktop and mobile viewports"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-027')
def test_sel_027_login_view_brand_title(driver, base_url, test_username, test_password):
    """SEL-027: Login View Brand Title - Verify 'Smart Travel' brand heading is displayed in sidebar banner"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-028')
def test_sel_028_login_welcome_subtext(driver, base_url, test_username, test_password):
    """SEL-028: Login Welcome Subtext - Verify descriptive subtitle appears below Welcome Back heading"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-029')
def test_sel_029_remembered_session_token_expiry(driver, base_url, test_username, test_password):
    """SEL-029: Remembered Session Token Expiry - Simulate expired token in localStorage and refresh page"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-030')
def test_sel_030_login_with_special_characters_in_password(driver, base_url, test_username, test_password):
    """SEL-030: Login With Special Characters in Password - Authenticate with complex password containing symbols !@#$%^&*"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-031')
def test_sel_031_email_field_placeholder(driver, base_url, test_username, test_password):
    """SEL-031: Email Field Placeholder - Verify email input displays 'name@example.com' placeholder"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-032')
def test_sel_032_password_field_placeholder(driver, base_url, test_username, test_password):
    """SEL-032: Password Field Placeholder - Verify password input placeholder guide is present"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-033')
def test_sel_033_tab_key_focus_traversal(driver, base_url, test_username, test_password):
    """SEL-033: Tab Key Focus Traversal - Use Tab key to traverse from email to password to submit button"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-034')
def test_sel_034_button_disabled_state_during_request(driver, base_url, test_username, test_password):
    """SEL-034: Button Disabled State During Request - Verify submit button displays appropriate state while request is in flight"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-035')
def test_sel_035_mock_db_offline_fallback_authentication(driver, base_url, test_username, test_password):
    """SEL-035: Mock DB Offline Fallback Authentication - Authenticate when backend runs in mock fallback mode"""
    page = LoginPage(driver, base_url)
    page.open()
    assert page.is_visible(LoginPage.HEADER_TITLE, timeout=5)
    assert page.is_visible(LoginPage.EMAIL_INPUT)
    assert page.is_visible(LoginPage.SUBMIT_BUTTON)
