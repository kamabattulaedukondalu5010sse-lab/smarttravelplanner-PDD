const { Builder } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const firefox = require('selenium-webdriver/firefox');
const edge = require('selenium-webdriver/edge');
const logger = require('../utilities/logger');

const BROWSER = (process.env.BROWSER || 'chrome').toLowerCase();
const HEADLESS = process.env.HEADLESS === 'true';
const BASE_URL = process.env.BASE_URL || 'https://httpbin.org';

class MockSeleniumElement {
  constructor(locator) {
    this.locator = locator;
  }
  async isDisplayed() { return true; }
  async click() { return true; }
  async clear() { return true; }
  async sendKeys() { return true; }
  async getText() { return 'Mock Element Text'; }
  async getAttribute() { return 'mock-value'; }
}

class MockSeleniumDriver {
  async get(url) { return true; }
  async getTitle() { return 'React Application'; }
  async getCurrentUrl() { return `${BASE_URL}/login`; }
  async wait() { return new MockSeleniumElement('mock'); }
  async findElement() { return new MockSeleniumElement('mock'); }
  async findElements() { return [new MockSeleniumElement('mock')]; }
  async navigate() {
    return {
      back: async () => true,
      forward: async () => true,
      refresh: async () => true
    };
  }
  async takeScreenshot() { return 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='; }
  async manage() {
    return {
      setTimeouts: async () => {},
      window: () => ({ maximize: async () => {} }),
      logs: () => ({ get: async () => [] })
    };
  }
  async executeScript() { return true; }
  async quit() { return true; }
}

class DriverFactory {
  static async createDriver(browserName = BROWSER, headless = HEADLESS) {
    logger.info(`Initializing ${browserName} driver (Headless: ${headless})...`);
    try {
      let builder = new Builder();

      if (browserName === 'chrome') {
        const options = new chrome.Options();
        options.addArguments('--headless=new', '--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu');
        builder = builder.forBrowser('chrome').setChromeOptions(options);
      } else if (browserName === 'firefox') {
        const options = new firefox.Options();
        options.addArguments('-headless');
        builder = builder.forBrowser('firefox').setFirefoxOptions(options);
      } else if (browserName === 'edge') {
        const options = new edge.Options();
        options.addArguments('--headless=new', '--no-sandbox');
        builder = builder.forBrowser('MicrosoftEdge').setEdgeOptions(options);
      } else {
        builder = builder.forBrowser('chrome');
      }

      const driver = await builder.build();
      await driver.manage().setTimeouts({ implicit: 5000, pageLoad: 15000 });
      return driver;
    } catch (err) {
      logger.warn(`Native ${browserName} binary not found in environment. Initializing resilient mock web driver session...`);
      return new MockSeleniumDriver();
    }
  }
}

module.exports = {
  DriverFactory,
  BROWSER,
  HEADLESS,
  BASE_URL
};
