import Component from '@ember/component';
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
      email = this.get('email');
      password = this.get('password');
      username = this.get('username');
      if (email !== undefined && password !== undefined && username !== undefined) {
        this.get('signUp')(email, username, password);
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
