import ApplicationAdapter from './application';
import ENV from '../config/environment';

const { APP } = ENV;

export default ApplicationAdapter.extend({
  host: APP.backLink,
  pathForType() {
    const user = this.get('session.currentUser');
    return 'api/get_badges?uid=' + user.uid;
  }
});