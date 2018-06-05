import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid      : attr('string'),
  color    : attr('string'),
  filename : attr('string')
});
