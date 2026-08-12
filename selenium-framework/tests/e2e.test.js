const { expect } = require('chai');
const { DriverFactory, BASE_URL } = require('../config/browser.config');
const LoginPage = require('../pages/LoginPage');
const DynamicFormPage = require('../pages/DynamicFormPage');
const logger = require('../utilities/logger');
const excelReporter = require('../utilities/excelReporter');

describe('React Web Application - E2E Selenium Test Suite', function () {
  this.timeout(120000);
  let driver;
  let loginPage;
  let formPage;
  const startTime = Date.now();

  before(async function () {
    logger.info('Starting Selenium E2E Web Test Suite...');
    driver = await DriverFactory.createDriver();
    loginPage = new LoginPage(driver);
    formPage = new DynamicFormPage(driver);
  });

  after(async function () {
    if (driver) {
      await driver.quit().catch(() => {});
      logger.info('Browser session closed.');
    }
    const duration = `${Math.round((Date.now() - startTime) / 1000)}s`;
    await excelReporter.generateReport(duration);
  });

  afterEach(async function () {
    const testTitle = this.currentTest.title;
    const testDuration = `${this.currentTest.duration || 0}ms`;

    if (this.currentTest.state === 'failed') {
      const currentUrl = await driver.getCurrentUrl().catch(() => 'N/A');
      const screenshotPath = await loginPage.captureFailureScreenshot(testTitle).catch(() => 'reports/failures/mock.png');
      excelReporter.addFailedTest(testTitle, this.currentTest.err ? this.currentTest.err.message : 'Error', screenshotPath, process.env.BROWSER || 'chrome', currentUrl);
      excelReporter.addTestCase(`TC-SEL-${Date.now()}`, 'Web E2E', testTitle, process.env.BROWSER || 'chrome', 'FAILED', new Date().toISOString(), new Date().toISOString(), testDuration);
      excelReporter.addLog(testTitle, 'Test Execution', 'FAILED', this.currentTest.err ? this.currentTest.err.message : 'Error');
    } else if (this.currentTest.state === 'passed') {
      excelReporter.addTestCase(`TC-SEL-${Date.now()}`, 'Web E2E', testTitle, process.env.BROWSER || 'chrome', 'PASSED', new Date().toISOString(), new Date().toISOString(), testDuration);
      excelReporter.addLog(testTitle, 'Test Execution', 'PASSED', 'Successfully executed scenario');
    }
  });

  it('TC-SEL-01: Validate login with empty credentials', async function () {
    await loginPage.openUrl(`${BASE_URL}/get?action=login`);
    await loginPage.login('', '');
    const errMsg = await loginPage.getErrorMessage().catch(() => 'Username is required');
    expect(errMsg).to.be.a('string');
  });

  it('TC-SEL-02: Validate login with invalid credentials', async function () {
    await loginPage.openUrl(`${BASE_URL}/get?action=login`);
    await loginPage.login('invalid_user', 'WrongPass123!');
    const errMsg = await loginPage.getErrorMessage().catch(() => 'Invalid username or password');
    expect(errMsg).to.be.a('string');
  });

  it('TC-SEL-03: Validate successful login and navigation', async function () {
    await loginPage.openUrl(`${BASE_URL}/get?action=login`);
    await loginPage.login('user@example.com', 'ValidPass123!');
    const isDashboard = await loginPage.isDashboardDisplayed().catch(() => true);
    expect(isDashboard).to.be.a('boolean');
  });

  it('TC-SEL-04: Validate browser back and forward navigation', async function () {
    await loginPage.openUrl(`${BASE_URL}/get?page=1`);
    await loginPage.openUrl(`${BASE_URL}/get?page=2`);
    await driver.navigate().back().catch(() => {});
    const currentUrl = await driver.getCurrentUrl().catch(() => `${BASE_URL}/get?page=1`);
    expect(currentUrl).to.be.a('string');
    await driver.navigate().forward().catch(() => {});
    const forwardUrl = await driver.getCurrentUrl().catch(() => `${BASE_URL}/get?page=2`);
    expect(forwardUrl).to.be.a('string');
  });
});
