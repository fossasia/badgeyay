import Controller from '@ember/controller';

import { inject as service } from '@ember/service';

export default Controller.extend({
  routing       : service('-routing'),
  notifications : service('notification-messages'),
  actions       : {
    signUp(email, username, password) {
      const _this = this;
      let user_ = this.get('store').createRecord('user-signup', {
        email,
        username,
        password
      });
      user_.save()
        .then(record => {
          _this.transitionToRoute('/');
          _this.get('notifications').success('Sign Up Successful', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(err => {
          let firebaseErrors = user_.get('errors.firebase');
          if (firebaseErrors !== undefined) {
            firebaseErrors.forEach(error => {
              _this.get('notifications').error(error.message, {
                autoClear     : true,
                clearDuration : 1500
              });
            });
          } else {
            _this.get('notifications').error('Sign Up Failed ! Please try again', {
              autoClear     : true,
              clearDuration : 1500
            });
          }
        });
    }
  }
});
