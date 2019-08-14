import { inject as service } from '@ember/service';
import Controller from '@ember/controller';

export default Controller.extend({
  userPage      : 1,
  notifications : service('notification-messages'),
  actions       : {
    nextPageUsers() {
      const _this = this;
      _this.get('store').query('all-user', {
        page: this.userPage + 1
      }).then(records => {
        if (records.length !== 0) {
          _this.set('users', records);
          _this.set('userPage', _this.userPage + 1);
        } else {
          _this.get('notifications').clearAll();
          _this.get('notifications').error('No users ahead', {
            autoClear     : true,
            clearDuration : 1500
          });
        }
      }).catch(err => {
        console.log(err);
      });
    },

    previousPageUsers() {
      const _this = this;
      if (this.userPage > 1) {
        _this.get('store').query('all-user', {
          page: this.userPage - 1
        }).then(records => {
          _this.set('users', records);
          _this.set('userPage', _this.userPage - 1);
        }).catch(err => {
          console.log(err);
        });
      }
    }
  }
});
