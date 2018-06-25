import Ember from 'ember';
import ENV from '../config/environment';
import Controller from '@ember/controller';

const { inject } = Ember;
const { APP } = ENV;

export default Controller.extend({
  session   : inject.service(),
  notify    : inject.service('notify'),
  authToken : inject.service('auth-session'),
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
          this_.send('generateLoginToken', userData.uid);
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
              this_.send('generateLoginToken', obj.id);
            })
            .catch(err => {
              console.log(err);
            });
        }).catch(function(err) {
          console.log(err.message);
          this_.get('notify').error('Log In Failed ! Please try again');
        });
      }
    },

    generateLoginToken(id) {
      const this_ = this;
      let queryPayload = {
        id
      };
      if (APP.adminAccess) {
        queryPayload.admin = true;
      }
      this.get('store').queryRecord('login-token', queryPayload)
        .then(record => {
          this_.get('authToken').updateToken(record.token);
          if (APP.adminAccess) {
            this_.get('authToken').enableAdmin();
          }
          this_.transitionToRoute('/');
          this_.get('notify').success('Log In Successful');
        })
        .catch(err => {
          this_.get('notify').error('Unable to validate user');
        });
    }
  }
});
