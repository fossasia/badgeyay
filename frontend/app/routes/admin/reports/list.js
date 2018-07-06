import Route from '@ember/routing/route';
import Ember from 'ember';

const { set } = Ember;

export default Route.extend({
  beforeModel(transition) {
    this._super(...arguments);
  },

  model(params) {
    let filter = {};
    filter.page = params.page;
    return this.get('store').query('admin-report', filter);
  },

  setupController(controller, model) {
    this._super(...arguments);
    set(controller, 'reports', model);
  }
});
