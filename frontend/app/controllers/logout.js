import Ember from 'ember';

import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session       : inject.service(),
  notifications : inject.service('notification-messages'),
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
