import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  notifications : inject.service('notification-messages'),
  actions       : {
    submit() {
      let modules = this.get('model');
      this.set('isLoading', true);
      modules.save()
        .then(() => {
          this.get('notifications').success('Settings have been saved successfully.', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(() => {
          this.get('notifications').error('An unexpected error has occurred. Settings not saved.', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .finally(() => {
          this.set('isLoading', false);
        });
    }
  }
});
