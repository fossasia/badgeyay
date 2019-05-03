import Route from '@ember/routing/route';
import Ember from 'ember';

const { inject, RSVP, set } = Ember;

export default Route.extend({
  authSession: inject.service('auth-session'),
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
