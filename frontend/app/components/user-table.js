import Ember from 'ember';
import Component from '@ember/component';

const { $, inject } = Ember;

export default Component.extend({
  notifications : inject.service('notification-messages'),
  authToken     : inject.service('auth-session'),
  actions       : {
    openModal(name, user) {
      $('.ui.' + name + '.modal').modal('show');
      this.set('userEdit', user);
    },

    initModal(name, user) {
      $('.ui.' + name + '.modal').modal('show');
      this.set('userDelete', user);
    },

    approveModal(element, component) {
      this.get('userEdit').save()
        .then(() => {
          this.get('notifications').clearAll();
          this.get('notifications').success('Updated successfully', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to Update User', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .finally(() => {
          return true;
        });
      return true;
    },

    denyModal(element, component) {
      return true;
    },

    deleteUser(user) {
      this.get('userDelete').destroyRecord()
        .then(() => {
          this.get('notifications').clearAll();
          this.get('notifications').success('Deleted successfully', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to delete user', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
    },

    nextPage() {
      this.get('nextPage')();
    },

    prevPage() {
      this.get('prevPage')();
    }
  }
});
