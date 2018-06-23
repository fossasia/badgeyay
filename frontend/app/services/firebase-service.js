import Service from '@ember/service';
import ENV from '../config/environment';

const { APP } = ENV;

export default Service.extend({

  firebaseResetMailLink : null,
  senderEmail           : null,
  senderEmailPassword   : null,
  welcomeMailTemplate   : null,

  init() {
    this._super(...arguments);
  },

  changeResetMailLink(email) {
    this.firebaseResetMailLink = email;
    APP.resetFunction = email;
  },

  changeSenderMail(email) {
    this.senderEmail = email;
  },

  changeWelcomeMailTemplate(mailBody) {
    this.set('welcomeMailTemplate', mailBody);
  },

  changeSenderPassword(pwd) {
    this.senderEmailPassword = pwd;
  }
});
