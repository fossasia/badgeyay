import DS from 'ember-data';

const { JSONAPISerializer } = DS;

export default JSONAPISerializer.extend({
  serialize(snapshot, options) {
    let json = this._super(...arguments);
    json.badge = {
      uid             : json.data.attributes.uid,
      csv             : json.data.attributes.csv,
      csv_type        : json.data.attributes['csv-type'],
      image           : json.data.attributes.image,
      image_link      : json.data.attributes['image-link'],
      logo_image_link : json.data.attributes['logo-image-link'],
      logo_text       : json.data.attributes['logo-text'],
      logo_color      : json.data.attributes['logo-color'],
      logo_image      : json.data.attributes['logo-image'],
      badge_name      : json.data.attributes['badge-name'],
      font_type       : json.data.attributes['font-type'],
      font_color_1    : json.data.attributes['font-color-1'],
      font_color_2    : json.data.attributes['font-color-2'],
      font_color_3    : json.data.attributes['font-color-3'],
      font_color_4    : json.data.attributes['font-color-4'],
      font_color_5    : json.data.attributes['font-color-5'],
      font_size_1     : json.data.attributes['font-size-1'],
      font_size_2     : json.data.attributes['font-size-2'],
      font_size_3     : json.data.attributes['font-size-3'],
      font_size_4     : json.data.attributes['font-size-4'],
      font_size_5     : json.data.attributes['font-size-5'],
      font_type_1     : json.data.attributes['font-type-1'],
      font_type_2     : json.data.attributes['font-type-2'],
      font_type_3     : json.data.attributes['font-type-3'],
      font_type_4     : json.data.attributes['font-type-4'],
      font_type_5     : json.data.attributes['font-type-5'],
      paper_size      : json.data.attributes['paper-size'],
      badge_size      : json.data.attributes['badge-size'],
      ticket_types    : json.data.attributes['ticket-types']
    };

    delete json.data;
    return json;
  },

  normalizeResponse(store, primaryModelClass, payload, id, requestType) {
    return payload;
  }
});
