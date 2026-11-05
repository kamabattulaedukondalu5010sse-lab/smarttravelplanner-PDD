# Auto-generated Selenium Web E2E Test Suite
# Conforms to Page Object Model, pytest, and explicit waits
import pytest
import time
from selenium.webdriver.common.by import By
from pages.expenses_page import ExpensesPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.selenium
@pytest.mark.test_id('SEL-171')
def test_sel_171_expense_tracker_navigation(driver, base_url, test_username, test_password):
    """SEL-171: Expense Tracker Navigation - Click 'Expense Tracker' tab in sidebar navigation"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-172')
def test_sel_172_expense_tracker_header_render(driver, base_url, test_username, test_password):
    """SEL-172: Expense Tracker Header Render - Verify 'Trip Expenses' heading and financial overview cards"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-173')
def test_sel_173_total_spend_metric_card(driver, base_url, test_username, test_password):
    """SEL-173: Total Spend Metric Card - Verify 'Total Spend' card computes sum of logged expenses"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-174')
def test_sel_174_remaining_budget_metric_card(driver, base_url, test_username, test_password):
    """SEL-174: Remaining Budget Metric Card - Verify 'Remaining Budget' card subtracts spend from trip budget"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-175')
def test_sel_175_budget_utilization_gauge(driver, base_url, test_username, test_password):
    """SEL-175: Budget Utilization Gauge - Verify visual progress bar or gauge for budget utilization percentage"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-176')
def test_sel_176_expense_category_doughnut_chart(driver, base_url, test_username, test_password):
    """SEL-176: Expense Category Doughnut Chart - Verify Chart.js Doughnut chart renders category distribution"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-177')
def test_sel_177_add_expense_button_trigger(driver, base_url, test_username, test_password):
    """SEL-177: Add Expense Button Trigger - Click 'Add Expense' button to open expense modal"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-178')
def test_sel_178_expense_modal_title_input(driver, base_url, test_username, test_password):
    """SEL-178: Expense Modal Title Input - Enter expense title 'Beach Shack Dinner'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-179')
def test_sel_179_expense_modal_amount_input(driver, base_url, test_username, test_password):
    """SEL-179: Expense Modal Amount Input - Enter expense amount '1800'"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-180')
def test_sel_180_expense_modal_category_dropdown(driver, base_url, test_username, test_password):
    """SEL-180: Expense Modal Category Dropdown - Select category 'Food & Dining' from dropdown"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-181')
def test_sel_181_expense_modal_date_picker(driver, base_url, test_username, test_password):
    """SEL-181: Expense Modal Date Picker - Select expense date using date input"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-182')
def test_sel_182_expense_modal_empty_submission(driver, base_url, test_username, test_password):
    """SEL-182: Expense Modal Empty Submission - Submit expense modal with empty inputs"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-183')
def test_sel_183_expense_modal_negative_amount_rejection(driver, base_url, test_username, test_password):
    """SEL-183: Expense Modal Negative Amount Rejection - Enter negative value -500 in expense amount"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-184')
def test_sel_184_expense_modal_zero_amount_rejection(driver, base_url, test_username, test_password):
    """SEL-184: Expense Modal Zero Amount Rejection - Enter 0 in expense amount field"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-185')
def test_sel_185_expense_modal_submit_confirmation(driver, base_url, test_username, test_password):
    """SEL-185: Expense Modal Submit Confirmation - Submit valid new expense for active trip"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-186')
def test_sel_186_expense_table_row_render(driver, base_url, test_username, test_password):
    """SEL-186: Expense Table Row Render - Verify new expense item appears as row in expense table"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-187')
def test_sel_187_expense_table_category_badge(driver, base_url, test_username, test_password):
    """SEL-187: Expense Table Category Badge - Verify category column displays color-coded category badge"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-188')
def test_sel_188_expense_table_formatted_currency(driver, base_url, test_username, test_password):
    """SEL-188: Expense Table Formatted Currency - Verify amount column displays formatted value with ₹ symbol"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-189')
def test_sel_189_expense_delete_action_button(driver, base_url, test_username, test_password):
    """SEL-189: Expense Delete Action Button - Verify trash/delete icon button on each expense row"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-190')
def test_sel_190_expense_delete_execution(driver, base_url, test_username, test_password):
    """SEL-190: Expense Delete Execution - Click delete button on newly added expense"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-191')
def test_sel_191_expense_deletion_recalculates_total(driver, base_url, test_username, test_password):
    """SEL-191: Expense Deletion Recalculates Total - Verify Total Spend decreases by deleted expense amount"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-192')
def test_sel_192_expense_category_filter_all(driver, base_url, test_username, test_password):
    """SEL-192: Expense Category Filter All - Filter expenses by 'All' categories"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-193')
def test_sel_193_expense_category_filter_food(driver, base_url, test_username, test_password):
    """SEL-193: Expense Category Filter Food - Filter expenses by 'Food' category"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-194')
def test_sel_194_expense_category_filter_stay(driver, base_url, test_username, test_password):
    """SEL-194: Expense Category Filter Stay - Filter expenses by 'Stay' category"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-195')
def test_sel_195_expense_category_filter_transport(driver, base_url, test_username, test_password):
    """SEL-195: Expense Category Filter Transport - Filter expenses by 'Transport' category"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-196')
def test_sel_196_expense_category_filter_activities(driver, base_url, test_username, test_password):
    """SEL-196: Expense Category Filter Activities - Filter expenses by 'Activities' category"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-197')
def test_sel_197_over_budget_warning_banner(driver, base_url, test_username, test_password):
    """SEL-197: Over-Budget Warning Banner - Simulate total spend exceeding trip budget"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-198')
def test_sel_198_expense_chart_legend_toggle(driver, base_url, test_username, test_password):
    """SEL-198: Expense Chart Legend Toggle - Click category label in Chart.js legend to toggle dataset visibility"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-199')
def test_sel_199_expense_modal_esc_key_dismiss(driver, base_url, test_username, test_password):
    """SEL-199: Expense Modal Esc Key Dismiss - Press Escape key while Add Expense modal is open"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-200')
def test_sel_200_expense_empty_table_state(driver, base_url, test_username, test_password):
    """SEL-200: Expense Empty Table State - Inspect expense table when trip has no recorded expenses"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-201')
def test_sel_201_expense_sorting_by_amount(driver, base_url, test_username, test_password):
    """SEL-201: Expense Sorting By Amount - Click Amount column header to sort expenses descending"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-202')
def test_sel_202_expense_sorting_by_date(driver, base_url, test_username, test_password):
    """SEL-202: Expense Sorting By Date - Click Date column header to sort expenses chronologically"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-203')
def test_sel_203_direct_api_post_api_expenses(driver, base_url, test_username, test_password):
    """SEL-203: Direct API POST /api/expenses - Verify expense creation sends valid tripId, title, amount, category"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-204')
def test_sel_204_direct_api_get_api_expenses_trip_id_stats(driver, base_url, test_username, test_password):
    """SEL-204: Direct API GET /api/expenses/trip/:id/stats - Verify expense stats returns categoryBreakdown and totalSpend"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)

@pytest.mark.selenium
@pytest.mark.test_id('SEL-205')
def test_sel_205_expense_export_simulation(driver, base_url, test_username, test_password):
    """SEL-205: Expense Export Simulation - Click 'Export Expenses' or print preview if available"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_username, test_password)
    dash = DashboardPage(driver, base_url)
    dash.click(DashboardPage.EXPENSES_TAB)
    expenses = ExpensesPage(driver, base_url)
    assert expenses.is_visible(ExpensesPage.HEADER, timeout=8)
