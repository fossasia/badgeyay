import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  image         : attr('string'),
  csv           : attr('string'),
  text_colour   : attr('string'),
  badge_size    : attr('string'),
  download_link : attr('string'),
  created_at    : attr('date'),
  user_id       : attr('string')
});
