import Ember from 'ember';

import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session: inject.service(),
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  model() {
    return this.get('store').fetch('user');
  },
  actions: {
    login(provider, email, password) {
      const that = this;
      if (provider === 'password') {
        that.get('session').open('firebase', {
          provider: 'password',
          email,
          password
        }).then(function(userData) {
          let userObj = userData.currentUser;
          that.get('store').pushPayload({
            data: [{
              id         : userData.uid,
              type       : 'user',
              attributes : {
                'name'     : userObj.displayName,
                'email'    : userObj.email,
                'photoUrl' : userObj.photoURL
              },
              relationships: {}
            }]
          });
          that.transitionToRoute('/');
        }).catch(function(err) {
          console.log(err.message);
        });
      } else {
        that.get('session').open('firebase', {
          provider
        }).then(function(userData) {
          let userObj = userData.currentUser;
          that.get('store').pushPayload({
            data: [{
              id         : userData.uid,
              type       : 'user',
              attributes : {
                'name'     : userObj.displayName,
                'email'    : userObj.email,
                'photoUrl' : userObj.photoURL
              },
              relationships: {}
            }]
          });
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
