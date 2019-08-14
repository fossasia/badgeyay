import { inject as service } from '@ember/service';
import DS from 'ember-data';
const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({
  authToken: service('auth-session'),
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
