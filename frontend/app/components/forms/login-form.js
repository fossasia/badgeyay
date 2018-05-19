import Component from '@ember/component';

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
      })
    ;
  }
});
