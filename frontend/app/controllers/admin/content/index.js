import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  notifications : inject.service('notification-messages'),
  actions       : {
    submitForm() {
      this.set('isLoading', true);
      this.get('model')
        .save()
        .then(() => this.get('notifications').success('Update successfully', {
          autoClear     : true,
          clearDuration : 1500
        }))
        .catch(() => this.get('notifications').error('Unable to update', {
          autoClear     : true,
          clearDuration : 1500
        }))
        .finally(() => this.set('isLoading', false));
    }
  }
});
