import Route from '@ember/routing/route';
import Ember from 'ember';

const { inject } = Ember;

export default Route.extend({
  templateName : '',
  session      : inject.service(),
  beforeModel(transition) {
    if (this.get('session.isAuthenticated')) {
      this.set('templateName', '');
    } else {
      this.set('templateName', 'not-found');
    }
  }
});
