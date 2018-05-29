import DS from 'ember-data';

const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({

  serialize(snapshot, options) {
    let json = this._super(...arguments);
    return json;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    return payload;
  }
});
