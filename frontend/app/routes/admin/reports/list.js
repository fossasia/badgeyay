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
    if (model.length < 9) {
      set(controller, 'allow_prev', false);
      set(controller, 'allow_next', false);
      set(controller, 'allow', false);
    }
  }
});
