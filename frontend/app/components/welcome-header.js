import Component from '@ember/component';
import { inject as service } from '@ember/service';

export default Component.extend({
  classNames    : ['welcome-header', 'mobile', 'text', 'centered'],
  notifications : service('notification-messages'),

  init() {
    this._super(...arguments);
  },

  actions: {
    loginToContinue() {
      this.get('notifications').clearAll();
      this.get('notifications').error('Please Login to continue', {
        autoClear     : true,
        clearDuration : 1500
      });
    }
  }
});
