const { By } = require('selenium-webdriver');
const BasePage = require('./BasePage');

class DynamicFormPage extends BasePage {
  constructor(driver) {
    super(driver);
    this.nameInput = By.name('fullName');
    this.emailInput = By.name('email');
    this.phoneInput = By.name('phone');
    this.passwordInput = By.name('password');
    this.roleDropdown = By.css('select[name="role"], #role-select');
    this.newsletterCheckbox = By.name('subscribe');
    this.submitBtn = By.css('button[type="submit"]');
    this.toastNotification = By.css('.toast-message, .alert-success');
    this.loaderSpinner = By.css('.loading-spinner, .spinner-border');
    this.modalDialog = By.css('.modal-dialog, .dialog-box');
    this.closeModalBtn = By.css('.modal-close, .btn-close');
    this.tableRows = By.css('table tbody tr');
    this.searchBar = By.css('input[type="search"], #table-search');
    this.nextPageBtn = By.css('.pagination .next-page');
  }

  async fillForm(data) {
    if (data.name) await this.type(this.nameInput, data.name);
    if (data.email) await this.type(this.emailInput, data.email);
    if (data.phone) await this.type(this.phoneInput, data.phone);
    if (data.password) await this.type(this.passwordInput, data.password);
  }

  async submit() {
    await this.click(this.submitBtn);
  }

  async getToastText() {
    return await this.getText(this.toastNotification);
  }

  async searchTable(query) {
    await this.type(this.searchBar, query);
  }

  async getTableRowCount() {
    const rows = await this.driver.findElements(this.tableRows);
    return rows.length;
  }
}

module.exports = DynamicFormPage;
