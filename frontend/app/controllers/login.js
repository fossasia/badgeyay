import Ember from 'ember';

import Controller from '@ember/controller';

const { inject } = Ember;

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
          if (!userObj.emailVerified) {
            this_.session.close();
            this_.notify.error('Please verify your email');
          } else {
            this_.get('store').createRecord('user', {
              uid      : userData.uid,
              username : userObj.displayName,
              email    : userObj.email,
              photoURL : userObj.photoURL
            }).save()
              .then(() => {
                this_.notify.success('Login successfull');
                this_.send('generateLoginToken', userData.uid);
              }).catch(() => {
                this_.notify.error('Unable to login');
              });
          }
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
      this.get('store').queryRecord('login-token', {
        id
      })
        .then(record => {
          this_.get('authToken').updateToken(record.token);

          let loginPayload = {
            id    : record.id,
            token : record.token
          };

          // Saving the token to persist in the device, will be deleted at logout
          localStorage.setItem('loginToken', JSON.stringify(loginPayload));

          this_.transitionToRoute('/');
          this_.get('notify').success('Log In Successful');
        })
        .catch(err => {
          this_.get('notify').error('Unable to validate user');
        });

      this.get('store').queryRecord('permission', {
        id
      })
        .then(record => {
          let permissionPayload = {
            id      : record.id,
            isUser  : record.isUser,
            isAdmin : record.isAdmin,
            isSales : record.isSales
          };

          localStorage.setItem('permissions', JSON.stringify(permissionPayload));
        })
        .catch(() => {
          this.notify.error('Unable to fetch permission');
        });
    }
  }
});
