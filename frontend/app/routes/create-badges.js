import Ember from 'ember';
import Route from '@ember/routing/route';

const { RSVP, set } = Ember;

export default Route.extend({
  beforeModel() {
    if (this.get('session.currentUser') === undefined) {
      this.transitionTo('login');
    }
  },
  model() {
    return RSVP.hash({
      def_images : this.get('store').findAll('def-image'),
<<<<<<< HEAD
      user       : this.get('store').findRecord('user', this.get('session.currentUser').uid)
=======
      user : this.get('store').findRecord('user' , this.get('session.currentUser').uid)
>>>>>>> 6e36409... Update create-badges.js
    });
  },
  setupController(controller, model) {
    this._super(...arguments);
    set(controller, 'defImages', model.def_images);
    set(controller, 'user', model.user);
    this.set('controller.badgeGenerated', false);
    this.set('controller.showProgress', false);
  }
});
