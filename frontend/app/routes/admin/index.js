import { inject as service } from '@ember/service';
import RSVP from 'rsvp';
import { set } from '@ember/object';
import Route from '@ember/routing/route';

export default Route.extend({
  authSession: service('auth-session'),
  beforeModel() {
    if (this.get('authSession.permissions.isAdmin') === false) {
      this.transitionTo('index');
    }
  },
  async model() {
    return {
      allBadge : await this.get('store').queryRecord('all-badge', {}),
      users    : await this.get('store').queryRecord('admin-stat-user', {}),
      mails    : await this.get('store').queryRecord('admin-stat-mail', {})
    };
  }
});
