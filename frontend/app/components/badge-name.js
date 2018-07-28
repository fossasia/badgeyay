import Component from '@ember/component';
import Ember from 'ember';

const { inject } = Ember;

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  notify  : inject.service('notify'),
  actions : {

    updateBadgeName(badge) {
      this.get('sendBadgeName')(badge);
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
