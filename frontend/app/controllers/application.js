import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session       : inject.service(),
  notifications : inject.service('notification-messages'),
  authToken     : inject.service('auth-session'),
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
