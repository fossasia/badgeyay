import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  valid: attr('boolean')
});
