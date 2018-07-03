import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  name       : attr('string'),
  created_at : attr('date'),
  deleted_at : attr('date')
});
