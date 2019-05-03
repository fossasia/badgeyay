import $ from 'jquery';
import Component from '@ember/component';
var pwShownConfirm = 0;
var pwShown = 0;

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  level     : 0,
  email     : '',
  password  : '',
  isLoading : false,

  actions: {
    signUp(event) {
      event.preventDefault();
      let email = '';
      let password = '';
      let username = '';
      let password_rep = '';
      email = this.get('email');
      password = this.get('password');
      password_rep = this.get('password_repeat');
      username = this.get('username');
      if (password === password_rep) {
        if (email !== undefined && password !== undefined && username !== undefined) {
          this.get('signUp')(email, username, password);
        }
      }
    },
    showPasswordSignupConfirm() {
      function show() {
        $('#pwdConfirm').attr('type',  'text');
        $('#eye2 > i').removeClass('eye slash icon');
        $('#eye2 > i').addClass('eye icon');
      }
      function hide() {
        $('#pwdConfirm').attr('type', 'password');
        $('#eye2 > i').removeClass('eye icon');
        $('#eye2 > i').addClass('eye slash icon');
      }
      if (pwShownConfirm == 0) {
        pwShownConfirm = 1;
        show();
      } else {
        pwShownConfirm = 0;
        hide();
      }
    },
    showPasswordSignup() {
      function show() {
        $('#pwd').attr('type', 'text');
        $('#eye1 > i').removeClass('eye slash icon');
        $('#eye1 > i').addClass('eye icon');
      }

      function hide() {
        $('#pwd').attr('type', 'password');
        $('#eye1 > i').removeClass('eye icon');
        $('#eye1 > i').addClass('eye slash icon');
      }
      if (pwShown == 0) {
        pwShown = 1;
        show();
      } else {
        pwShown = 0;
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
          email: {
            identifier : 'email',
            rules      : [
              {
                type   : 'email',
                prompt : 'Please enter a valid email address'
              }
            ]
          },
          username: {
            identifier : 'username',
            rules      : [
              {
                type   : 'empty',
                prompt : 'Please enter a valid username'
              }
            ]
          },
          password: {
            identifier : 'password',
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
          password_repeat: {
            identifier : 'password_repeat',
            rules      : [
              {
                type   : 'match[password]',
                prompt : 'Passwords do not match'
              }
            ]
          }
        }
      });
  },
  keyUp(event) {
    if (event.target.name === 'password') {
      if ((event.target.value).length < 6) {
        $('#signUpSubmit').attr('disabled', 'true');
        $('#feedback').html('Your password must have at least 6 characters');
      } else {
        $('#signUpSubmit').removeAttr('disabled');
        $('#feedback').html('');
      }
    }
  },
  keyDown(event) {
    if (event.target.name === 'password') {
      var strongRegex = new RegExp('^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$', 'g');
      var mediumRegex = new RegExp('^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$', 'g');
      var enoughRegex = new RegExp('(?=.{6,}).*', 'g');
      if (false == enoughRegex.test(event.target.value)) {
        this.set('level', 0);
      } else if (strongRegex.test(event.target.value)) {
        this.set('level', 4);
      } else if (mediumRegex.test(event.target.value)) {
        this.set('level', 3);
      } else {
        this.set('level', 1);
      }
    }
  }
});
