import { inject as service } from '@ember/service';
import Controller from '@ember/controller';

export default Controller.extend({
  notifications            : service('notification-messages'),
  isAddSystemRoleModalOpen : false,
  actions                  : {
    openAddSystemRoleModal(state) {
      this.set('state', state);
      this.set('isAddSystemRoleModalOpen', true);
    },

    checkEmail(email) {
      this.set('isLoading', true);
      this.get('store').queryRecord('all-user', {
        email
      }).then(recordObj => {
        this.set('roleFounded', recordObj);
      }).catch(err => {
        this.get('notifications').clearAll();
        this.get('notifications').error('Unable to find user', {
          autoClear     : true,
          clearDuration : 1500
        });
      }).finally(() => this.set('isLoading', false));
    },

    enableAdmin(user, boolFlag) {
      if (boolFlag) {
        this.get('store').createRecord('create-admin', {
          email     : user.email,
          adminStat : boolFlag
        }).save().then(() => {
          this.get('notifications').clearAll();
          this.get('notifications').success('Admin created', {
            autoClear     : true,
            clearDuration : 1500
          });
        }).catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to set admin', {
            autoClear     : true,
            clearDuration : 1500
          });
        }).finally(() => {
          this.set('isAddSystemRoleModalOpen', false);
        });
      } else {
        this.get('notifications').clearAll();
        this.get('notifications').error('Admin not enabled', {
          autoClear     : true,
          clearDuration : 1500
        });
      }
    },

    enableSales(user, boolFlag) {
      if (boolFlag) {
        this.get('store').createRecord('create-sale', {
          email     : user.email,
          salesStat : boolFlag
        }).save().then(() => {
          this.get('notifications').clearAll();
          this.get('notifications').success('Sales created', {
            autoClear     : true,
            clearDuration : 1500
          });
        }).catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to set Sales roles', {
            autoClear     : true,
            clearDuration : 1500
          });
        }).finally(() => {
          this.set('isAddSystemRoleModalOpen', false);
        });
      } else {
        this.get('notifications').clearAll();
        this.get('notifications').error('Sales not enabled', {
          autoClear     : true,
          clearDuration : 1500
        });
      }
    },

    deleteSaleRole(email) {
      this.get('store').queryRecord('delete-sale', {
        email
      }).then(() => {
        this.get('notifications').clearAll();
        this.get('notifications').success('Sales Role deleted successfully', {
          autoClear     : true,
          clearDuration : 1500
        });
      }).catch(err => {
        console.error(err);
        this.get('notifications').clearAll();
        this.get('notifications').error('Unable to delete sales role', {
          autoClear     : true,
          clearDuration : 1500
        });
      });
    },

    deleteAdmin(email) {
      this.get('store').queryRecord('delete-admin', {
        email
      }).then(() => {
        this.get('notifications').clearAll();
        this.get('notifications').success('Admin deleted successfully', {
          autoClear     : true,
          clearDuration : 1500
        });
      }).catch(err => {
        console.error(err);
        this.get('notifications').clearAll();
        this.get('notifications').error('Unable to delete admin', {
          autoClear     : true,
          clearDuration : 1500
        });
      });
    }
  }
});
