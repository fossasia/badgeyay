import DS from 'ember-data';

const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({

  serialize(snapshot, options) {
    let json = this._super(...arguments);
    json.imgFile = {
      'uid'       : json.data.attributes.uid,
      'imgFile'   : json.data.attributes['image-data'],
      'extension' : json.data.attributes.extension
    };

    delete json.data;
    return json;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    return payload;
  }
});
