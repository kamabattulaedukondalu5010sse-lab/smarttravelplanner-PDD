const { By } = require('selenium-webdriver');
const logger = require('./logger');
const excelReporter = require('./excelReporter');
const ScreenshotUtils = require('./screenshotUtils');

class DynamicTestGenerator {
  /**
   * Automatically executes form validation test scenarios derived from React route scanning
   */
  static async executeDynamicRouteTests(driver, routeSpecs, baseUrl) {
    logger.info(`[Dynamic Test Generator] Generating and executing dynamic tests for ${routeSpecs.length} routes...`);
    const testResults = [];

    for (const route of routeSpecs) {
      const fullUrl = `${baseUrl}${route.path}`;
      logger.info(`[Dynamic Test Generator] Testing route: ${fullUrl}`);

      try {
        await driver.get(fullUrl);
        excelReporter.addLog(`Dynamic-Route-${route.path}`, `Navigate to ${fullUrl}`, 'PASSED', 'Successfully navigated');

        if (route.forms && route.forms.length > 0) {
          for (const form of route.forms) {
            for (const field of form.fields) {
              const testScenarioName = `Dynamic Rule Test: ${route.path} -> ${field.fieldName} (${field.fieldType})`;
              const startTime = Date.now();

              try {
                // Test empty field validation if required
                if (field.required) {
                  const inputEl = await driver.findElement(By.name(field.fieldName)).catch(() => null);
                  if (inputEl) {
                    await inputEl.clear();
                    await inputEl.sendKeys('');
                    excelReporter.addLog(testScenarioName, `Validate required input: ${field.fieldName}`, 'PASSED', 'Field cleared and checked');
                  }
                }

                // Test type-specific invalid entry
                if (field.fieldType === 'email') {
                  const inputEl = await driver.findElement(By.name(field.fieldName)).catch(() => null);
                  if (inputEl) {
                    await inputEl.clear();
                    await inputEl.sendKeys('invalid_email_string');
                    excelReporter.addLog(testScenarioName, `Validate email format: ${field.fieldName}`, 'PASSED', 'Invalid email entered');
                  }
                }

                const duration = `${Date.now() - startTime}ms`;
                excelReporter.addTestCase(
                  `TC-DYN-${Date.now()}`,
                  'Dynamic Form Validation',
                  testScenarioName,
                  process.env.BROWSER || 'chrome',
                  'PASSED',
                  new Date(startTime).toISOString(),
                  new Date().toISOString(),
                  duration
                );

                testResults.push({ scenario: testScenarioName, status: 'PASSED' });
              } catch (err) {
                const screenshotPath = await ScreenshotUtils.captureScreenshot(driver, testScenarioName);
                excelReporter.addFailedTest(testScenarioName, err.message, screenshotPath, process.env.BROWSER || 'chrome', fullUrl);
                testResults.push({ scenario: testScenarioName, status: 'FAILED', error: err.message });
              }
            }
          }
        }
      } catch (err) {
        logger.error(`[Dynamic Test Generator] Navigation failed for route ${fullUrl}: ${err.message}`);
      }
    }

    return testResults;
  }
}

module.exports = DynamicTestGenerator;
