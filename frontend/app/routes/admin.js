import Route from '@ember/routing/route';
import Ember from 'ember';

const { inject, RSVP, set } = Ember;

export default Route.extend({
  templateName : '',
  authToken    : inject.service('auth-session'),
  beforeModel(transition) {
    if (this.get('authToken.adminValid')) {
      this.set('templateName', '');
    } else {
      this.set('templateName', 'not-found');
      transition.abort();
    }
  },

  model() {
    return RSVP.hash({
      users: this.get('store').query('all-user', { page: 1 })
    });
  },

  setupController(controller, model) {
    this._super(...arguments);
    set(controller, 'users', model.users);
  }
});
