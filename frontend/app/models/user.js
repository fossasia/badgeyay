import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid      : attr('string'),
  username : attr('string'),
  email    : attr('string'),
  photoURL : attr('string'),
  ftl      : attr('boolean')
});
