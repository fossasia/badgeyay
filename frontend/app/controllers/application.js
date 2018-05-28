import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session : inject.service(),
  actions : {
    logOut() {
      this.get('store').unloadAll('user');
      this.get('session').close();
      this.transitionToRoute('/');
    }
  }
});
