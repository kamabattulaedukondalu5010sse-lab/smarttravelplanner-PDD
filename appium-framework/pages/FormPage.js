const BasePage = require('./BasePage');

class FormPage extends BasePage {
  get nameField() { return '~input_name'; }
  get emailField() { return '~input_email'; }
  get phoneField() { return '~input_phone'; }
  get passwordField() { return '~input_password'; }
  get termsCheckbox() { return '~checkbox_terms'; }
  get genderRadio() { return '~radio_male'; }
  get notificationSwitch() { return '~switch_notifications'; }
  get dropdownPicker() { return '~dropdown_country'; }
  get datePicker() { return '~date_picker_button'; }
  get submitButton() { return '~submit_form_button'; }
  get validationErrorMsg() { return '~validation_error_msg'; }
  get snackbarMsg() { return '~snackbar_msg'; }
  get bottomSheet() { return '~bottom_sheet_view'; }
  get tabHome() { return '~tab_home'; }
  get tabProfile() { return '~tab_profile'; }
  get drawerIcon() { return '~drawer_icon'; }

  async fillForm({ name, email, phone, password, acceptTerms = true }) {
    if (name) await this.sendKeys(this.nameField, name);
    if (email) await this.sendKeys(this.emailField, email);
    if (phone) await this.sendKeys(this.phoneField, phone);
    if (password) await this.sendKeys(this.passwordField, password);
    
    if (acceptTerms) {
      const checkbox = await this.waitForElement(this.termsCheckbox);
      const isSelected = await checkbox.getAttribute('checked');
      if (isSelected !== 'true') {
        await checkbox.click();
      }
    }
  }

  async submitForm() {
    await this.click(this.submitButton);
  }

  async getValidationError() {
    return await this.getText(this.validationErrorMsg);
  }

  async toggleSwitch() {
    await this.click(this.notificationSwitch);
  }

  async selectRadio() {
    await this.click(this.genderRadio);
  }

  async openDrawer() {
    await this.click(this.drawerIcon);
  }

  async switchTab(tab) {
    if (tab === 'home') await this.click(this.tabHome);
    if (tab === 'profile') await this.click(this.tabProfile);
  }
}

module.exports = FormPage;
