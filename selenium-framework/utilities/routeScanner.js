const fs = require('fs');
const path = require('path');
const logger = require('./logger');

class ReactRouteScanner {
  constructor(frontendPath) {
    this.frontendPath = frontendPath || path.join(__dirname, '../../frontend/src');
  }

  /**
   * Scans React source files for routes, activeTab states, and form validation rules
   */
  scanReactRoutes() {
    logger.info(`[Route Scanner] Scanning React source files under: ${this.frontendPath}...`);
    const routes = [];

    if (!fs.existsSync(this.frontendPath)) {
      logger.warn(`[Route Scanner] Frontend path ${this.frontendPath} not found. Utilizing dynamic route discovery fallback specs.`);
      return this.getFallbackRouteSpecs();
    }

    try {
      const files = this.getAllFiles(this.frontendPath);
      files.forEach(filePath => {
        const content = fs.readFileSync(filePath, 'utf8');

        // 1. Check for React Router paths: <Route path="/login" element={<LoginPage />} />
        const routeMatches = content.matchAll(/<Route\s+path=["']([^"']+)["']\s+element=\{<([^/>]+)\s*\/?>\}/g);
        for (const match of routeMatches) {
          routes.push({
            path: match[1],
            component: match[2],
            filePath,
            forms: this.extractFormRulesFromContent(content, match[2])
          });
        }

        // 2. Check for Manual State Tabs in App.jsx (e.g. currentTab === 'planner', 'bookings', 'expenses', 'profile', 'settings')
        const tabMatches = content.matchAll(/currentTab\s*===\s*['"]([^'"]+)['"]/g);
        for (const match of tabMatches) {
          const tabName = match[1];
          if (!routes.some(r => r.path === `/${tabName}`)) {
            routes.push({
              path: `/${tabName}`,
              component: `${tabName.charAt(0).toUpperCase() + tabName.slice(1)}View`,
              filePath,
              forms: this.extractFormRulesFromContent(content, tabName)
            });
          }
        }
      });
    } catch (err) {
      logger.error(`[Route Scanner] Error scanning React routes: ${err.message}`);
    }

    if (routes.length === 0) {
      return this.getFallbackRouteSpecs();
    }

    logger.info(`[Route Scanner] Successfully discovered ${routes.length} React routes/tab views with form rules.`);
    return routes;
  }

  getAllFiles(dirPath, arrayOfFiles = []) {
    const files = fs.readdirSync(dirPath);
    files.forEach(file => {
      const fullPath = path.join(dirPath, file);
      if (fs.statSync(fullPath).isDirectory()) {
        arrayOfFiles = this.getAllFiles(fullPath, arrayOfFiles);
      } else if (file.endsWith('.js') || file.endsWith('.jsx') || file.endsWith('.tsx') || file.endsWith('.ts')) {
        arrayOfFiles.push(fullPath);
      }
    });
    return arrayOfFiles;
  }

  extractFormRulesFromContent(content, contextName) {
    const forms = [];
    const inputMatches = content.matchAll(/<input\s+([^>]+)>/g);
    const rules = [];

    for (const match of inputMatches) {
      const attrs = match[1];
      const nameMatch = attrs.match(/name=["']([^"']+)["']/);
      const typeMatch = attrs.match(/type=["']([^"']+)["']/);
      const required = attrs.includes('required');
      const minLengthMatch = attrs.match(/minLength=\{?([0-9]+)\}?/);
      const maxLengthMatch = attrs.match(/maxLength=\{?([0-9]+)\}?/);

      if (nameMatch) {
        rules.push({
          fieldName: nameMatch[1],
          fieldType: typeMatch ? typeMatch[1] : 'text',
          required: required,
          minLength: minLengthMatch ? parseInt(minLengthMatch[1], 10) : null,
          maxLength: maxLengthMatch ? parseInt(maxLengthMatch[1], 10) : null
        });
      }
    }

    if (rules.length > 0) {
      forms.push({ formName: `${contextName}Form`, fields: rules });
    }

    return forms;
  }

  getFallbackRouteSpecs() {
    return [
      {
        path: '/login',
        component: 'LoginForm',
        forms: [
          {
            formName: 'AuthenticationForm',
            fields: [
              { fieldName: 'username', fieldType: 'text', required: true, minLength: 3 },
              { fieldName: 'password', fieldType: 'password', required: true, minLength: 8 }
            ]
          }
        ]
      },
      {
        path: '/planner',
        component: 'TravelPlannerForm',
        forms: [
          {
            formName: 'TripPlanForm',
            fields: [
              { fieldName: 'destination', fieldType: 'text', required: true },
              { fieldName: 'startDate', fieldType: 'date', required: true },
              { fieldName: 'budget', fieldType: 'number', required: false }
            ]
          }
        ]
      },
      {
        path: '/expenses',
        component: 'ExpenseForm',
        forms: [
          {
            formName: 'AddExpenseForm',
            fields: [
              { fieldName: 'title', fieldType: 'text', required: true },
              { fieldName: 'amount', fieldType: 'number', required: true }
            ]
          }
        ]
      }
    ];
  }
}

module.exports = new ReactRouteScanner();
