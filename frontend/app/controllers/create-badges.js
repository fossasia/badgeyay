import Controller from '@ember/controller';

import { inject as service } from '@ember/service';

export default Controller.extend({
  routing      : service('-routing'),
  defColor     : '',
  defFontColor : '',
  defFontSize  : '',
  uid          : '',
  textData     : '',
  userError    : '',
  actions      : {
    submitForm() {
      const _this = this;
      const user = _this.get('store').peekAll('user');
      let uid;
      user.forEach(user_ => {
        uid = user_.get('id');
      });
      if (uid !== undefined && uid !== '') {
        _this.set('uid', uid);
      }
      let textEntry = _this.get('store').createRecord('text-data', {
        uid,
        manual_data : _this.get('textData'),
        time        : new Date()
      });
      textEntry.save().then(record => {
        console.log(record);
      }).catch(err => {
        let userErrors = textEntry.get('errors.user');
        if (userErrors !== undefined) {
          _this.set('userError', userErrors);
        }
      });
    },

    mutateCSV(csvData) {
      const _this = this;
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
        extension : '.csv'
      });
      csv_.save()
        .catch(err => {
          let userErrors = csv_.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
          }
        });
    },

    mutateText(txtData) {
      this.set('textData', txtData);
    },

    mutateBackground(id) {
      console.log(id);
    },

    mutateDefColor(color) {
      this.set('defColor', color);
    },

    mutateCustomImage(imageData) {
      const _this = this;
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
        extension: '.png'
      });
      image_.save()
        .catch(err => {
          let userErrors = image_.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
          }
        });
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
