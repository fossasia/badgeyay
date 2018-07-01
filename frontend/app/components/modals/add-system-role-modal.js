import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  actions: {
    close() {
      this.set('isOpen', false);
    },

    checkEmail() {
      let email = this.get('roleEmail');
      if (email) {
        this.get('checkEmail')(email);
      }
    },

    addSystemRole() {
      let user = this.get('userFounded');
      this.get('enableAdmin')(user, this.get('pre_checked'));
    }
  }
});
