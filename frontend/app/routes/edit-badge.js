import Ember from 'ember';
import Route from '@ember/routing/route';
import { setProperties } from '@ember/object';

const { RSVP, set } = Ember;

export default Route.extend({
  templateName: 'create-badges',

  beforeModel() {
    if (this.get('session.currentUser') === undefined) {
      this.transitionTo('login');
    }
  },
  model(params) {
    return RSVP.hash({
      badge      : this.get('store').findRecord('badge', params.badge_id),
      def_images : this.get('store').findAll('def-image'),
      user       : this.get('store').findRecord('user', this.get('session.currentUser').uid)
    });
  },
  setupController(controller, model) {
    this._super(...arguments);
    let { badge } = model;
    controller.setProperties({
      'nameData'       : badge.badge_name,
      'defImages'      : model.def_images,
      'user'           : model.user,
      'badgeGenerated' : false,
      'showProgress'   : false,
      'paper_size'     : badge.paper_size,
      'badge_size'     : badge.badge_size,
      'defFont1Size'   : badge.font_size_1,
      'defFont2Size'   : badge.font_size_2,
      'defFont3Size'   : badge.font_size_3,
      'defFont4Size'   : badge.font_size_4,
      'defFont5Size'   : badge.font_size_5,
      'defFontType1'   : badge.font_type_1,
      'defFontType2'   : badge.font_type_2,
      'defFontType3'   : badge.font_type_3,
      'defFontType4'   : badge.font_type_4,
      'defFontType5'   : badge.font_type_5,
      'defFontCol1'    : badge.font_color_1.substr(1),
      'defFontCol2'    : badge.font_color_2.substr(1),
      'defFontCol3'    : badge.font_color_3.substr(1),
      'defFontCol4'    : badge.font_color_4.substr(1),
      'defFontCol5'    : badge.font_color_5.substr(1),
      'imageData'      : badge.image_link,
      'custImage'      : true,
      'defImage'       : false,
      'mode'           : 'edit',
      'logoImageData'  : (badge.logo_image_link && badge.logo_image_link !== '')
        ?  badge.logo_image_link : '/images/default_logo.png',
      'logo_text'     : badge.logo_text,
      'logoFontColor' : badge.logo_color.substr(1)
    });
    controller.send('setUpTemplate', model);
  }
});
