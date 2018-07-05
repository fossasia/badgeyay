import Route from '@ember/routing/route';
import Ember from 'ember';

const { inject } = Ember;

export default Route.extend({
  authToken: inject.service('auth-session'),
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  async model() {
    const userObj = this.get('session.currentUser');
    if (userObj !== undefined) {
      const uid = this.get('session.uid');
      const adminStatus = localStorage.getItem('adminStatus');
      if (adminStatus === 'true') {
        this.authToken.enableAdmin();
      }

      const loginToken = JSON.parse(localStorage.getItem('loginToken'));

      if (loginToken && loginToken !== undefined) {
        // Persist the login token in the cache
        this.get('store').pushPayload({
          data: [{
            id         : loginToken.id,
            type       : 'login-token',
            attributes : {
              token: loginToken.token
            }
          }]
        });

        this.authToken.updateToken(loginToken.token);
      }

      this.get('store').pushPayload({
        data: [{
          id         : uid,
          type       : 'user',
          attributes : {
            uid,
            'username' : userObj.displayName,
            'email'    : userObj.email,
            'photoURL' : userObj.photoURL
          },
          relationships: {}
        }]
      });
    }
    return {
      'socialMedia': await this.get('store').findAll('social-content')
    };
  }
});
