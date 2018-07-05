import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  description : attr('string'),
  link        : attr('string'),
  icon        : attr('string')
});
