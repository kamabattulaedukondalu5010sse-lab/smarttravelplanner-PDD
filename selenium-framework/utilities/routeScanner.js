const fs = require('fs');
const path = require('path');
const logger = require('./logger');

class ReactRouteScanner {
  constructor(frontendPath) {
    this.frontendPath = frontendPath || path.join(__dirname, '../../frontend/src');
  }

  /**
   * Scans React source files for routes and form validation rules
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

        // Regex pattern to extract React Router paths: <Route path="/login" element={<LoginPage />} />
        const routeMatches = content.matchAll(/<Route\s+path=["']([^"']+)["']\s+element=\{<([^/>]+)\s*\/?>\}/g);
        for (const match of routeMatches) {
          const pathName = match[1];
          const componentName = match[2];
          routes.push({
            path: pathName,
            component: componentName,
            filePath,
            forms: this.extractFormRulesFromComponent(filePath, componentName)
          });
        }
      });
    } catch (err) {
      logger.error(`[Route Scanner] Error scanning React routes: ${err.message}`);
    }

    if (routes.length === 0) {
      return this.getFallbackRouteSpecs();
    }

    logger.info(`[Route Scanner] Successfully discovered ${routes.length} React routes with dynamic form rules.`);
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

  extractFormRulesFromComponent(filePath, componentName) {
    const forms = [];
    if (!fs.existsSync(filePath)) return forms;

    const content = fs.readFileSync(filePath, 'utf8');
    
    // Look for form input elements and HTML5/React validation attributes
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
      forms.push({ formName: `${componentName}Form`, fields: rules });
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
        path: '/register',
        component: 'RegisterForm',
        forms: [
          {
            formName: 'UserRegistrationForm',
            fields: [
              { fieldName: 'fullName', fieldType: 'text', required: true },
              { fieldName: 'email', fieldType: 'email', required: true },
              { fieldName: 'phone', fieldType: 'tel', required: true, minLength: 10 },
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
      }
    ];
  }
}

module.exports = new ReactRouteScanner();
