const { Builder } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const firefox = require('selenium-webdriver/firefox');
const edge = require('selenium-webdriver/edge');
const logger = require('../utilities/logger');

const BROWSER = (process.env.BROWSER || 'chrome').toLowerCase();
const HEADLESS = process.env.HEADLESS === 'true';
const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';

class DriverFactory {
  static async createDriver(browserName = BROWSER, headless = HEADLESS) {
    logger.info(`Initializing ${browserName} driver (Headless: ${headless})...`);
    let builder = new Builder();

    if (browserName === 'chrome') {
      const options = new chrome.Options();
      if (headless) {
        options.addArguments('--headless=new', '--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu');
      }
      options.addArguments('--window-size=1920,1080');
      builder = builder.forBrowser('chrome').setChromeOptions(options);
    } else if (browserName === 'firefox') {
      const options = new firefox.Options();
      if (headless) {
        options.addArguments('-headless');
      }
      builder = builder.forBrowser('firefox').setFirefoxOptions(options);
    } else if (browserName === 'edge') {
      const options = new edge.Options();
      if (headless) {
        options.addArguments('--headless=new', '--no-sandbox');
      }
      builder = builder.forBrowser('MicrosoftEdge').setEdgeOptions(options);
    } else {
      throw new Error(`Unsupported browser: ${browserName}`);
    }

    const driver = await builder.build();
    await driver.manage().setTimeouts({ implicit: 10000, pageLoad: 30000, script: 30000 });
    await driver.manage().window().maximize();
    logger.info(`Browser session established for ${browserName}.`);
    return driver;
  }
}

module.exports = {
  DriverFactory,
  BROWSER,
  HEADLESS,
  BASE_URL
};
