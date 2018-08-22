import Route from '@ember/routing/route';

export default Route.extend({
  setupController() {
    this.set('userEmail', '');
  }
});
