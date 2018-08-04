import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  mailSentCount      : attr('string'),
  badgeCount         : attr('string'),
  userCreationCount  : attr('string'),
  userDeletionCount  : attr('string'),
  badgeDeletionCount : attr('string')
});
