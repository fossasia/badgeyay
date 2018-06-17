import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session : inject.service(),
  notify  : inject.service('notify'),
  actions : {
    sendResetMail(email) {
      // Get Token from backend
      const _this = this;
      let resetUserPromise = this.get('store').createRecord('reset-user', {
        email
      });

      resetUserPromise.save()
        .then(record => {
          const { token } = record;
          // Send Token and email to cloud function
          _this.get('store').query('reset-mail', {
            token,
            email
          });
          _this.get('notify').success('Reset mail sent to ' + email);
        })
        .catch(err => {
          let userErrors = resetUserPromise.get('errors.user');
          if (userErrors !== undefined) {
            userErrors.forEach(error => {
              _this.get('notify').error(error.message);
            });
          }
        });
    }
  }
});
