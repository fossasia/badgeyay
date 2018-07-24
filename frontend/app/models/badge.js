import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid           : attr('string'),
  badgename     : attr('string'),
  csv           : attr('string'),
  image         : attr('string'),
  font_type     : attr('string'),
  font_color    : attr('string'),
  font_size_1   : attr('string'),
  font_size_2   : attr('string'),
  font_size_3   : attr('string'),
  font_size_4   : attr('string'),
  font_size_5   : attr('string'),
  badge_size    : attr('string'),
  paper_size    : attr('string'),
  download_link : attr('string')
});
