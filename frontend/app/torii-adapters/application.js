import Ember from 'ember';
import ToriiFirebaseAdapter from 'emberfire/torii-adapters/firebase';
import ENV from '../config/environment';

const { APP } = ENV;

const { inject, RSVP } = Ember;

export default ToriiFirebaseAdapter.extend({
  firebase: inject.service(),

  /**
   * Executed after Firebase authentication.
   *
   * @param  {Object} authData
   * @return {Promise<Object>} Updated session info
   */
  open(user) {
    let User = {};
    Object.keys(user).forEach(key => User[key] = user[key]);
    return new RSVP.Promise(resolve => {
      fetch(APP.backLink + '/user/updateLastLogin/' + user.uid)
        .then(res => res.json())
        .then(res => {
          User.photoURL = res.data.attributes.photoURL;
        })
        .catch(err => {
          console.log(err);
        })
        .finally(() => {
          resolve({
            provider    : this.extractProviderId_(User),
            uid         : User.uid,
            currentUser : User
          });
        });
    });
  }
});
