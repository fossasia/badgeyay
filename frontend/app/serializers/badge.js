import DS from 'ember-data';

const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({

  serialize(snapshot, options) {
    let json = this._super(...arguments);
    json.badge = {
      'uid'        : json.data.attributes.uid,
      'csv'        : json.data.attributes['csv-file'],
      'image'      : json.data.attributes['image-data'],
      'font_type'  : json.data.attributes,
      'font_color' : json.data.attributes,
      'font_size'  : json.data.attributes,
      'badge_size' : json.data.attributes
    };

    delete json.data;
    return json;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    return payload;
  }

});
