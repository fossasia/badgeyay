import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  token  : attr('string'),
  pwd    : attr('string'),
  status : attr('string')
});
