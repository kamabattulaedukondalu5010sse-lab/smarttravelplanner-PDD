const { expect } = require('chai');
const { DriverFactory } = require('../config/driver.config');
const FormPage = require('../pages/FormPage');
const GestureUtils = require('../utilities/gestureUtils');
const logger = require('../utilities/logger');
const excelReporter = require('../utilities/excelReporter');

describe('React Native Android - Form & Widget Validation Suite', function () {
  this.timeout(180000);
  let driver;
  let formPage;

  before(async function () {
    driver = await DriverFactory.createDriver();
    formPage = new FormPage(driver);
  });

  after(async function () {
    if (driver) await driver.deleteSession();
  });

  afterEach(async function () {
    if (this.currentTest.state === 'failed') {
      const screenshotPath = await formPage.captureScreenshot(this.currentTest.title);
      excelReporter.addFailedTest(this.currentTest.title, this.currentTest.err.message, screenshotPath);
    }
  });

  it('TC-FORM-01: Validate required form field rules', async function () {
    await formPage.submitForm();
    const errorMsg = await formPage.getValidationError();
    expect(errorMsg).to.include('All required fields must be populated');
  });

  it('TC-FORM-02: Validate email format constraints', async function () {
    await formPage.fillForm({ email: 'invalid-email-format' });
    await formPage.submitForm();
    const errorMsg = await formPage.getValidationError();
    expect(errorMsg).to.include('Please enter a valid email address');
  });

  it('TC-FORM-03: Validate phone number format rules', async function () {
    await formPage.fillForm({ email: 'valid@company.com', phone: '123' });
    await formPage.submitForm();
    const errorMsg = await formPage.getValidationError();
    expect(errorMsg).to.include('Phone number must contain at least 10 digits');
  });

  it('TC-FORM-04: Validate password complexity & min length rules', async function () {
    await formPage.fillForm({ email: 'valid@company.com', phone: '+12345678901', password: 'abc' });
    await formPage.submitForm();
    const errorMsg = await formPage.getValidationError();
    expect(errorMsg).to.include('Password must be at least 8 characters with numbers and special symbols');
  });

  it('TC-FORM-05: Validate interactive React Native widgets (Radio, Switch, Checkbox, Gestures)', async function () {
    await formPage.selectRadio();
    await formPage.toggleSwitch();
    await GestureUtils.scroll(driver, 'down', 300);
    await formPage.fillForm({
      name: 'John Doe',
      email: 'john.doe@company.com',
      phone: '+19876543210',
      password: 'StrongPass123!@#',
      acceptTerms: true
    });
    await formPage.submitForm();
  });
});
