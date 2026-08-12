const path = require('path');
const logger = require('../utilities/logger');

const APK_PATH = process.env.APK_PATH || path.join(__dirname, '../app/app-release.apk');
const APP_PACKAGE = process.env.APP_PACKAGE || 'com.company.app';
const APP_ACTIVITY = process.env.APP_ACTIVITY || 'com.company.app.MainActivity';
const APPIUM_HOST = process.env.APPIUM_HOST || '127.0.0.1';
const APPIUM_PORT = parseInt(process.env.APPIUM_PORT || '4723', 10);
const DEVICE_NAME = process.env.DEVICE_NAME || 'Android Emulator';
const PLATFORM_VERSION = process.env.PLATFORM_VERSION || '13.0';

const capabilities = {
  platformName: 'Android',
  'appium:automationName': 'UiAutomator2', // Primary driver for React Native Android
  'appium:deviceName': DEVICE_NAME,
  'appium:platformVersion': PLATFORM_VERSION,
  'appium:app': APK_PATH,
  'appium:appPackage': APP_PACKAGE,
  'appium:appActivity': APP_ACTIVITY,
  'appium:autoGrantPermissions': true,
  'appium:noReset': false,
  'appium:fullReset': false,
  'appium:newCommandTimeout': 300,
  'appium:ensureWebviewsHavePages': true,
  'appium:nativeWebScreenshot': true,
  'appium:connectHardwareKeyboard': true
};

const serverConfig = {
  hostname: APPIUM_HOST,
  port: APPIUM_PORT,
  path: '/',
  logLevel: 'info'
};

class DriverFactory {
  static async createDriver() {
    logger.info(`Initializing Appium 2.x session with capabilities for ${APP_PACKAGE}...`);
    const { remote } = require('webdriverio');
    const driver = await remote({
      ...serverConfig,
      capabilities
    });
    logger.info('Appium session created successfully.');
    return driver;
  }
}

module.exports = {
  capabilities,
  serverConfig,
  DriverFactory,
  APK_PATH,
  APP_PACKAGE,
  APP_ACTIVITY
};
