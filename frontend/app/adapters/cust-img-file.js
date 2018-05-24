import ApplicationAdapter from './application';

export default ApplicationAdapter.extend({
  host        : 'http://localhost:5000',
  pathForType : () => {
    return 'api/upload/image';
  }
});
