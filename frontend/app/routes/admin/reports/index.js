import Route from '@ember/routing/route';

export default Route.extend({
  templateName: 'admin/reports/list',
  beforeModel() {
    this._super(...arguments);
    this.transitionTo('admin.reports.list');
  }
});
