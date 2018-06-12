import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  actions: {
    sendResetMail() {
      this.get('sendResetMail')(this.email);
    }
  }
});
