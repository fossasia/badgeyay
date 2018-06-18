import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  actions: {
    sendResetMail() {
      this.get('sendResetMail')(this.email);
    }
  },
  didRender() {
    this.$('.ui.fluid.form')
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
          }
        }
      });
  }
});
