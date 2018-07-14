import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  username   : attr('string'),
  email      : attr('string'),
  photoURL   : attr('string'),
  created_at : attr('date'),
  password   : attr('string'),
  deleted_at : attr('date'),

  // Permissions
  isAdmin : attr('boolean'),
  isSales : attr('boolean'),
  isUser  : attr('boolean')
});
