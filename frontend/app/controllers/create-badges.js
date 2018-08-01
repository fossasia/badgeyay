import Controller from '@ember/controller';
import ENV from '../config/environment';

const { APP } = ENV;

import { inject as service } from '@ember/service';

export default Controller.extend({
  routing        : service('-routing'),
  notify         : service('notify'),
  authToken      : service('auth-session'),
  defColor       : '',
  backColor      : '',
  defFontColor   : '',
  fontColor      : '',
  defFont1Size   : '10',
  defFont2Size   : '10',
  defFont3Size   : '10',
  defFont4Size   : '10',
  defFont5Size   : '10',
  defFont        : '',
  uid            : '',
  textData       : '',
  nameData       : '',
  userError      : '',
  csvFile        : '',
  custImgFile    : '',
  badgeSize      : '',
  previewToggled : false,
  previewHeight  : '',
  badgeGenerated : false,
  backLink       : APP.backLink,
  defPaperSize   : '',
  genBadge       : '',
  defImageName   : '',
  csvEnable      : false,
  manualEnable   : false,
  defImage       : false,
  custImage      : false,
  colorImage     : false,
  overlay        : false,
  showProgress   : false,
  imageData      : null,
  progress       : 0,
  progressState  : '',
  firstName      : '',
  lastName       : '',
  organization   : '',
  socialHandle   : '',
  designation    : '',
  prevImageData  : '',
  csvClicked() {
    this.set('csvEnable', true);
    this.set('manualEnable', false);
  },

  manualClicked() {
    this.set('manualEnable', true);
    this.set('csvEnable', false);
  },

  defImageClicked() {
    this.set('defImage', true);
    this.set('colorImage', false);
    this.set('custImage', false);
    this.set('imageData', null);
  },

  bgColorClicked() {
    this.set('colorImage', true);
    this.set('defImage', false);
    this.set('custImage', false);
    this.set('imageData', null);
  },

  custImgClicked() {
    this.set('custImage', true);
    this.set('defImage', false);
    this.set('colorImage', false);
  },
  actions: {
    submitForm() {
      const _this = this;
      const user = _this.get('store').peekAll('user');
      _this.set('overlay', true);
      let uid;
      user.forEach(user_ => {
        uid = user_.get('id');
      });
      if (uid !== undefined && uid !== '') {
        _this.set('uid', uid);
      }

      let badgeData = {
        uid        : _this.uid,
        paper_size : 'A3',
        badgename  : '',
        badge_size : '4x3'
      };

      if (_this.nameData !== '') {
        badgeData.badgename = _this.nameData;
      }

      if (_this.badgeSize !== '' && _this.badgeSize !== undefined) {
        badgeData.badge_size = _this.badgeSize;
      }

      if (_this.defPaperSize !== '' && _this.defPaperSize !== undefined) {
        badgeData.paper_size = _this.defPaperSize;
      }

      if (_this.csvEnable) {
        badgeData.csv = _this.csvFile;
      }

      if (_this.defFontColor !== '' && _this.defFontColor !== undefined) {
        badgeData.font_color = '#' + _this.defFontColor;
      }

      if (_this.defFont1Size !== '' && _this.defFont1Size !== undefined) {
        badgeData.font_size_1 = _this.defFont1Size.toString();
        badgeData.font_size_2 = _this.defFont2Size.toString();
        badgeData.font_size_3 = _this.defFont3Size.toString();
        badgeData.font_size_4 = _this.defFont4Size.toString();
        badgeData.font_size_5 = _this.defFont5Size.toString();
      }

      if (_this.defFont !== '' && _this.defFont !== undefined) {
        badgeData.font_type = _this.defFont;
      }

      _this.send('sendManualData', badgeData);

    },

    sendManualData(badgeData) {
      const _this = this;
      if (_this.manualEnable) {
        this.set('showProgress', true);
        this.set('progress', 10);
        this.set('progressState', 'Setting Paper Size');
        let textEntry = _this.get('store').createRecord('text-data', {
          uid         : _this.uid,
          manual_data : _this.get('textData'),
          time        : new Date()
        });
        this.set('progress', 20);
        this.set('progressState', 'Generating CSV');
        textEntry.save().then(record => {
          _this.set('csvFile', record.filename);
          badgeData.csv = _this.csvFile;
          _this.send('sendDefaultImg', badgeData);
          _this.get('notify').success('Text saved Successfully');
          this.set('progress', 40);
          this.set('progressState', 'Gathering background');
        }).catch(err => {
          let userErrors = textEntry.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
            userErrors.forEach(error => {
              _this.get('notify').error(error.message);
              this.set('showProgress', false);
              this.set('progress', 0);
              this.set('progressState', '');
            });
          }
        });
      } else if (_this.csvEnable) {
        if (_this.csvFile !== undefined && _this.csvFile !== '') {
          badgeData.csv = _this.csvFile;
          this.set('showProgress', true);
          this.set('progress', 40);
          this.set('progressState', 'Gathering background');
          _this.send('sendDefaultImg', badgeData);
        }
      } else {
        _this.get('notify').error('No Input source specified');
        this.set('showProgress', false);
        this.set('progress', 0);
      }
    },

    sendDefaultImg(badgeData) {
      const _this = this;
      if (_this.defImage) {
        let imageRecord = _this.get('store').createRecord('def-image-upload', {
          uid          : _this.uid,
          defaultImage : _this.defImageName
        });
        imageRecord.save()
          .then(record => {
            _this.set('custImgFile', record.filename);
            badgeData.image = _this.custImgFile;
            _this.send('sendBadge', badgeData);
            this.set('progress', 70);
            this.set('progressState', 'Preparing your badges');
          })
          .catch(error => {
            let userErrors = imageRecord.get('errors.user');
            if (userErrors !== undefined) {
              _this.set('userError', userErrors);
              userErrors.forEach(error => {
                _this.get('notify').error(error.message);
                this.set('showProgress', false);
                this.set('progress', 0);
                this.set('progressState', '');
              });
            }
          });
      } else if (this.imageData) {
        this.get('store').createRecord('cust-img-file', {
          uid       : this.uid,
          imageData : this.imageData,
          extension : '.png' })
          .save()
          .then(record => {
            badgeData.image = record.filename;
            _this.send('sendBadge', badgeData);
            this.set('progress', 70);
            this.set('progressState', 'Preparing your badges');
          })
          .catch(error => {
            let userErrors = this.get('errors.user');
            if (userErrors !== undefined) {
              _this.set('userError', userErrors);
              userErrors.forEach(error => {
                _this.get('notify').error(error.message);
                this.set('showProgress', false);
                this.set('progress', 0);
                this.set('progressState', '');
              });
            }
          });
      } else if (_this.colorImage && _this.defColor !== undefined && _this.defColor !== '') {
        console.log(_this.defColor);
        let imageRecord = _this.get('store').createRecord('bg-color', {
          uid      : _this.uid,
          bg_color : _this.defColor
        });
        imageRecord.save()
          .then(record => {
            badgeData.image = record.filename;
            _this.send('sendBadge', badgeData);
            this.set('progress', 70);
            this.set('progressState', 'Preparing your badges');
          })
          .catch(error => {
            let userErrors = imageRecord.get('errors.user');
            if (userErrors !== undefined) {
              _this.set('userError', userErrors);
              userErrors.forEach(error => {
                _this.get('notify').error(error.message);
                this.set('showProgress', false);
                this.set('progress', 0);
                this.set('progressState', '');
              });
            }
          });
      } else {
        _this.get('notify').error('No background source specified');
        this.set('showProgress', false);
        this.set('progress', 0);
        this.set('progressState', '');
      }
    },


    sendBadge(badgeData) {
      const _this = this;
      let badgeRecord = _this.get('store').createRecord('badge', badgeData);
      this.set('progress', 80);
      badgeRecord.save()
        .then(record => {
          _this.set('overlay', false);
          _this.set('badgeGenerated', true);
          _this.set('genBadge', record);
          this.set('progress', 100);
          this.set('progressState', '');
          this.set('badgeGeneratedLink', record.download_link);
        })
        .catch(err => {
          _this.set('overlay', false);
          _this.get('notify').error('Unable to generate badge');
          this.set('showProgress', false);
          this.set('progress', 0);
        });
    },


    mutateCSV(csvData) {
      this.csvClicked();
      const _this = this;
      const user = this.get('store').peekAll('user');
      let uid;
      user.forEach(user_ => {
        uid = user_.get('id');
      });
      if (uid !== undefined && uid !== '') {
        _this.set('uid', uid);
      }
      let csv_ = this.get('store').createRecord('csv-file', {
        uid,
        csvFile   : csvData,
        extension : 'csv'
      });
      csv_.save()
        .then(record => {
          _this.set('csvFile', record.filename);
          _this.get('notify').success('CSV uploaded Successfully');
        })
        .catch(err => {
          let userErrors = csv_.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
            userErrors.forEach(error => {
              _this.get('notify').error(error.message);
            });
          }
        });
    },

    mutateText(txtData) {
      this.manualClicked();
      this.set('textData', txtData);
      let prevData = txtData.split('\n')[0].split(',');
      this.set('firstName', prevData[0].toString());
      this.set('lastName', prevData[1].toString());
      this.set('designation', prevData[2].toString());
      this.set('organization', prevData[3].toString());
      this.set('socialHandle', prevData[4].toString());
    },

    mutateName(namData) {
      this.set('nameData', namData);
    },

    mutateBackground(id) {
      this.defImageClicked();
      let defImageRecord = this.get('store').peekRecord('def-image', id);
      this.set('defImageName', defImageRecord.name + '.png');
    },

    mutateDefColor(color) {
      this.bgColorClicked();
      this.set('defColor', color);
      this.set('backColor', color);
    },

    mutateCustomImage(imageData) {
      this.custImgClicked();
      this.set('prevImageData', imageData);
      const _this = this;
      let uid = this.get('uid');
      if (uid === undefined || uid === '') {
        const user = this.get('store').peekAll('user');
        user.forEach(user_ => {
          uid = user_.get('id');
          _this.set('uid', uid);
        });
      }
      let image_ = this.get('store').createRecord('cust-img-file', {
        uid,
        imageData,
        extension: '.png'
      });
      image_.save()
        .then(record => {
          _this.set('custImgFile', record.filename);
          _this.get('notify').success('Image uploaded Successfully');
        })
        .catch(err => {
          let userErrors = image_.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
            userErrors.forEach(error => {
              _this.get('notify').error(error.message);
            });
          }
        });
    },

    removeFTL() {
      const _this = this;
      const user = _this.get('store').peekAll('user');
      let uid;
      user.forEach(user_ => {
        uid = user_.get('id');
      });
      if (uid !== undefined && uid !== '') {
        _this.set('uid', uid);
      }
      this.get('store').findRecord('user', uid)
        .then(record => {
          record.set('ftl', false);
          record.save();
        });
    },

    mutateDefFontColor(fontcolor) {
      this.set('defFontColor', fontcolor);
      this.set('fontColor', fontcolor);
    },

    mutateCustomFont(id) {
      this.set('defFont', id);
    },

    mutateFontSize(values) {
      const [font1, font2, font3, font4, font5] = values;
      if (font1 !== '') {
        this.set('defFont1Size', font1);
      }
      if (font2 !== '') {
        this.set('defFont2Size', font2);
      }
      if (font3 !== '') {
        this.set('defFont3Size', font3);
      }
      if (font4 !== '') {
        this.set('defFont4Size', font4);
      }
      if (font5 !== '') {
        this.set('defFont5Size', font5);
      }
    },

    mutatePaperSize(value) {
      this.set('defPaperSize', value);
    },

    mutateBadgeSize(value) {
      if (value === '4.5x4') {
        this.set('previewHeight', true);
      } else {
        this.set('previewHeight', false);
      }
      console.log(this.previewHeight);
      this.set('badgeSize', value);
    },

    togglePreview() {
      this.set('previewToggled', !this.previewToggled);
    }
  }
});
