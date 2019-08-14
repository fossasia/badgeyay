import { inject as service } from '@ember/service';
import Controller from '@ember/controller';

export default Controller.extend({
  queryParams   : ['token'],
  token         : null,
  notifications : service('notification-messages'),
  actions       : {
    resetPwd(pwd) {
      const _this = this;
      let resetPwd = _this.get('store').createRecord('reset-password', {
        token: _this.token,
        pwd
      });
      resetPwd.save()
        .then(record => {
          if (record.status === 'Changed') {
            _this.get('notifications').success('Please login with changed credentials', {
              autoClear     : true,
              clearDuration : 1500
            });
            _this.transitionToRoute('/login');
          } else if (record.status === 'Not Changed') {
            _this.get('notifications').error('Unable to change the password', {
              autoClear     : true,
              clearDuration : 1500
            });
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
  }
});
