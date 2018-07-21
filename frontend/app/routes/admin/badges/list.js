import Route from '@ember/routing/route';
import Ember from 'ember';

const { set } = Ember;

export default Route.extend({
  beforeModel(transition) {
    this._super(...arguments);
  },

  model(params) {
    let filter = {};
    this.set('params', params);
    if (params.badge_status === 'all') {
      filter.state = 'all';
    } else if (params.badge_status === 'created') {
      filter.state = 'created';
    } else if (params.badge_status === 'deleted') {
      filter.state = 'deleted';
    }
    filter.page = params.page;
    return this.get('store').query('all-admin-badge', filter);
  },

  setupController(controller, model) {
    this._super(...arguments);
    set(controller, 'state', this.params.badge_status);
    set(controller, 'badges', model);
    if (model.length < 10) {
      set(controller, 'allow_prev', false);
      set(controller, 'allow_next', false);
      set(controller, 'allow', false);
    }
  }
});
