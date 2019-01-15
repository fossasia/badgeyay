import Route from '@ember/routing/route';
import ENV from '../config/environment';

export default Route.extend({
  model() {
    return ENV.badgeyaySupportMail;
  }
});
