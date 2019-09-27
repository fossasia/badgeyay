import Component from '@ember/component';
import { inject as service } from '@ember/service';

export default Component.extend({
  notifications: service('notification-messages'),

  init() {
    this._super(...arguments);
  },

  actions: {
    logOut() {
      this.get('logOut')();
    },
    loginToContinue() {
      this.get('notifications').clearAll();
      this.get('notifications').error('Please Login to continue', {
        autoClear     : true,
        clearDuration : 1500
      });
    }
  }
});
