import Controller from '@ember/controller';

import { inject as service } from '@ember/service';

export default Controller.extend({
  routing : service('-routing'),
  notify  : service('notify'),
  actions : {
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
          _this.get('notify').success('Sign Up Successful');
        })
        .catch(err => {
          let firebaseErrors = user_.get('errors.firebase');
          if (firebaseErrors !== undefined) {
            firebaseErrors.forEach(error => {
              _this.get('notify').error(error.message);
            });
          } else {
            _this.get('notify').error('Sign Up Failed ! Please try again');
          }
        });
    }
  }
});
