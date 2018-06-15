import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session : inject.service(),
  notify  : inject.service('notify'),
  actions : {
    sendResetMail(email) {
      // Get Token from backend
      const this_ = this;
      let resetUserPromise = this.get('store').createRecord('reset-user', {
        email
      });

      resetUserPromise.save()
        .then(record => {
          const { token } = record;
          // Send Token and email to cloud function
          this_.get('store').query('reset-mail', {
            token,
            email
          });
          this_.get('notify').success('Reset mail sent to ' + email);
        });
    }
  }
});
