import CreateBadges from './create-badges';
import ENV from '../config/environment';
import $ from 'jquery';

const { APP } = ENV;

import { inject as service } from '@ember/service';

export default CreateBadges.extend({
  actions: {
    csvChange() {
      this.set('csvChanged', false);
      document.getElementById('csv').style.display = 'none';
      document.getElementById('details').style.display = 'none';
    },

    logoChange() {
      this.set('logoImgChanged', false);
      let { badge } = this.model;
      this.setProperties({
        'logoImgChanged' : false,
        'logoImageData'  : (badge.logo_image_link && badge.logo_image_link !== '')
          ?  badge.logo_image_link : '/images/default_logo.png',
        'custLogoImage' : false,
        'logo_text'     : badge.logo_text,
        'logoFontColor' : badge.logo_color
      });
      document.getElementById('custlogoimg').style.display = 'none';
      document.getElementById('custlogocol').style.display = 'none';
    },

    imageChange() {
      let { badge } = this.model;
      this.setProperties({
        'backImgChanged' : false,
        'imageData'      : badge.image_link,
        'defImage'       : false,
        'colorImage'     : false,
        'custImage'      : true
      });
      console.log(this.get('backImgChanged'), this.get('imageData'));
      document.getElementById('custcol').style.display = 'none';
      document.getElementById('custbg').style.display = 'none';
      document.getElementById('custimg').style.display = 'none';
    },

    setUpTemplate(model) {
      $(document).ready(function() {
        document.querySelectorAll('input[name="size"]').forEach(el => {
          if (el.value === model.badge.paper_size) {
            el.checked = true;
          }
        });
        document.querySelectorAll('input[name="badge"]').forEach(el => {
          if (el.value === model.badge.badge_size) {
            el.checked = true;
          }
        });
      });
    }
  }
});
