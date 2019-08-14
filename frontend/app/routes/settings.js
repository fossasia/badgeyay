import RSVP from 'rsvp';
import { set } from '@ember/object';
import Route from '@ember/routing/route';

export default Route.extend({
  beforeModel() {
    if (this.get('session.uid') === undefined) {
      this.transitionTo('login');
    }
  },
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
