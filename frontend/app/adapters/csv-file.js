import DS from 'ember-data';

const { RESTAdapter } = DS;

export default RESTAdapter.extend({
  host        : 'http://localhost:5000',
  pathForType : () => {
    return 'api/upload/file';
  }
});
