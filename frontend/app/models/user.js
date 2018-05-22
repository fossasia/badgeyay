import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  name     : attr('string'),
  email    : attr('string'),
  photoUrl : attr('string')
});
