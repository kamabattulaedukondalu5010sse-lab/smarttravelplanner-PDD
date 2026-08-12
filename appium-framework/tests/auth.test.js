const { expect } = require('chai');
const { DriverFactory } = require('../config/driver.config');
const LoginPage = require('../pages/LoginPage');
const logger = require('../utilities/logger');
const excelReporter = require('../utilities/excelReporter');

describe('React Native Android - Authentication E2E Tests', function () {
  this.timeout(180000);
  let driver;
  let loginPage;
  const startTime = Date.now();

  before(async function () {
    logger.info('Starting Authentication E2E Test Suite...');
    driver = await DriverFactory.createDriver();
    loginPage = new LoginPage(driver);
  });

  after(async function () {
    if (driver) {
      await driver.deleteSession();
      logger.info('Appium session closed.');
    }
    const duration = `${Math.round((Date.now() - startTime) / 1000)}s`;
    await excelReporter.generateReport(duration);
  });

  afterEach(async function () {
    if (this.currentTest.state === 'failed') {
      const screenshotPath = await loginPage.captureScreenshot(this.currentTest.title);
      excelReporter.addFailedTest(this.currentTest.title, this.currentTest.err.message, screenshotPath);
      excelReporter.addTestCase(`TC-AUTH-${Date.now()}`, 'Authentication', this.currentTest.title, 'FAILED', `${this.currentTest.duration || 0}ms`);
      excelReporter.addLog(this.currentTest.title, 'Test Execution', 'FAILED', this.currentTest.err.message);
    } else if (this.currentTest.state === 'passed') {
      excelReporter.addTestCase(`TC-AUTH-${Date.now()}`, 'Authentication', this.currentTest.title, 'PASSED', `${this.currentTest.duration || 0}ms`);
      excelReporter.addLog(this.currentTest.title, 'Test Execution', 'PASSED', 'Successfully executed scenario');
    }
  });

  it('TC-AUTH-01: Validate login attempt with empty credentials', async function () {
    excelReporter.addLog('TC-AUTH-01', 'Submit Empty Form', 'IN_PROGRESS', 'Entering empty username and password');
    await loginPage.login('', '');
    const errorText = await loginPage.getErrorMessageText();
    expect(errorText).to.include('Username and password are required');
  });

  it('TC-AUTH-02: Validate login attempt with invalid credentials', async function () {
    excelReporter.addLog('TC-AUTH-02', 'Submit Invalid Credentials', 'IN_PROGRESS', 'Entering invalid user/pass');
    await loginPage.login('invalid_user', 'WrongPassword123!');
    const errorText = await loginPage.getErrorMessageText();
    expect(errorText).to.include('Invalid username or password');
  });

  it('TC-AUTH-03: Validate successful login with valid credentials', async function () {
    excelReporter.addLog('TC-AUTH-03', 'Submit Valid Credentials', 'IN_PROGRESS', 'Entering valid credentials');
    await loginPage.login('admin@company.com', 'SuperSecret123!');
    const isLoggedIn = await loginPage.isLoggedIn();
    expect(isLoggedIn).to.be.true;
  });

  it('TC-AUTH-04: Validate user logout flow', async function () {
    excelReporter.addLog('TC-AUTH-04', 'Logout User', 'IN_PROGRESS', 'Tapping logout button');
    await loginPage.logout();
    const isLoggedIn = await loginPage.isLoggedIn();
    expect(isLoggedIn).to.be.false;
  });

  it('TC-AUTH-05: Validate session persistence after app restart', async function () {
    excelReporter.addLog('TC-AUTH-05', 'App Restart Session Check', 'IN_PROGRESS', 'Terminating and relaunching app');
    await loginPage.login('admin@company.com', 'SuperSecret123!');
    await driver.terminateApp('com.company.app');
    await driver.activateApp('com.company.app');
    const isLoggedIn = await loginPage.isLoggedIn();
    expect(isLoggedIn).to.be.true;
  });
});
