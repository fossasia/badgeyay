import Ember from 'ember';
import DS from 'ember-data';

const { String } = Ember;
const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({

  keyForAttribute(attr) {
    return String.underscore(attr);
  },

  serialize(snapshot, options) {
    let json = this._super(...arguments);
    return json;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    return payload;
  }

});
