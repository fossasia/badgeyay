import { inject as service } from '@ember/service';
import RSVP from 'rsvp';
import { set } from '@ember/object';
import Route from '@ember/routing/route';

export default Route.extend({
  templateName : '',
  authSession  : service('auth-session'),
  beforeModel(transition) {
    if (this.get('authSession.permissions.isAdmin')) {
      this.set('templateName', '');
    } else {
      this.set('templateName', 'not-found');
    }
  }
});
