import ApplicationAdapter from './application';
import ENV from '../config/environment';

const { APP } = ENV;

export default ApplicationAdapter.extend({
  host        : APP.backLink,
  pathForType : () => {
    return 'api/upload/image';
  }
});
