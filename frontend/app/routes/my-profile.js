import Ember from 'ember';
import Route from '@ember/routing/route';

const { RSVP, set } = Ember;

export default Route.extend({
  model() {
    return RSVP.hash({
      user: this.get('store').peekAll('user').slice(0, 1)[0]
    });
  },

  setupController(controller, model) {
    this._super(...arguments);
    set(controller, 'user', model.user);
  }
});
