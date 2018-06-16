import Controller from '@ember/controller';

export default Controller.extend({
  queryParams : ['token'],
  token       : null,
  actions     : {
    resetPwd(pwd) {
      const this_ = this;
      let resetPwd = this_.get('store').createRecord('reset-password', {
        token: this_.token,
        pwd
      });
      resetPwd.save();
    }
  }
});
