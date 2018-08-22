import DS from 'ember-data';

const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    console.log(payload);
    return payload;
  }

});
