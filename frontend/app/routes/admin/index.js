import Route from '@ember/routing/route';

export default Route.extend({
  async model() {
    return {
      allBadge : await this.get('store').queryRecord('all-badge', {}),
      users    : await this.get('store').queryRecord('admin-stat-user', {}),
      mails    : await this.get('store').queryRecord('admin-stat-mail', {})
    };
  }
});
