import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  badgeCount        : attr('string'),
  userCreationCount : attr('string'),
  userDeletionCount : attr('string')
});
