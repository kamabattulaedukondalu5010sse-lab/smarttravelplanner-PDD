const fs = require('fs');
const path = require('path');
const ExcelJS = require('exceljs');
const logger = require('./logger');

class ExcelReporter {
  constructor(reportFileName = 'React_Native_E2E_Report.xlsx') {
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
      deviceName: process.env.DEVICE_NAME || 'Android Emulator',
      androidVersion: process.env.PLATFORM_VERSION || '13.0',
      duration: '0s'
    };
  }

  addTestCase(testId, moduleName, scenario, status, duration) {
    this.testCases.push({
      testId,
      module: moduleName,
      scenario,
      status,
      device: this.summaryMeta.deviceName,
      duration
    });
  }

  addFailedTest(testName, failureReason, screenshotPath) {
    this.failedTests.push({
      testName,
      failureReason,
      screenshotPath,
      device: this.summaryMeta.deviceName,
      androidVersion: this.summaryMeta.androidVersion
    });
  }

  addLog(testName, step, result, remarks) {
    this.logs.push({
      timestamp: new Date().toISOString(),
      testName,
      step,
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
      { metric: 'Device Name', value: this.summaryMeta.deviceName },
      { metric: 'Android Version', value: this.summaryMeta.androidVersion },
      { metric: 'Total Tests', value: total },
      { metric: 'Passed', value: passed },
      { metric: 'Failed', value: failed },
      { metric: 'Skipped', value: skipped },
      { metric: 'Pass Percentage', value: passPercentage },
      { metric: 'Total Duration', value: totalDuration }
    ]);

    // Sheet 2: Test Cases
    const tcSheet = workbook.addWorksheet('Test Cases');
    tcSheet.columns = [
      { header: 'Test ID', key: 'testId', width: 15 },
      { header: 'Module', key: 'module', width: 20 },
      { header: 'Scenario', key: 'scenario', width: 35 },
      { header: 'Status', key: 'status', width: 15 },
      { header: 'Device', key: 'device', width: 25 },
      { header: 'Duration', key: 'duration', width: 15 }
    ];
    this.testCases.forEach(tc => tcSheet.addRow(tc));

    // Sheet 3: Failed Tests
    const failSheet = workbook.addWorksheet('Failed Tests');
    failSheet.columns = [
      { header: 'Test Name', key: 'testName', width: 30 },
      { header: 'Failure Reason', key: 'failureReason', width: 45 },
      { header: 'Screenshot Path', key: 'screenshotPath', width: 40 },
      { header: 'Device', key: 'device', width: 20 },
      { header: 'Android Version', key: 'androidVersion', width: 15 }
    ];
    this.failedTests.forEach(ft => failSheet.addRow(ft));

    // Sheet 4: Execution Logs
    const logSheet = workbook.addWorksheet('Execution Logs');
    logSheet.columns = [
      { header: 'Timestamp', key: 'timestamp', width: 25 },
      { header: 'Test Name', key: 'testName', width: 25 },
      { header: 'Step', key: 'step', width: 35 },
      { header: 'Result', key: 'result', width: 15 },
      { header: 'Remarks', key: 'remarks', width: 35 }
    ];
    this.logs.forEach(l => logSheet.addRow(l));

    // Apply header styling
    [summarySheet, tcSheet, failSheet, logSheet].forEach(sheet => {
      sheet.getRow(1).font = { bold: true, color: { argb: 'FFFFFF' } };
      sheet.getRow(1).fill = {
        type: 'pattern',
        pattern: 'solid',
        fgColor: { argb: '1E88E5' }
      };
    });

    await workbook.xlsx.writeFile(this.filePath);
    logger.info(`Excel report successfully generated at: ${this.filePath}`);
  }
}

module.exports = new ExcelReporter();
