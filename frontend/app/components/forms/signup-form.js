import Component from '@ember/component';

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
