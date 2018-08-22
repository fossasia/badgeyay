import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },

  actions: {
    updateUserPassword() {
      let password = this.get('newPassword');
      this.get('sendUserPassword')(password);
    }
  },


  didRender() {
    this.$('.ui.form')
      .form({
        inline : true,
        delay  : false,
        fields : {
          newPassword: {
            identifier : 'newPassword',
            rules      : [
              {
                type   : 'empty',
                prompt : 'Please enter a password'
              },
              {
                type   : 'minLength[6]',
                prompt : 'Your password must have at least {ruleValue} characters'
              }
            ]
          },
          newPasswordVerify: {
            identifier : 'newPasswordVerify',
            rules      : [
              {
                type   : 'match[newPassword]',
                prompt : 'Passwords do not match'
              }
            ]
          }
        }
      });
  }
});
