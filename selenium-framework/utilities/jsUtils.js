const logger = require('./logger');

class JSUtils {
  static async clickViaJS(driver, element) {
    logger.info('Performing click via JavaScript execution...');
    await driver.executeScript('arguments[0].click();', element);
  }

  static async scrollToElement(driver, element) {
    logger.info('Scrolling element into view via JS...');
    await driver.executeScript('arguments[0].scrollIntoView({ behavior: "smooth", block: "center" });', element);
  }

  static async setValueViaJS(driver, element, value) {
    logger.info(`Setting element value via JS: "${value}"`);
    await driver.executeScript('arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event("change"));', element, value);
  }

  static async getBrowserConsoleLogs(driver) {
    try {
      const logs = await driver.manage().logs().get('browser');
      return logs;
    } catch (e) {
      return [];
    }
  }
}

module.exports = JSUtils;
