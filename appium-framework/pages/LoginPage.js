const BasePage = require('./BasePage');

class LoginPage extends BasePage {
  // React Native Locators (Accessibility ID / ValueKey / UIAutomator)
  get usernameInput() { return '~username_field'; } // Accessibility ID / Semantics Label
  get passwordInput() { return '~password_field'; }
  get loginButton() { return '~login_button'; }
  get logoutButton() { return '~logout_button'; }
  get errorMessage() { return '~error_message'; }
  get welcomeBanner() { return '~welcome_text'; }

  async login(username, password) {
    if (username !== undefined && username !== null) {
      await this.sendKeys(this.usernameInput, username);
    }
    if (password !== undefined && password !== null) {
      await this.sendKeys(this.passwordInput, password);
    }
    await this.click(this.loginButton);
  }

  async logout() {
    await this.click(this.logoutButton);
  }

  async getErrorMessageText() {
    return await this.getText(this.errorMessage);
  }

  async isLoggedIn() {
    try {
      const el = await this.waitForElement(this.welcomeBanner, 3000);
      return await el.isDisplayed();
    } catch (err) {
      return false;
    }
  }
}

module.exports = LoginPage;
