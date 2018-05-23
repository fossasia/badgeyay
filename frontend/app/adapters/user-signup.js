import DS from 'ember-data';

const { JSONAPIAdapter } = DS;

export default JSONAPIAdapter.extend({
  host        : 'http://localhost:5000',
  pathForType : () => {
    return 'api/user/signup';
  }
});
