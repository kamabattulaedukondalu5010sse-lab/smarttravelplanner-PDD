const { By } = require('selenium-webdriver');
const BasePage = require('./BasePage');

class LoginPage extends BasePage {
  constructor(driver) {
    super(driver);
    this.usernameInput = By.css('input[type="email"], input[name="email"], #username, input[name="username"]');
    this.passwordInput = By.css('input[type="password"], input[name="password"], #password');
    this.loginButton = By.css('button[type="submit"], #login-btn');
    this.logoutButton = By.css('#logout-btn, .logout-button, button:contains("Logout")');
    this.errorMessageAlert = By.css('.error-message, .alert-danger, form + div, div[style*="FEE2E2"]');
    this.dashboardHeader = By.css('h1, h2, .welcome-banner, .dashboard-title');
  }

  async login(username, password) {
    if (username !== null && username !== undefined) {
      await this.type(this.usernameInput, username);
    }
    if (password !== null && password !== undefined) {
      await this.type(this.passwordInput, password);
    }
    await this.click(this.loginButton);
  }

  async logout() {
    await this.click(this.logoutButton);
  }

  async getErrorMessage() {
    return await this.getText(this.errorMessageAlert);
  }

  async isDashboardDisplayed() {
    return await this.isElementDisplayed(this.dashboardHeader);
  }
}

module.exports = LoginPage;
