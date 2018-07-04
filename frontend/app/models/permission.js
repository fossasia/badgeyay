import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  isUser  : attr('boolean'),
  isAdmin : attr('boolean'),
  isSales : attr('boolean')
});
