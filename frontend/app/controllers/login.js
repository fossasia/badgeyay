import Ember from 'ember';

import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session: inject.service(),
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  actions: {
    login(provider, email, password) {
      const that = this;
      if (provider === 'password') {
        this.get('session').open('firebase', {
          provider: 'password',
          email,
          password
        }).then(function(userData) {
          console.log(userData);
          that.transitionToRoute('/');
        }).catch(function(err) {
          console.log(err.message);
        });
      } else {
        const that = this;
        this.get('session').open('firebase', {
          provider
        }).then(function(userData) {
          console.log(userData);
          that.transitionToRoute('/');
        }).catch(function(err) {
          console.log(err.message);
        });
      }
    },

    logOut() {
      this.get('session').close();
    }
  }
});
