import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid           : attr('string'),
  csv           : attr('string'),
  image         : attr('string'),
  font_type     : attr('string'),
  font_color    : attr('string'),
  font_size     : attr('string'),
  badge_size    : attr('string'),
  download_link : attr('string')
});
