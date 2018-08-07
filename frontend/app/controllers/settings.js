import Controller from '@ember/controller';
import { inject as service } from '@ember/service';

export default Controller.extend({
  routing       : service('-routing'),
  notifications : service('notification-messages'),
  uid           : '',
  actions       : {
    updateProfileImage(profileImageData, extension) {
      const _this = this;
      const user = this.get('store').peekAll('user');
      user.forEach(user_ => {
        _this.set('uid', user_.get('id'));
      });
      let profileImage = _this.get('store').createRecord('profile-image', {
        image     : profileImageData,
        uid       : _this.uid,
        extension : '.' + extension
      });
      profileImage.save()
        .then(record => {
          user.forEach(user_ => {
            user_.set('photoURL', record.photoURL);
          });
        })
        .catch(err => {
          let userErrors = profileImage.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
          }
        });
    },


    updateUserName() {
      this.set('isLoadingName', true);
      this.get('user').save()
        .then(() => this.get('notifications').success('Username Successfully Updated!', {
          autoClear     : true,
          clearDuration : 1500
        }))
        .finally(() => this.set('isLoadingName', false));
    },

    updateUserPassword() {
      this.set('isLoadingPassword', true);
      this.get('user').save()
        .then(() => this.get('notifications').success('Password Successfully Updated!', {
          autoClear     : true,
          clearDuration : 1500
        }))
        .finally(() => this.set('isLoadingPassword', false));
    }
  }
});
