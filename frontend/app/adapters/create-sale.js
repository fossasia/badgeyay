import DS from 'ember-data';
import ENV from '../config/environment';
import { computed } from '@ember/object';
import { inject as service } from '@ember/service';


const { APP } = ENV;
const { JSONAPIAdapter } = DS;

export default JSONAPIAdapter.extend({
  host       : APP.backLink,
  loginToken : service('auth-session'),
  headers    : computed('loginToken.authToken', function() {
    return {
      'x-access-token': this.get('loginToken.sessionToken')
    };
  }),
  pathForType: () => {
    return 'admin/register_sales';
  }
});
