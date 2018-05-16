import DS from 'ember-data';
import Route from '@ember/routing/route';

const { Store } = DS;

export default Route.extend({
  actions: {
    createUser(uid, name) {
      let user = Store.createRecord('user', {
        uid,
        name
      });
      user.save();
    }
  }
});
