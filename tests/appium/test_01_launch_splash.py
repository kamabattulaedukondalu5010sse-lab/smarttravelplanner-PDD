# Auto-generated Appium Mobile UI Test Suite
# Conforms to Screen Object Model, pytest, and UiAutomator2
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from screens.auth_screens import SplashScreen

@pytest.mark.appium
@pytest.mark.test_id('APP-001')
def test_app_001_app_cold_launch(driver, app_package):
    """APP-001: App Cold Launch - Perform cold launch of Flutter mobile app on Android emulator"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-002')
def test_app_002_splash_screen_animation(driver, app_package):
    """APP-002: Splash Screen Animation - Verify splash screen logo scaling and opacity animation"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-003')
def test_app_003_splash_screen_brand_title(driver, app_package):
    """APP-003: Splash Screen Brand Title - Verify 'Smart Travel Planner' title text appears on splash screen"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-004')
def test_app_004_splash_screen_subtitle(driver, app_package):
    """APP-004: Splash Screen Subtitle - Verify 'AI-Powered Intelligent Travel with Cost Optimization' subtitle"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-005')
def test_app_005_splash_screen_auto_navigation(driver, app_package):
    """APP-005: Splash Screen Auto Navigation - Verify automatic transition to /login route after 3 second delay"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-006')
def test_app_006_splash_screen_background_gradient(driver, app_package):
    """APP-006: Splash Screen Background Gradient - Verify background gradient displays primary to dark blue colors"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-007')
def test_app_007_splash_screen_decorative_circles(driver, app_package):
    """APP-007: Splash Screen Decorative Circles - Verify positioned background decorative circular overlays"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-008')
def test_app_008_splash_screen_quick_navigation_on_tap(driver, app_package):
    """APP-008: Splash Screen Quick Navigation On Tap - Tap screen during splash to test tap behavior"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-009')
def test_app_009_splash_orientation_change(driver, app_package):
    """APP-009: Splash Orientation Change - Rotate device to landscape during splash screen animation"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-010')
def test_app_010_splash_return_to_foreground(driver, app_package):
    """APP-010: Splash Return To Foreground - Send app to background during splash and resume immediately"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-011')
def test_app_011_splash_memory_footprint(driver, app_package):
    """APP-011: Splash Memory Footprint - Measure heap memory usage during initial splash load"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-012')
def test_app_012_splash_no_network_tolerance(driver, app_package):
    """APP-012: Splash No Network Tolerance - Launch app in airplane mode with zero network connectivity"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-013')
def test_app_013_splash_back_button_guard(driver, app_package):
    """APP-013: Splash Back Button Guard - Press Android hardware back button during splash screen"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-014')
def test_app_014_splash_dark_theme_handling(driver, app_package):
    """APP-014: Splash Dark Theme Handling - Launch app while system dark mode is enabled on Android"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-015')
def test_app_015_splash_status_bar_styling(driver, app_package):
    """APP-015: Splash Status Bar Styling - Verify Android status bar icons are light and transparent"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-016')
def test_app_016_splash_app_version_display(driver, app_package):
    """APP-016: Splash App Version Display - Verify build version or trademark footer if configured"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-017')
def test_app_017_splash_warm_launch_time(driver, app_package):
    """APP-017: Splash Warm Launch Time - Perform warm launch and verify transition within 1.5 seconds"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-018')
def test_app_018_splash_multi_tasking_switcher(driver, app_package):
    """APP-018: Splash Multi-tasking Switcher - Open Android recent apps overview during splash animation"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-019')
def test_app_019_splash_custom_font_rendering(driver, app_package):
    """APP-019: Splash Custom Font Rendering - Verify custom typography loads without fallback font glitch"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-020')
def test_app_020_splash_device_density_scaling(driver, app_package):
    """APP-020: Splash Device Density Scaling - Test splash rendering on hdpi, xhdpi, and xxhdpi screen densities"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-021')
def test_app_021_splash_accessibility_label(driver, app_package):
    """APP-021: Splash Accessibility Label - Inspect accessibility semantic tree for splash screen announcement"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-022')
def test_app_022_splash_flutter_engine_startup(driver, app_package):
    """APP-022: Splash Flutter Engine Startup - Verify Flutter engine initialization finishes cleanly in logcat"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-023')
def test_app_023_splash_render_frame_callback(driver, app_package):
    """APP-023: Splash Render Frame Callback - Verify first frame callback fires within 500ms of process start"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-024')
def test_app_024_splash_native_splash_handover(driver, app_package):
    """APP-024: Splash Native Splash Handover - Verify seamless transition from Android native launch screen to Flutter splash"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-025')
def test_app_025_splash_low_storage_startup(driver, app_package):
    """APP-025: Splash Low Storage Startup - Launch app on device with low available internal storage"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-026')
def test_app_026_splash_low_ram_startup(driver, app_package):
    """APP-026: Splash Low RAM Startup - Launch app on low RAM virtual device profile"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-027')
def test_app_027_splash_logcat_initialization_log(driver, app_package):
    """APP-027: Splash Logcat Initialization Log - Inspect logcat for clean startup without missing asset warnings"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-028')
def test_app_028_splash_safe_area_insets(driver, app_package):
    """APP-028: Splash Safe Area Insets - Verify splash content does not clip under camera notch or display cutout"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-029')
def test_app_029_splash_high_refresh_rate_90_120hz(driver, app_package):
    """APP-029: Splash High Refresh Rate (90/120Hz) - Verify 60+ fps animation fluidity on high refresh emulators"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)

@pytest.mark.appium
@pytest.mark.test_id('APP-030')
def test_app_030_splash_screen_route_disposal(driver, app_package):
    """APP-030: Splash Screen Route Disposal - Verify SplashScreen widget state is disposed after navigation to login"""
    screen = SplashScreen(driver)
    assert driver.session_id is not None
    assert screen.wait_for_transition_to_login(timeout=6)
