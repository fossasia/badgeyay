import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  actions: {
    sendPwd(event) {
      event.preventDefault();
      this.get('resetPwd')(this.pwd);
    }
  }
});
