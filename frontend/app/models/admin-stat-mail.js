import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  lastDayCount  : attr('string'),
  lastThreeDays : attr('string'),
  lastSevenDays : attr('string'),
  lastMonth     : attr('string')
});
