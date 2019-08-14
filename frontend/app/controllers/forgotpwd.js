import { inject as service } from '@ember/service';
import Controller from '@ember/controller';

export default Controller.extend({
  session       : service(),
  notifications : service('notification-messages'),
  actions       : {
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
          _this.get('notifications').success('Reset mail sent to ' + email, {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(err => {
          let userErrors = resetUserPromise.get('errors.user');
          if (userErrors !== undefined) {
            userErrors.forEach(error => {
              _this.get('notifications').error(error.message, {
                autoClear     : true,
                clearDuration : 1500
              });
            });
          }
        });
    }
  }
});
