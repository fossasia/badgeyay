import Controller from '@ember/controller';

import { inject as service } from '@ember/service';

export default Controller.extend({
  routing      : service('-routing'),
  defColor     : '',
  defFontColor : '',
  defFontSize  : '',
  uid          : '',
  actions      : {
    mutateCSV(csvData) {
      const user = this.get('store').peekAll('user');
      let uid;
      user.forEach(user_ => {
        uid = user_.get('id');
      });
      if (uid !== undefined && uid !== '') {
        this.set('uid', uid);
      }
      let csv_ = this.get('store').createRecord('csv-file', {
        uid,
        csvFile   : csvData,
        extension : 'csv'
      });
      csv_.save();
    },

    mutateText(txtData) {
      console.log(txtData);
    },

    mutateBackground(id) {
      console.log(id);
    },

    mutateDefColor(color) {
      this.set('defColor', color);
    },

    mutateCustomImage(imageData) {
      let uid = this.get('uid');
      if (uid === undefined || uid === '') {
        const user = this.get('store').peekAll('user');
        user.forEach(user_ => {
          uid = user_.get('id');
        });
      }
      let image_ = this.get('store').createRecord('cust-img-file', {
        uid,
        imageData,
        extension: 'png'
      });
      image_.save();
    },

    mutateDefFontColor(fontcolor) {
      this.set('defFontColor', fontcolor);
    },

    mutateCustomFont(id) {
      console.log(id);
    },

    mutateFontSize(value) {
      this.set('defFontSize', value);
    }
  }
});
