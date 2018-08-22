/* jshint strict:false */

import Route from '@ember/routing/route';

export default Route.extend({
  beforeModel(transition) {
    var isAuthenticated = this.get('session.content.isAuthenticated');
    if (isAuthenticated) {
      this.transitionTo('application');
    }
  }
});
