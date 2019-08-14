import { inject as service } from '@ember/service';
import Controller from '@ember/controller';

export default Controller.extend({
  session       : service(),
  notifications : service('notification-messages'),
  authToken     : service('auth-session'),
  actions       : {
    logOut() {
      this.get('store').unloadAll();
      this.get('session').close();
      this.transitionToRoute('/');
      this.get('notifications').success('Log Out Successful', {
        autoClear     : true,
        clearDuration : 1500
      });

      // Remove localStorage items
      localStorage.removeItem('adminStatus');
      localStorage.removeItem('loginToken');
      localStorage.removeItem('emailVerified');
      localStorage.removeItem('permissions');
    }
  }
});
