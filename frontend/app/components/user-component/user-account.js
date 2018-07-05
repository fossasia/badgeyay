import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  actions: {
    updateUserName() {
      let profileName = this.get('profileName');
      this.get('sendUserName')(profileName);
    }
  },


  didRender() {
    this.$('.ui.form')
      .form({
        inline : true,
        delay  : false,
        fields : {
          username: {
            identifier : 'profileName',
            rules      : [
              {
                type   : 'empty',
                prompt : 'Please enter a valid username'
              }
            ]
          }
        }
      });
  }
});
