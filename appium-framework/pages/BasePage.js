const fs = require('fs');
const path = require('path');
const logger = require('../utilities/logger');

class BasePage {
  constructor(driver) {
    this.driver = driver;
  }

  async waitForElement(selector, timeoutMs = 15000) {
    logger.info(`Waiting for element: ${selector}`);
    if (Array.isArray(selector)) {
      for (const sel of selector) {
        try {
          const el = await this.driver.$(sel);
          if (await el.isDisplayed().catch(() => false)) {
            return el;
          }
        } catch (e) {}
      }
      // Fallback to first selector
      const el = await this.driver.$(selector[0]);
      await el.waitForDisplayed({ timeout: timeoutMs }).catch(() => {});
      return el;
    }
    const el = await this.driver.$(selector);
    await el.waitForDisplayed({ timeout: timeoutMs }).catch(() => {});
    return el;
  }

  async click(selector) {
    logger.info(`Clicking element: ${selector}`);
    const el = await this.waitForElement(selector);
    await el.click();
  }

  async sendKeys(selector, value) {
    logger.info(`Entering text into ${selector}: "${value}"`);
    const el = await this.waitForElement(selector);
    await el.setValue(value);
  }

  async getText(selector) {
    const el = await this.waitForElement(selector);
    const text = await el.getText();
    logger.info(`Retrieved text from ${selector}: "${text}"`);
    return text;
  }

  async captureScreenshot(testName) {
    const failureDir = path.join(__dirname, '../reports/failures');
    if (!fs.existsSync(failureDir)) {
      fs.mkdirSync(failureDir, { recursive: true });
    }
    const filename = `${testName.replace(/[^a-zA-Z0-9]/g, '_')}_${Date.now()}.png`;
    const fullPath = path.join(failureDir, filename);
    await this.driver.saveScreenshot(fullPath);
    logger.info(`Failure screenshot saved: ${fullPath}`);
    return fullPath;
  }

  async captureLogs() {
    try {
      const logs = await this.driver.getLogs('logcat').catch(() => []);
      return logs.slice(-20); // Last 20 logs
    } catch (e) {
      return [];
    }
  }
}

module.exports = BasePage;
