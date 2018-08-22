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
    if (params.users_status === 'all') {
      filter.state = 'all';
    } else if (params.users_status === 'active') {
      filter.state = 'active';
    } else if (params.users_status === 'deleted') {
      filter.state = 'deleted';
    } else {
      filter.filter = params.users_status;
      return this.get('store').query('all-user', filter);
    }
    filter.page = params.page;
    return this.get('store').query('all-user', filter);
  },

  setupController(controller, model) {
    this._super(...arguments);
    set(controller, 'state', this.params.users_status);
    if (model.length == 0) {
      set(controller, 'empty', true);
    } else {
      set(controller, 'empty', false);
    }
    set(controller, 'users', model);
    if (model.length < 10) {
      set(controller, 'allow_prev', false);
      set(controller, 'allow_next', false);
      set(controller, 'allow', false);
    }
  }
});
