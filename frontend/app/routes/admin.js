import Route from '@ember/routing/route';
import Ember from 'ember';

const { isEmpty, inject } = Ember;

export default Route.extend({
  session: inject.service(),
  beforeModel(transition) {
    if (isEmpty(this.get('session').get('token'))) {
      return this.transitionTo('login');
    }
  }
});
