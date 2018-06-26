import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session   : inject.service(),
  notify    : inject.service('notify'),
  authToken : inject.service('auth-session'),
  actions   : {
    logOut() {
      this.get('store').unloadAll('user');
      this.get('session').close();
      this.transitionToRoute('/');
      this.get('notify').success('Log Out Successful');
    }
  }
});
