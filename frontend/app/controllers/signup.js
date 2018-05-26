import Controller from '@ember/controller';

import { inject as service } from '@ember/service';

export default Controller.extend({
  routing : service('-routing'),
  actions : {
    signUp(email, password) {
      this.get('store').createRecord('user-signup', {
        email,
        password
      }).push();
    }
  }
});
