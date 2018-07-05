import Route from '@ember/routing/route';

export default Route.extend({
  templateName: 'admin/badges/list',
  beforeModel() {
    this._super(...arguments);
    this.transitionTo('admin.badges.list', 'all');
  }
});
