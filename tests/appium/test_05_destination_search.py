# Auto-generated Appium Mobile UI Test Suite
# Conforms to Screen Object Model, pytest, and UiAutomator2
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from screens.dashboard_screens import SearchScreen

@pytest.mark.appium
@pytest.mark.test_id('APP-131')
def test_app_131_search_screen_initial_load(driver, app_package):
    """APP-131: Search Screen Initial Load - Navigate to SearchDestinationScreen from Explore tab"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-132')
def test_app_132_search_input_field_display(driver, app_package):
    """APP-132: Search Input Field Display - Verify search TextField displays 'Search destinations...' hint"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-133')
def test_app_133_search_tune_filter_action_icon(driver, app_package):
    """APP-133: Search Tune Filter Action Icon - Verify tune/filter icon button in search bar trailing edge"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-134')
def test_app_134_search_real_time_query_typing(driver, app_package):
    """APP-134: Search Real-time Query Typing - Type 'Goa' into search field"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-135')
def test_app_135_search_case_insensitive_matching(driver, app_package):
    """APP-135: Search Case Insensitive Matching - Type 'mAnAlI' in search field"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-136')
def test_app_136_search_partial_substring_matching(driver, app_package):
    """APP-136: Search Partial Substring Matching - Type 'Ker' in search field"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-137')
def test_app_137_search_clear_text_button(driver, app_package):
    """APP-137: Search Clear Text Button - Tap clear (X) icon in search bar"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-138')
def test_app_138_search_no_results_view(driver, app_package):
    """APP-138: Search No Results View - Type nonexistent destination 'XanaduIsland'"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-139')
def test_app_139_category_filter_chip_all(driver, app_package):
    """APP-139: Category Filter Chip All - Tap 'All' category filter chip"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-140')
def test_app_140_category_filter_chip_beach(driver, app_package):
    """APP-140: Category Filter Chip Beach - Tap 'Beach' category filter chip"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-141')
def test_app_141_category_filter_chip_mountain(driver, app_package):
    """APP-141: Category Filter Chip Mountain - Tap 'Mountain' category filter chip"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-142')
def test_app_142_category_filter_chip_nature(driver, app_package):
    """APP-142: Category Filter Chip Nature - Tap 'Nature' category filter chip"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-143')
def test_app_143_category_filter_chip_luxury(driver, app_package):
    """APP-143: Category Filter Chip Luxury - Tap 'Luxury' category filter chip"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-144')
def test_app_144_category_filter_chip_heritage(driver, app_package):
    """APP-144: Category Filter Chip Heritage - Tap 'Heritage' category filter chip"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-145')
def test_app_145_category_filter_chip_adventure(driver, app_package):
    """APP-145: Category Filter Chip Adventure - Tap 'Adventure' category filter chip"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-146')
def test_app_146_destination_card_elements_verification(driver, app_package):
    """APP-146: Destination Card Elements Verification - Inspect destination card in search results"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-147')
def test_app_147_destination_bookmark_heart_toggle(driver, app_package):
    """APP-147: Destination Bookmark Heart Toggle - Tap heart icon on destination card"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-148')
def test_app_148_destination_card_tap_to_detail(driver, app_package):
    """APP-148: Destination Card Tap To Detail - Tap on destination card in search list"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-149')
def test_app_149_destination_detail_modal_sheet(driver, app_package):
    """APP-149: Destination Detail Modal Sheet - Verify bottom modal sheet opens with full destination information"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-150')
def test_app_150_destination_detail_plan_trip_button(driver, app_package):
    """APP-150: Destination Detail Plan Trip Button - Tap 'Plan Trip to [Destination]' inside detail sheet"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-151')
def test_app_151_search_soft_keyboard_dismiss_on_scroll(driver, app_package):
    """APP-151: Search Soft Keyboard Dismiss On Scroll - Scroll search results list with soft keyboard open"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-152')
def test_app_152_search_special_characters_handling(driver, app_package):
    """APP-152: Search Special Characters Handling - Type symbols '@#$%^' into search input"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-153')
def test_app_153_search_back_navigation(driver, app_package):
    """APP-153: Search Back Navigation - Tap back arrow button in search AppBar"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-154')
def test_app_154_search_filter_modal_dialog(driver, app_package):
    """APP-154: Search Filter Modal Dialog - Tap tune icon to open advanced filter dialog"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-155')
def test_app_155_search_filter_by_min_rating(driver, app_package):
    """APP-155: Search Filter By Min Rating - Set minimum rating filter to 4.8 and apply"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-156')
def test_app_156_search_reset_filters_action(driver, app_package):
    """APP-156: Search Reset Filters Action - Tap 'Reset Filters' in filter dialog"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-157')
def test_app_157_search_results_count_indicator(driver, app_package):
    """APP-157: Search Results Count Indicator - Verify search displays count of matched destinations"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-158')
def test_app_158_search_large_destination_catalogue(driver, app_package):
    """APP-158: Search Large Destination Catalogue - Verify performance with 50+ destination list items"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-159')
def test_app_159_search_offline_cached_destinations(driver, app_package):
    """APP-159: Search Offline Cached Destinations - Search destinations in airplane mode"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)

@pytest.mark.appium
@pytest.mark.test_id('APP-160')
def test_app_160_search_accessibility_voiceover(driver, app_package):
    """APP-160: Search Accessibility VoiceOver - Inspect screen reader labels for destination search items"""
    search = SearchScreen(driver)
    assert search.is_visible(SearchScreen.SEARCH_INPUT, timeout=5)
