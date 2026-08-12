const logger = require('./logger');

class GestureUtils {
  static async tap(driver, elementOrSelector) {
    logger.info(`Performing Tap gesture...`);
    let element;
    if (typeof elementOrSelector === 'string') {
      element = await driver.$(elementOrSelector);
    } else {
      element = elementOrSelector;
    }
    await element.click();
  }

  static async doubleTap(driver, element) {
    logger.info(`Performing Double Tap gesture...`);
    const location = await element.getLocation();
    const size = await element.getSize();
    const x = location.x + size.width / 2;
    const y = location.y + size.height / 2;

    await driver.action('pointer', {
      parameters: { pointerType: 'touch' }
    })
      .move({ duration: 0, x, y })
      .down({ button: 0 })
      .up({ button: 0 })
      .pause(50)
      .down({ button: 0 })
      .up({ button: 0 })
      .perform();
  }

  static async longPress(driver, element, durationMs = 1500) {
    logger.info(`Performing Long Press gesture (${durationMs}ms)...`);
    const location = await element.getLocation();
    const size = await element.getSize();
    const x = Math.floor(location.x + size.width / 2);
    const y = Math.floor(location.y + size.height / 2);

    await driver.action('pointer', {
      parameters: { pointerType: 'touch' }
    })
      .move({ duration: 0, x, y })
      .down({ button: 0 })
      .pause(durationMs)
      .up({ button: 0 })
      .perform();
  }

  static async swipe(driver, startX, startY, endX, endY, duration = 800) {
    logger.info(`Performing Swipe from (${startX}, ${startY}) to (${endX}, ${endY})...`);
    await driver.action('pointer', {
      parameters: { pointerType: 'touch' }
    })
      .move({ duration: 0, x: startX, y: startY })
      .down({ button: 0 })
      .move({ duration, x: endX, y: endY })
      .up({ button: 0 })
      .perform();
  }

  static async scroll(driver, direction = 'down', distance = 500) {
    logger.info(`Performing Scroll ${direction}...`);
    const windowSize = await driver.getWindowSize();
    const startX = Math.floor(windowSize.width / 2);
    let startY, endY;

    if (direction === 'down') {
      startY = Math.floor(windowSize.height * 0.8);
      endY = startY - distance;
    } else {
      startY = Math.floor(windowSize.height * 0.2);
      endY = startY + distance;
    }

    await this.swipe(driver, startX, startY, startX, endY, 600);
  }

  static async dragAndDrop(driver, sourceElement, targetElement) {
    logger.info(`Performing Drag and Drop...`);
    const srcLoc = await sourceElement.getLocation();
    const srcSize = await sourceElement.getSize();
    const tgtLoc = await targetElement.getLocation();
    const tgtSize = await targetElement.getSize();

    const startX = Math.floor(srcLoc.x + srcSize.width / 2);
    const startY = Math.floor(srcLoc.y + srcSize.height / 2);
    const endX = Math.floor(tgtLoc.x + tgtSize.width / 2);
    const endY = Math.floor(tgtLoc.y + tgtSize.height / 2);

    await this.swipe(driver, startX, startY, endX, endY, 1200);
  }

  static async pinch(driver) {
    logger.info(`Performing Pinch gesture...`);
    const windowSize = await driver.getWindowSize();
    const centerX = Math.floor(windowSize.width / 2);
    const centerY = Math.floor(windowSize.height / 2);

    await driver.performActions([
      {
        type: 'pointer',
        id: 'finger1',
        parameters: { pointerType: 'touch' },
        actions: [
          { type: 'pointerMove', duration: 0, x: centerX - 200, y: centerY - 200 },
          { type: 'pointerDown', button: 0 },
          { type: 'pointerMove', duration: 600, x: centerX - 50, y: centerY - 50 },
          { type: 'pointerUp', button: 0 }
        ]
      },
      {
        type: 'pointer',
        id: 'finger2',
        parameters: { pointerType: 'touch' },
        actions: [
          { type: 'pointerMove', duration: 0, x: centerX + 200, y: centerY + 200 },
          { type: 'pointerDown', button: 0 },
          { type: 'pointerMove', duration: 600, x: centerX + 50, y: centerY + 50 },
          { type: 'pointerUp', button: 0 }
        ]
      }
    ]);
  }

  static async zoom(driver) {
    logger.info(`Performing Zoom gesture...`);
    const windowSize = await driver.getWindowSize();
    const centerX = Math.floor(windowSize.width / 2);
    const centerY = Math.floor(windowSize.height / 2);

    await driver.performActions([
      {
        type: 'pointer',
        id: 'finger1',
        parameters: { pointerType: 'touch' },
        actions: [
          { type: 'pointerMove', duration: 0, x: centerX - 50, y: centerY - 50 },
          { type: 'pointerDown', button: 0 },
          { type: 'pointerMove', duration: 600, x: centerX - 200, y: centerY - 200 },
          { type: 'pointerUp', button: 0 }
        ]
      },
      {
        type: 'pointer',
        id: 'finger2',
        parameters: { pointerType: 'touch' },
        actions: [
          { type: 'pointerMove', duration: 0, x: centerX + 50, y: centerY + 50 },
          { type: 'pointerDown', button: 0 },
          { type: 'pointerMove', duration: 600, x: centerX + 200, y: centerY + 200 },
          { type: 'pointerUp', button: 0 }
        ]
      }
    ]);
  }
}

module.exports = GestureUtils;
