import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  uid  : attr('string'),
  name : attr('string')
});
