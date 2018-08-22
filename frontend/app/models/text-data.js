import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid         : attr('string'),
  manual_data : attr('string'),
  time        : attr('date'),
  filename    : attr('string')
});
