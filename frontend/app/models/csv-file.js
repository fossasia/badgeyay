import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid       : attr('string'),
  csvFile   : attr('string'),
  extension : attr('string'),
  filename  : attr('string')
});
