const BasePage = require('./BasePage');

class LoginPage extends BasePage {
  // React Native Locators (Accessibility ID / ValueKey / UIAutomator)
  get usernameInput() { return ['~username_field', '//android.widget.EditText[1]', '//*[@text="Email Address"]']; }
  get passwordInput() { return ['~password_field', '//android.widget.EditText[2]', '//*[@text="Password"]']; }
  get loginButton() { return ['~login_button', '//*[@text="Login"]', '//*[@text="Log In"]']; }
  get logoutButton() { return ['~logout_button', '//*[@text="Logout"]', '//*[@text="Log Out"]']; }
  get errorMessage() { return ['~error_message', '//*[contains(@text, "Invalid credentials")]', '//*[contains(@text, "Please enter all fields")]', '//*[contains(@text, "required")]']; }
  get welcomeBanner() { return ['~welcome_text', '//*[@text="Welcome Back!"]', '//*[contains(@text, "Smart Travel")]']; }

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
