import Component from '@ember/component';
var pwShown1 = 0;
var pwShown = 0;

export default Component.extend({
  init() {
    this._super(...arguments);
  },

  email     : '',
  password  : '',
  isLoading : false,

  actions: {
    signUp(event) {
      event.preventDefault();
      let email = '';
      let password = '';
      let username = '';
      email = this.get('email');
      password = this.get('password');
      username = this.get('username');
      if (email !== undefined && password !== undefined && username !== undefined) {
        this.get('signUp')(email, username, password);
      }
    },
    show2() {


      function show1() {
        var p = document.getElementById('pwd2');
        p.setAttribute('type', 'text');
      }

      function hide1() {
        var p = document.getElementById('pwd2');
        p.setAttribute('type', 'password');
      }


      if (pwShown == 0) {
        pwShown = 1;
        show1();
      } else {
        pwShown = 0;
        hide1();
      }
    },
    show1() {
      function show() {
        var p = document.getElementById('pwd1');
        p.setAttribute('type', 'text');
      }

      function hide() {
        var p = document.getElementById('pwd1');
        p.setAttribute('type', 'password');
      }
      if (pwShown1 == 0) {
        pwShown1 = 1;
        show();
      } else {
        pwShown1 = 0;
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
  }
});
