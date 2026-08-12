const { until, By } = require('selenium-webdriver');
const logger = require('./logger');

class WaitUtils {
  static async waitForElementVisible(driver, locator, timeoutMs = 15000) {
    logger.info(`Waiting for element to be visible: ${locator}`);
    const byLocator = typeof locator === 'string' ? By.css(locator) : locator;
    const el = await driver.wait(until.elementLocated(byLocator), timeoutMs);
    await driver.wait(until.elementIsVisible(el), timeoutMs);
    return el;
  }

  static async waitForElementClickable(driver, locator, timeoutMs = 15000) {
    logger.info(`Waiting for element to be clickable: ${locator}`);
    const byLocator = typeof locator === 'string' ? By.css(locator) : locator;
    const el = await this.waitForElementVisible(driver, byLocator, timeoutMs);
    await driver.wait(until.elementIsEnabled(el), timeoutMs);
    return el;
  }

  static async waitForUrlContains(driver, text, timeoutMs = 15000) {
    logger.info(`Waiting for URL to contain: "${text}"`);
    return await driver.wait(until.urlContains(text), timeoutMs);
  }
}

module.exports = WaitUtils;
