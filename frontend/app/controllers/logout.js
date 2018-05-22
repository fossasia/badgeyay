import Ember from 'ember';

import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session: inject.service(),
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  actions: {
    logOut() {
      const that = that;
      this.get('session').close();
      that.transitionToRoute('/');
    }
  }
});
