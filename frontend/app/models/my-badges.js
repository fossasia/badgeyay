import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  badge_size    : attr('string'),
  csv           : attr('string'),
  download_link : attr('string'),
  image         : attr('string'),
  text_color    : attr('string')
});
