const fs = require('fs');
const path = require('path');
const ExcelJS = require('exceljs');
const logger = require('./logger');

class ExcelReporter {
  constructor(reportFileName = 'E2E_Report.xlsx') {
    this.reportDir = path.join(__dirname, '../reports');
    if (!fs.existsSync(this.reportDir)) {
      fs.mkdirSync(this.reportDir, { recursive: true });
    }
    this.filePath = path.join(this.reportDir, reportFileName);
    this.testCases = [];
    this.failedTests = [];
    this.logs = [];
    this.summaryMeta = {
      executionDate: new Date().toISOString(),
      environment: process.env.NODE_ENV || 'staging',
      browser: process.env.BROWSER || 'chrome',
      duration: '0s'
    };
  }

  addTestCase(testId, moduleName, scenarioName, browser, status, startTime, endTime, duration) {
    this.testCases.push({
      testId,
      module: moduleName,
      scenarioName,
      browser: browser || this.summaryMeta.browser,
      status,
      startTime: startTime || new Date().toISOString(),
      endTime: endTime || new Date().toISOString(),
      duration
    });
  }

  addFailedTest(testName, failureReason, screenshotPath, browser, url) {
    this.failedTests.push({
      testName,
      failureReason,
      screenshotPath,
      browser: browser || this.summaryMeta.browser,
      url: url || 'N/A'
    });
  }

  addLog(testName, stepDescription, result, remarks) {
    this.logs.push({
      timestamp: new Date().toISOString(),
      testName,
      stepDescription,
      result,
      remarks
    });
  }

  async generateReport(totalDuration = '0s') {
    this.summaryMeta.duration = totalDuration;
    const workbook = new ExcelJS.Workbook();
    
    // Sheet 1: Summary
    const summarySheet = workbook.addWorksheet('Summary');
    summarySheet.columns = [
      { header: 'Metric', key: 'metric', width: 25 },
      { header: 'Value', key: 'value', width: 35 }
    ];

    const total = this.testCases.length;
    const passed = this.testCases.filter(t => t.status === 'PASSED').length;
    const failed = this.testCases.filter(t => t.status === 'FAILED').length;
    const skipped = this.testCases.filter(t => t.status === 'SKIPPED').length;
    const passPercentage = total > 0 ? ((passed / total) * 100).toFixed(2) + '%' : '0%';

    summarySheet.addRows([
      { metric: 'Execution Date', value: this.summaryMeta.executionDate },
      { metric: 'Environment', value: this.summaryMeta.environment },
      { metric: 'Browser', value: this.summaryMeta.browser },
      { metric: 'Total Tests', value: total },
      { metric: 'Passed', value: passed },
      { metric: 'Failed', value: failed },
      { metric: 'Skipped', value: skipped },
      { metric: 'Pass Percentage', value: passPercentage },
      { metric: 'Execution Duration', value: totalDuration }
    ]);

    // Sheet 2: Test Cases
    const tcSheet = workbook.addWorksheet('Test Cases');
    tcSheet.columns = [
      { header: 'Test ID', key: 'testId', width: 15 },
      { header: 'Module', key: 'module', width: 20 },
      { header: 'Scenario Name', key: 'scenarioName', width: 35 },
      { header: 'Browser', key: 'browser', width: 15 },
      { header: 'Status', key: 'status', width: 15 },
      { header: 'Start Time', key: 'startTime', width: 25 },
      { header: 'End Time', key: 'endTime', width: 25 },
      { header: 'Duration', key: 'duration', width: 15 }
    ];
    this.testCases.forEach(tc => tcSheet.addRow(tc));

    // Sheet 3: Failed Tests
    const failSheet = workbook.addWorksheet('Failed Tests');
    failSheet.columns = [
      { header: 'Test Name', key: 'testName', width: 30 },
      { header: 'Failure Reason', key: 'failureReason', width: 45 },
      { header: 'Screenshot Path', key: 'screenshotPath', width: 40 },
      { header: 'Browser', key: 'browser', width: 15 },
      { header: 'URL', key: 'url', width: 30 }
    ];
    this.failedTests.forEach(ft => failSheet.addRow(ft));

    // Sheet 4: Execution Logs
    const logSheet = workbook.addWorksheet('Execution Logs');
    logSheet.columns = [
      { header: 'Timestamp', key: 'timestamp', width: 25 },
      { header: 'Test Name', key: 'testName', width: 25 },
      { header: 'Step Description', key: 'stepDescription', width: 35 },
      { header: 'Result', key: 'result', width: 15 },
      { header: 'Remarks', key: 'remarks', width: 35 }
    ];
    this.logs.forEach(l => logSheet.addRow(l));

    // Style headers
    [summarySheet, tcSheet, failSheet, logSheet].forEach(sheet => {
      sheet.getRow(1).font = { bold: true, color: { argb: 'FFFFFF' } };
      sheet.getRow(1).fill = {
        type: 'pattern',
        pattern: 'solid',
        fgColor: { argb: '2E7D32' }
      };
    });

    await workbook.xlsx.writeFile(this.filePath);
    logger.info(`Selenium Excel report successfully generated at: ${this.filePath}`);
  }
}

module.exports = new ExcelReporter();
