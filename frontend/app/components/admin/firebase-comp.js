import Component from '@ember/component';

export default Component.extend({
  init() {
    // Variables for the greeting mail
    this.greetingMailEn = false;
    this.greetingMailVal = 'This is a sample greeting mail';
    this.greetingMailBtn = 'Modify';

    // Variables for the veriifcation mail
    this.verificationMailEn = false;
    this.verificationMailVal = 'This is a sample verification mail';
    this.verificationMailBtn = 'Modify';

    // Variables for the forgot Mail
    this.forgotMailEn = false;
    this.forgotMailVal = 'This is a sample forgot mail';
    this.forgotMailBtn = 'Modify';

    // Variables for the senderEmail
    this.senderEmail = 'senderEmail@xyz.com';
    this.senderEmailBtn = 'Modify';

    // Variables for the sender Password
    this.senderPassword = 'password';
    this.senderPasswordBtn = 'Modify';

    this._super(...arguments);
  },

  actions: {
    toggleGreetingMailEn() {
      this.set('greetingMailEn', !this.greetingMailEn);
      this.set('greetingMailBtn', this.greetingMailEn ? 'Change' : 'Modify');
    },

    toggleVerificationMailEn() {
      this.set('verificationMailEn', !this.verificationMailEn);
      this.set('verificationMailBtn', this.verificationMailEn ? 'Change' : 'Modify');
    },

    toggleForgotMailEn() {
      this.set('forgotMailEn', !this.forgotMailEn);
      this.set('forgotMailBtn', this.forgotMailEn ? 'Change' : 'Modify');
    },

    changeSenderEmail() {
    },

    changeSenderPassword() {
    }
  }
});
