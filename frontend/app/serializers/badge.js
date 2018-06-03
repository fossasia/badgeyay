import DS from 'ember-data';

const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({

  serialize(snapshot, options) {
    let json = this._super(...arguments);
    json.badge = {
      'uid'        : json.data.attributes.uid,
      'csv'        : json.data.attributes.csv,
      'image'      : json.data.attributes.image,
      'font_type'  : json.data.attributes['font-type'],
      'font_color' : json.data.attributes['font-color'],
      'font_size'  : json.data.attributes['font-size'],
      'badge_size' : json.data.attributes['badge-size']
    };

    delete json.data;
    return json;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    return payload;
  }

});
