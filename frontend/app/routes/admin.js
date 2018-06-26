import Route from '@ember/routing/route';
import Ember from 'ember';

const { inject, RSVP, set } = Ember;

export default Route.extend({
  templateName : '',
  authSession  : inject.service('auth-session'),
  beforeModel(transition) {
    if (this.get('authSession.adminValid')) {
      this.set('templateName', '');
    } else {
      this.set('templateName', 'not-found');
    }
  }
});
