import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  notify                   : inject.service('notify'),
  isAddSystemRoleModalOpen : false,
  actions                  : {
    openAddSystemRoleModal() {
      this.set('isAddSystemRoleModalOpen', true);
    },

    checkEmail(email) {
      this.get('store').queryRecord('all-user', {
        email
      }).then(recordObj => {
        this.set('roleFounded', recordObj);
      }).catch(err => {
        this.notify.error('Unable to find user');
      });
    },

    enableAdmin(user, boolFlag) {
      this.get('store').createRecord('create-admin', {
        email     : user.email,
        adminStat : boolFlag
      }).save().then(() => {
        this.notify.success('Admin created');
      }).catch(() => {
        this.notify.error('Unable to set admin');
      }).finally(() => {
        this.set('isAddSystemRoleModalOpen', false);
      });
    }
  }
});
