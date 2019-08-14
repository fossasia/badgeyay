import { inject as service } from '@ember/service';
import $ from 'jquery';

import Controller from '@ember/controller';

export default Controller.extend({
  session       : service(),
  notifications : service('notification-messages'),
  authToken     : service('auth-session'),
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
          if (userObj.emailVerified) {
            localStorage.setItem('emailVerified', true);
            this_.authToken.emailVerified();
          } else {
            localStorage.setItem('emailVerified', false);
          }
          this_.get('store').createRecord('user', {
            uid      : userData.uid,
            username : userObj.displayName,
            email    : userObj.email,
            photoURL : userObj.photoURL
          }).save()
            .then(() => {
              this_.send('generateLoginToken', userData.uid);
            }).catch(() => {
              this_.get('notifications').error('Unable to login', {
                autoClear     : true,
                clearDuration : 1500
              });
            });
        }).catch(function(err) {
          console.log(err.message);
          this_.get('notifications').clearAll();
          this_.notifications.error('Log In Failed ! Please try again', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
      } else {
        this_.get('session').open('firebase', {
          provider
        }).then(function(userData) {
          let userObj = userData.currentUser;
          localStorage.setItem('emailVerified', true);
          this_.authToken.emailVerified();
          let user_ = this_.get('store').createRecord('user', {
            uid      : userData.uid,
            username : userObj.displayName,
            email    : userObj.email,
            photoURL : userObj.photoURL
          });
          user_.save()
            .then(obj => {
              this_.set('userLoggedIn', obj);
              if (obj.password === null) {
                $('.ui.passwordForm.modal').modal('show');
              } else {
                this_.send('generateLoginToken', obj.id);
              }
            })
            .catch(err => {
              console.log(err);
            });
        }).catch(function(err) {
          console.log(err.message);
          this_.get('notifications').clearAll();
          this_.notifications.error('Log In Failed ! Please try again', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
      }
    },

    denyModal(element, component) {
      this.session.close();
      this.get('notifications').clearAll();
      this.get('notifications').error('Please set your password', {
        autoClear     : true,
        clearDuration : 1500
      });
      return true;
    },

    approveModal(element, component) {
      let formPassword = this.get('formPassword');
      let confirmPassword = this.get('formConfirmPassword');
      if (formPassword !== null && confirmPassword !== null && formPassword === confirmPassword) {
        this.get('userLoggedIn')
          .set('password', formPassword);
        this.set('isDimmerVisible', true);
        this.set('loaderText', 'Setting Password');
        this.get('userLoggedIn')
          .save()
          .then(obj => this.send('generateLoginToken', obj.id))
          .catch(() => this.notifications.error('Unable to save password', {
            autoClear     : true,
            clearDuration : 1500
          }))
          .finally(() => { return true });
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

          this.set('isDimmerVisible', false);

          // Saving the token to persist in the device, will be deleted at logout
          localStorage.setItem('loginToken', JSON.stringify(loginPayload));

          this_.transitionToRoute('/');
          this_.get('notifications').clearAll();
          this_.get('notifications').success('Log In Successful', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(err => {
          this_.get('notifications').clearAll();
          this_.get('notifications').error('Unable to validate user', {
            autoClear     : true,
            clearDuration : 1500
          });
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
          this.authToken.setPermission(permissionPayload);
        })
        .catch(() => {
          this.notifications.error('Unable to fetch permission', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
    }
  }
});
