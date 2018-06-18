import ApplicationAdapter from './application';
import ENV from '../config/environment';
import { computed } from '@ember/object';
import { inject as service } from '@ember/service';

const { APP } = ENV;

export default ApplicationAdapter.extend({
  host       : APP.backLink,
  loginToken : service('auth-session'),
  headers    : computed('loginToken.authToken', function() {
    return {
      'x-access-token': this.get('loginToken.sessionToken')
    };
  }),
  pathForType: () => {
    return 'api/default_images';
  }
});
