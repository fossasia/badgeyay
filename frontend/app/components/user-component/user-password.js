import Component from '@ember/component';
import $ from 'jquery';

var pwShownVerify = 0;
var pwShown = 0;


export default Component.extend({
  init() {
    this._super(...arguments);
  },

  actions: {
    updateUserPassword() {
      let password = this.get('newPassword');
      this.get('sendUserPassword')(password);
    },
    showPasswordSettings() {
      function show() {
        $('#newPassword').attr('type',  'text');
      }
      function hide() {
        $('#newPassword').attr('type', 'password');
      }
      if (pwShown == 0) {
        pwShown = 1;
        show();
      } else {
        pwShown = 0;
        hide();
      }
    },
    showPasswordSettingsVerify() {
      function show() {
        $('#newPasswordVerify').attr('type',  'text');
      }
      function hide() {
        $('#newPasswordVerify').attr('type', 'password');
      }
      if (pwShownVerify == 0) {
        pwShownVerify = 1;
        show();
      } else {
        pwShownVerify = 0;
        hide();
      }
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
