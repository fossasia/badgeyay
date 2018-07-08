import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },


  actions: {
    updateUserPassword() {
      let password = this.get('newPassword');
      this.get('sendUserPassword')(password);
    }
  }
});
