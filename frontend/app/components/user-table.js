import Ember from 'ember';
import Component from '@ember/component';

const { $, inject } = Ember;

export default Component.extend({
  notify    : inject.service('notify'),
  authToken : inject.service('auth-session'),
  actions   : {
    openModal(name, user) {
      $('.ui.' + name + '.modal').modal('show');
      this.set('userEdit', user);
    },

    approveModal(element, component) {
      this.get('userEdit').save()
        .then(() => {
          this.notify.success('Updated successfully');
        })
        .catch(() => {
          this.notify.error('Unable to Update User');
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
      user.destroyRecord()
        .then(() => {
          this.notify.success('Deleted successfully');
        })
        .catch(() => {
          this.notify.error('Unable to delete user');
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
