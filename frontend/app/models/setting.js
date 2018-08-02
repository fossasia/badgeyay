import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  appEnvironment        : attr('string'),
  appName               : attr('string'),
  secretKey             : attr('string'),
  firebaseStorageBucket : attr('string'),
  firebaseDatabaseURL   : attr('string'),
  fromMail              : attr('string'),
  sendGridApiKey        : attr('string')
});
