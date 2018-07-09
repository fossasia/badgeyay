import Route from '@ember/routing/route';

export default Route.extend({
  async model() {
    return {
      'admins' : await this.get('store').query('role', { class: 'admin' }),
      'sales'  : await this.get('store').query('role', { class: 'sales' })
    };
  }
});
