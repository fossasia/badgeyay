import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  notify                   : inject.service('notify'),
  isAddSystemRoleModalOpen : false,
  actions                  : {
    openAddSystemRoleModal(state) {
      this.set('state', state);
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
      if (boolFlag) {
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
      } else {
        this.notify.error('Admin not enabled');
      }
    },

    enableSales(user, boolFlag) {
      if (boolFlag) {
        this.get('store').createRecord('create-sale', {
          email     : user.email,
          salesStat : boolFlag
        }).save().then(() => {
          this.notify.success('Sales created');
        }).catch(() => {
          this.notify.error('Unable to set Sales roles');
        }).finally(() => {
          this.set('isAddSystemRoleModalOpen', false);
        });
      } else {
        this.notify.error('Sales not enabled');
      }
    },

    deleteSaleRole(email) {
      this.get('store').queryRecord('delete-sale', {
        email
      }).then(() => {
        this.notify.success('Sales Role deleted successfully');
      }).catch(err => {
        console.error(err);
        this.notify.error('Unable to delete sales role');
      });
    },

    deleteAdmin(email) {
      this.get('store').queryRecord('delete-admin', {
        email
      }).then(() => {
        this.notify.success('Admin deleted successfully');
      }).catch(err => {
        console.error(err);
        this.notify.error('Unable to delete admin');
      });
    }
  }
});
