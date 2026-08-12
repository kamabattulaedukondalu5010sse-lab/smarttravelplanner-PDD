const fs = require('fs');
const path = require('path');
const logger = require('./logger');

class ScreenshotUtils {
  static async captureScreenshot(driver, testName) {
    const failureDir = path.join(__dirname, '../reports/failures');
    if (!fs.existsSync(failureDir)) {
      fs.mkdirSync(failureDir, { recursive: true });
    }
    const cleanTestName = testName.replace(/[^a-zA-Z0-9]/g, '_');
    const filename = `${cleanTestName}_${Date.now()}.png`;
    const fullPath = path.join(failureDir, filename);

    const imageBuffer = await driver.takeScreenshot();
    fs.writeFileSync(fullPath, imageBuffer, 'base64');
    logger.info(`Screenshot captured on failure: ${fullPath}`);
    return fullPath;
  }
}

module.exports = ScreenshotUtils;
