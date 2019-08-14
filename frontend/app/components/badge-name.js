import { inject as service } from '@ember/service';
import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  notifications : service('notification-messages'),
  actions       : {

    updateBadgeName() {
      this.get('sendBadgeName')(this.get('badge'));
    },


    didRender() {
      this.$('.ui.form')
        .form({
          inline : true,
          delay  : false,
          fields : {
            Name: {
              identifier : 'Name',
              rules      : [
                {
                  type   : 'empty',
                  prompt : 'Please enter a valid Badge Name'
                }
              ]
            }
          }
        });
    }
  }
});
