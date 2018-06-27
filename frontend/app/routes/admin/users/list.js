import Route from '@ember/routing/route';
import Ember from 'ember';

const { set } = Ember;

export default Route.extend({
  beforeModel(transition) {
    this._super(...arguments);
    const userState = transition.params[transition.targetName].users_status;
    if (!['all', 'deleted', 'active'].includes(userState)) {
      this.replaceWith('admin.users.view', userState);
    }
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
    }
    filter.page = params.page;
    return this.get('store').query('all-user', filter);
  },

  setupController(controller, model) {
    this._super(...arguments);
    set(controller, 'state', this.params.users_status);
    set(controller, 'users', model);
  }
});
