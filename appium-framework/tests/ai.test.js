const { expect } = require('chai');
const { DriverFactory } = require('../config/driver.config');
const SmartAITester = require('../utilities/aiTester');
const logger = require('../utilities/logger');

describe('React Native Android - Smart AI Automated Testing Suite', function () {
  this.timeout(180000);
  let driver;
  let aiTester;

  before(async function () {
    driver = await DriverFactory.createDriver();
    aiTester = new SmartAITester(driver);
  });

  after(async function () {
    if (driver) await driver.deleteSession();
  });

  it('TC-AI-01: Auto-discover React Native screen widgets and generate scenarios', async function () {
    logger.info('Running AI Screen Analysis...');
    const widgets = await aiTester.analyzeScreen();
    expect(widgets).to.be.an('array');

    logger.info('Executing AI-generated dynamic test scenarios...');
    const results = await aiTester.executeAutoTests();
    expect(results).to.be.an('array');
    results.forEach(res => {
      logger.info(`AI Scenario Result [${res.scenario}]: ${res.status}`);
      expect(res.status).to.equal('PASSED');
    });
  });
});
