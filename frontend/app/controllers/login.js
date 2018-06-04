import Ember from 'ember';

import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session : inject.service(),
  notify  : inject.service('notify'),
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  model() {
    return this.get('store').fetch('user');
  },
  actions: {
    login(provider, email, password) {
      const this_ = this;
      if (provider === 'password') {
        this_.get('session').open('firebase', {
          provider: 'password',
          email,
          password
        }).then(function(userData) {
          let userObj = userData.currentUser;
          this_.get('store').pushPayload({
            data: [{
              id         : userData.uid,
              type       : 'user',
              attributes : {
                'uid'      : userData.uid,
                'username' : userObj.displayName,
                'email'    : userObj.email,
                'photoURL' : userObj.photoURL
              },
              relationships: {}
            }]
          });
          this_.transitionToRoute('/');
          this_.get('notify').success('Log In Successful');
        }).catch(function(err) {
          console.log(err.message);
          this_.get('notify').error('Log In Failed ! Please try again');
        });
      } else {
        this_.get('session').open('firebase', {
          provider
        }).then(function(userData) {
          let userObj = userData.currentUser;
          let user_ = this_.get('store').createRecord('user', {
            uid      : userData.uid,
            username : userObj.displayName,
            email    : userObj.email,
            photoURL : userObj.photoURL
          });
          user_.save()
            .then(obj => {
              this_.transitionToRoute('/');
              this_.get('notify').success('Log In Successful');
            })
            .catch(err => {
              console.log(err);
            });
        }).catch(function(err) {
          console.log(err.message);
          this_.get('notify').error('Log In Failed ! Please try again');
        });
      }
    }
  }
});
