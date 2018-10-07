import Component from '@ember/component';

var pwShown = 0;

export default Component.extend({
  init() {
    this._super(...arguments);
  },

  actions: {

    logIn(provider) {
      let email = '';
      let password = '';
      if (provider == 'password') {
        email = this.get('email');
        password = this.get('password');
      }
      this.get('login')(provider, email, password);
    },

    logOut() {
      this.get('session').close();
    },
    show1() {
      if (pwShown == 0) {
        pwShown = 1;
        show();
      } else {
        pwShown = 0;
        hide();
      }
      function show() {
        var p = document.getElementById('pwd');
        p.setAttribute('type', 'text');
      }

      function hide() {
        var p = document.getElementById('pwd');
        p.setAttribute('type', 'password');
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
          password: {
            identifier : 'password',
            rules      : [
              {
                type   : 'empty',
                prompt : 'Please enter a password'
              }
            ]
          }
        }
      });
  }
});
