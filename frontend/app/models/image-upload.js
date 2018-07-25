import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid       : attr('string'),
  imageData : attr('string'),
  extension : attr('string'),
  filename  : attr('string')
});
