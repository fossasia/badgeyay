import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  csvFile   : attr('string'),
  extension : attr('string')
});
