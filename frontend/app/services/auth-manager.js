/* jshint strict: false */
import { observer, computed } from '@ember/object';

import { on } from '@ember/object/evented';
import Service, { inject as service } from '@ember/service';

export default Service.extend({

  session : service(),
  metrics : service(),

  currentUser: computed('session.session.content.authenticated.token', function() {
    if (this.get('session.isAuthenticated')) {
      return this.get('session.session.content.authenticated');
    }
  }),

  userAuthenticatedStatusChange: observer('session.isAuthenticated', function() {
    if (this.get('session.isAuthenticated')) {
      this.identify();
    } else {
      this.identifyStranger();
    }
  }),

  identify() {
    let currentUser = this.get('currentUser');
    this.get('metrics').identify({
      distinctId : currentUser.id,
      email      : currentUser.email,
      name       : currentUser.name
    });
  },

  identifyStranger() {
    this.get('metrics').identify(null);
  },

  _init: on('init', function() {
    if (this.get('session.isAuthenticated')) {
      this.identify();
    } else {
      this.identifyStranger();
    }
  })
});
