import DS from 'ember-data';
import Ember from 'ember';

const { inject } = Ember;
const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({
  authToken: inject.service('auth-session'),
  keyForAttribute(key) {
    return key;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    if (payload.data.attributes.siteAdmin === true) {
      this.authToken.enableAdmin();
      localStorage.setItem('adminStatus', true);
    } else {
      localStorage.setItem('adminStatus', false);
    }
    delete payload.data.attributes.siteAdmin;
    return this._super(...arguments);
  }
});
