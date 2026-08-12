const { expect } = require('chai');
const { DriverFactory, BASE_URL } = require('../config/browser.config');
const routeScanner = require('../utilities/routeScanner');
const DynamicTestGenerator = require('../utilities/dynamicTestGenerator');
const logger = require('../utilities/logger');

describe('React Web Application - Dynamic Route & Form Validation Discovery Suite', function () {
  this.timeout(180000);
  let driver;

  before(async function () {
    driver = await DriverFactory.createDriver();
  });

  after(async function () {
    if (driver) await driver.quit();
  });

  it('TC-DYN-01: Auto-scan React routes and execute dynamic form validation rules', async function () {
    logger.info('Scanning React routes automatically...');
    const discoveredRoutes = routeScanner.scanReactRoutes();
    expect(discoveredRoutes).to.be.an('array').that.is.not.empty;

    logger.info(`Discovered ${discoveredRoutes.length} React routes. Executing dynamic test generator...`);
    const results = await DynamicTestGenerator.executeDynamicRouteTests(driver, discoveredRoutes, BASE_URL);
    expect(results).to.be.an('array');
    
    results.forEach(res => {
      logger.info(`Dynamic Scenario Result [${res.scenario}]: ${res.status}`);
      expect(res.status).to.equal('PASSED');
    });
  });
});
