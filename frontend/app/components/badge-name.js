import Component from '@ember/component';
import Ember from 'ember';

const { inject } = Ember;

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  notifications : inject.service('notification-messages'),
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
