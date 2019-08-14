import { inject as service } from '@ember/service';

import Controller from '@ember/controller';

export default Controller.extend({
  session       : service(),
  notifications : service('notification-messages'),
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  actions: {
    logOut() {
      this.get('session').close();
      this.transitionToRoute('/');
      this.get('notifications').warning('Log Out Successful', {
        autoClear     : true,
        clearDuration : 1500
      });
    }
  }
});
