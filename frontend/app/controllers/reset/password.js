import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  queryParams : ['token'],
  token       : null,
  notify      : inject.service('notify'),
  actions     : {
    resetPwd(pwd) {
      const _this = this;
      let resetPwd = _this.get('store').createRecord('reset-password', {
        token: _this.token,
        pwd
      });
      resetPwd.save()
        .then(record => {
          if (record.status === 'Changed') {
            _this.get('notify').success('Please login with changed credentials');
            _this.transitionToRoute('/login');
          } else if (record.status === 'Not Changed') {
            _this.get('notify').error('Unable to change the password');
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
  }
});
