const { By, until } = require('selenium-webdriver');
const logger = require('../utilities/logger');
const WaitUtils = require('../utilities/waitUtils');
const JSUtils = require('../utilities/jsUtils');
const ScreenshotUtils = require('../utilities/screenshotUtils');

class BasePage {
  constructor(driver) {
    this.driver = driver;
  }

  async openUrl(url) {
    logger.info(`Opening URL: ${url}`);
    await this.driver.get(url);
  }

  async getTitle() {
    return await this.driver.getTitle();
  }

  async getCurrentUrl() {
    return await this.driver.getCurrentUrl();
  }

  async findElement(locator) {
    return await WaitUtils.waitForElementVisible(this.driver, locator);
  }

  async click(locator) {
    logger.info(`Clicking element: ${locator}`);
    const el = await WaitUtils.waitForElementClickable(this.driver, locator);
    await el.click();
  }

  async type(locator, text) {
    logger.info(`Typing "${text}" into element: ${locator}`);
    const el = await this.findElement(locator);
    await el.clear();
    await el.sendKeys(text);
  }

  async getText(locator) {
    const el = await this.findElement(locator);
    const text = await el.getText();
    logger.info(`Retrieved text from ${locator}: "${text}"`);
    return text;
  }

  async isElementDisplayed(locator) {
    try {
      const el = await WaitUtils.waitForElementVisible(this.driver, locator, 3000);
      return await el.isDisplayed();
    } catch (e) {
      return false;
    }
  }

  async captureFailureScreenshot(testName) {
    return await ScreenshotUtils.captureScreenshot(this.driver, testName);
  }
}

module.exports = BasePage;
