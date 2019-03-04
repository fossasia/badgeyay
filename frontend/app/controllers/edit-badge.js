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

    imageChange(idx) {
      let { badge } = this.model;
      let backImgChanged = this.get('backImgChanged');
      let defImage = this.get('defImage');
      let colorImage = this.get('colorImage');
      let custImage = this.get('custImage');
      let imageData = this.get('imageData');
      backImgChanged.set(idx, false);
      defImage.set(idx, false);
      colorImage.set(idx, false);
      custImage.set(idx, true);
      imageData.set(idx, badge.image_link);
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
