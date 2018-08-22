import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid       : attr('string'),
  image     : attr('string'),
  extension : attr('string'),
  photoURL  : attr('string')
});
