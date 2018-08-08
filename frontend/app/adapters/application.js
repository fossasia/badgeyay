import DS from 'ember-data';
import Ember from 'ember';
import { inject as service } from '@ember/service';

const { JSONAPIAdapter } = DS;

export default JSONAPIAdapter.extend({
  notifications: service('notification-messages'),

  isInvalid() {
    this.get('notifications').clearAll();
    this.get('notifications').error('An unexpected error occurred. Please try again later.', {
      autoClear     : true,
      clearDuration : 1500
    });
  }
});
