import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  session : inject.service(),
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
          }).then(record => {
            console.log(record.res);
          });
        }).catch(err => {
          console.error(err);
        });

    }
  }
});
