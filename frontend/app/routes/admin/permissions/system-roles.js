import Route from '@ember/routing/route';

export default Route.extend({
  async model() {
    return {
      'admins': await this.get('store').findAll('admin')
    };
  }
});
