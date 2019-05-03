import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },

  actions: {
    logOut() {
      this.get('logOut')();
    }
  }
});
