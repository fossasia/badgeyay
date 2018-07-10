import Component from '@ember/component';
import Ember from 'ember';

const { inject } = Ember;

export default Component.extend({
  notify: inject.service('notify'),
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
      let adminChecked = this.get('admin_checked');
      let salesChecked = this.get('sales_checked');
      let state = this.get('state');
      if (state === 'Admin') {
        this.get('enableAdmin')(user, adminChecked);
      } else {
        this.get('enableSales')(user, salesChecked);
      }
    }
  },

  didRender() {
    this.$('.ui.form')
      .form({
        inline : true,
        delay  : false,
        fields : {
          email: {
            identifier : 'role_email',
            rules      : [
              {
                type   : 'email',
                prompt : 'Please enter a valid email address'
              }
            ]
          }
        }
      });
  }
});
