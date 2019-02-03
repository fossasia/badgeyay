import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid             : attr('string'),
  badge_name      : attr('string'),
  csv             : attr('string'),
  image           : attr('string'),
  image_link      : attr('string'),
  logo_image_link : attr('string'),
  logo_text       : attr('string'),
  logo_color      : attr('string'),
  logo_image      : attr('string'),
  font_color_1    : attr('string'),
  font_color_2    : attr('string'),
  font_color_3    : attr('string'),
  font_color_4    : attr('string'),
  font_color_5    : attr('string'),
  font_size_1     : attr('string'),
  font_size_2     : attr('string'),
  font_size_3     : attr('string'),
  font_size_4     : attr('string'),
  font_size_5     : attr('string'),
  font_type_1     : attr('string'),
  font_type_2     : attr('string'),
  font_type_3     : attr('string'),
  font_type_4     : attr('string'),
  font_type_5     : attr('string'),
  badge_size      : attr('string'),
  paper_size      : attr('string'),
  download_link   : attr('string')
});
