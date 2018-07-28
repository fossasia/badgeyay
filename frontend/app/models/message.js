import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  Description : attr('string'),
  Subject     : attr('string')
});
