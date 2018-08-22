import DS from 'ember-data';

const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({

  serialize(snapshot, options) {
    let json = this._super(...arguments);
    json.csvFile = {
      'uid'       : json.data.attributes.uid,
      'csvFile'   : json.data.attributes['csv-file'],
      'extension' : json.data.attributes.extension
    };

    delete json.data;
    return json;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    return payload;
  }

});

