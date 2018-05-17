/* jshint strict:false */

import Ember from 'ember';

const { Route, inject } = Ember;

export default Route.extend({
  session: inject.service(),
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  actions: {

    signIn() {
      const that = this;
      const ctrl = this.get('controller');
      this.get('session').open('firebase', {
        provider : 'password',
        email    : ctrl.get('email'),
        password : ctrl.get('password')
      }).then(function(userData) {
        console.log(userData);
        that.transitionTo('/');
      }).catch(function(err) {
        console.log(err.message);
      });
    },

    signOut() {
      this.get('session').close();
    }

  }
});
