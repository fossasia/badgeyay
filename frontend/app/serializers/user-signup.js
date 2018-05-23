import DS from 'ember-data';

const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({

  serialize(snapshot, options) {
    let json = this._super(...arguments);
    json.userSignup = {
      'email'    : json.data.attributes.email,
      'password' : json.data.attributes.password
    };

    delete json.data;
    return json;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    return payload;
  }
});
