import { inject as service } from '@ember/service';
import Route from '@ember/routing/route';
import ENV from '../config/environment';

const { APP } = ENV;

export default Route.extend({
  authToken: service('auth-session'),
  beforeModel() {
    return this.get('session')
      .fetch()
      .catch(function() {});
  },
  async model() {
    const userObj = this.get('session.currentUser');
    if (userObj !== undefined) {
      const uid = this.get('session.uid');
      const adminStatus = localStorage.getItem('adminStatus');
      if (adminStatus === 'true') {
        this.authToken.enableAdmin();
      }

      // Update the last login details
      fetch(APP.backLink + '/user/updateLastLogin/' + uid)
        .catch(err => console.log(err));

      const emailStatus = localStorage.getItem('emailVerified');
      if (emailStatus === 'true') {
        this.authToken.emailVerified();
      }

      const loginToken = JSON.parse(localStorage.getItem('loginToken'));

      if (loginToken && loginToken !== undefined) {
        // Persist the login token in the cache
        this.get('store').pushPayload({
          data: [
            {
              id         : loginToken.id,
              type       : 'login-token',
              attributes : {
                token: loginToken.token
              }
            }
          ]
        });

        this.authToken.updateToken(loginToken.token);
      }

      const permission = JSON.parse(localStorage.getItem('permissions'));

      if (permission && permission !== undefined) {
        // Sets the permission in service
        this.authToken.setPermission(permission);

        // Persist the permissions in the cache
        this.get('store').pushPayload({
          data: [
            {
              id         : permission.id,
              type       : 'permission',
              attributes : {
                isUser  : permission.isUser,
                isAdmin : permission.isAdmin,
                isSales : permission.isSales
              }
            }
          ]
        });
      }

      this.get('store').pushPayload({
        data: [
          {
            id         : uid,
            type       : 'user',
            attributes : {
              uid,
              username : userObj.displayName,
              email    : userObj.email,
              photoURL : userObj.photoURL
            },
            relationships: {}
          }
        ]
      });
    }
    return {
      socialMedia: await this.get('store').findAll('social-content')
    };
  }
});
