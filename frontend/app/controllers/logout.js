import Ember from 'ember';

import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session : inject.service(),
  notify  : inject.service('notify'),
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  actions: {
    logOut() {
      this.get('session').close();
      this.transitionToRoute('/');
      this.get('notify').warning('Log Out Successful');
    }
  }
});
