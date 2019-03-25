import Controller from '@ember/controller';
import ENV from '../config/environment';

import Ember from 'ember';
const { $ } = Ember;

const { APP } = ENV;
import { inject as service } from '@ember/service';

const CreateBadges =  Controller.extend({
  init: () => {
    $.ajax({
      url       : '/images/default_logo.png',
      xhrFields : {
        responseType: 'blob'
      },
      success: (data, defImagedata) => {
        var reader = new FileReader();
        reader.onloadend = function() {
          localStorage.setItem('defImagedata', reader.result);
        };
        reader.readAsDataURL(data);
      }
    });
  },
  routing        : service('-routing'),
  notifications  : service('notification-messages'),
  authToken      : service('auth-session'),
  defColor       : [''],
  backColor      : [''],
  defFontColor   : 'ffffff',
  fontColor      : '',
  defFont1Size   : '10',
  defFont2Size   : '10',
  defFont3Size   : '10',
  defFont4Size   : '10',
  defFont5Size   : '10',
  defFontType1   : 'Helvetica',
  defFontType2   : 'Helvetica',
  defFontType3   : 'Helvetica',
  defFontType4   : 'Helvetica',
  defFontType5   : 'Helvetica',
  defFontCol1    : 'ffffff',
  defFontCol2    : 'ffffff',
  defFontCol3    : 'ffffff',
  defFontCol4    : 'ffffff',
  defFontCol5    : 'ffffff',
  uid            : '',
  textData       : '',
  nameData       : '',
  userError      : '',
  csvFile        : '',
  csvType        : '',
  custImgFile    : [''],
  logoImgFile    : '',
  badgeSize      : '',
  previewToggled : true,
  previewHeight  : '',
  badgeGenerated : false,
  backLink       : APP.backLink,
  defPaperSize   : '',
  genBadge       : '',
  defImageName   : ['red_futuristic'],
  csvEnable      : false,
  manualEnable   : false,
  defImage       : [true],
  custImage      : [false],
  colorImage     : [false],
  custLogoImage  : true,
  overlay        : false,
  showProgress   : false,
  progress       : 0,
  logo_text      : '',
  logoBackColor  : '',
  logoFontColor  : '000',
  progressState  : '',
  firstName      : 'Dominic',
  lastName       : 'Del Piero',
  organization   : 'FOSSASIA',
  socialHandle   : '@dompiero07',
  designation    : 'Social Media Manager',
  prevImageData  : 'https://raw.githubusercontent.com/fossasia/badgeyay/development/frontend/public/images/badge_backgrounds/red_futuristic.png',
  imageData      : ['/images/badge_backgrounds/red_futuristic.png'],
  logoImageData  : '/images/default_logo.png',
  mode           : 'create',
  csvChanged     : false,
  backImgChanged : [false],
  logoImgChanged : false,
  ticketTypes    : [''],

  csvClicked(type) {
    this.set('csvChanged', true);
    this.set('csvEnable', true);
    this.set('csvType', type);
    this.set('manualEnable', false);
  },

  manualClicked() {
    this.set('csvChanged', true);
    this.set('manualEnable', true);
    this.set('csvEnable', false);
    this.set('ticketTypes', ['']);
  },

  defImageClicked(idx) {
    let backImgChanged = this.get('backImgChanged');
    let defImage = this.get('defImage');
    let colorImage = this.get('colorImage');
    let custImage = this.get('custImage');
    let imageData = this.get('imageData');
    backImgChanged.set(idx, true);
    defImage.set(idx, true);
    colorImage.set(idx, false);
    custImage.set(idx, false);
    imageData.set(idx, null);
  },

  bgColorClicked(idx) {
    let backImgChanged = this.get('backImgChanged');
    let defImage = this.get('defImage');
    let colorImage = this.get('colorImage');
    let custImage = this.get('custImage');
    let imageData = this.get('imageData');
    backImgChanged.set(idx, true);
    defImage.set(idx, false);
    colorImage.set(idx, true);
    custImage.set(idx, false);
    imageData.set(idx, null);
  },

  custImgClicked(idx) {
    let backImgChanged = this.get('backImgChanged');
    let defImage = this.get('defImage');
    let colorImage = this.get('colorImage');
    let custImage = this.get('custImage');
    backImgChanged.set(idx, true);
    defImage.set(idx, false);
    colorImage.set(idx, false);
    custImage.set(idx, true);
  },

  actions: {
    defaultlogoimage() {
      this.set('logoImgChanged', true);
      this.set('custLogoImage', true);
      this.set('logoImageData', localStorage.getItem('defImagedata'));
    },
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
        badge_name : '',
        badge_size : '4x3',
        csv_type   : '',
        imageData  : [],
        logo_text  : ''
      };

      if (_this.nameData !== '') {
        badgeData.badge_name = _this.nameData;
      }

      if (_this.badgeSize !== '' && _this.badgeSize !== undefined) {
        badgeData.badge_size = _this.badgeSize;
      }

      if (_this.defPaperSize !== '' && _this.defPaperSize !== undefined) {
        badgeData.paper_size = _this.defPaperSize;
      }

      if (_this.csvEnable || !_this.csvChanged) {
        badgeData.csv = _this.csvFile;
        badgeData.csv_type = _this.csvType;
      }

      if (_this.defFontCol1 !== '' && _this.defFontCol1 !== undefined) {
        badgeData.font_color_1 = '#' + _this.defFontCol1.toString();
        badgeData.font_color_2 = '#' + _this.defFontCol2.toString();
        badgeData.font_color_3 = '#' + _this.defFontCol3.toString();
        badgeData.font_color_4 = '#' + _this.defFontCol4.toString();
        badgeData.font_color_5 = '#' + _this.defFontCol5.toString();
      }

      if (_this.defFont1Size !== '' && _this.defFont1Size !== undefined) {
        badgeData.font_size_1 = _this.defFont1Size.toString();
        badgeData.font_size_2 = _this.defFont2Size.toString();
        badgeData.font_size_3 = _this.defFont3Size.toString();
        badgeData.font_size_4 = _this.defFont4Size.toString();
        badgeData.font_size_5 = _this.defFont5Size.toString();
      }

      if (_this.defFontType1 !== '' && _this.defFontType1 !== undefined) {
        badgeData.font_type_1 = _this.defFontType1;
        badgeData.font_type_2 = _this.defFontType2;
        badgeData.font_type_3 = _this.defFontType3;
        badgeData.font_type_4 = _this.defFontType4;
        badgeData.font_type_5 = _this.defFontType5;
      }

      badgeData.ticket_types = this.get('ticketTypes');

      _this.send('sendManualData', badgeData);

    },

    sendManualData(badgeData) {
      const _this = this;
      if (this.mode === 'edit' && !this.csvChanged) {
        this.send('sendDefaultImg', badgeData);
        this.set('showProgress', true);
        this.set('progress', 40);
        this.set('progressState', 'Gathering background');
        return;
      }
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
          _this.get('notifications').success('Text saved Successfully', {
            autoClear     : true,
            clearDuration : 1500
          });
          this.set('progress', 40);
          this.set('progressState', 'Gathering background');
        }).catch(err => {
          let userErrors = textEntry.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
            userErrors.forEach(error => {
              _this.get('notifications').clearAll();
              _this.get('notifications').error(error.message, {
                autoClear     : true,
                clearDuration : 1500
              });
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
        _this.get('notifications').clearAll();
        _this.get('notifications').error('No Input source specified', {
          autoClear     : true,
          clearDuration : 1500
        });
        this.set('showProgress', false);
        this.set('progress', 0);
      }
    },

    sendDefaultImg(badgeData) {
      const _this = this;
      let promises = [], images = [];
      this.get('ticketTypes').forEach((ticketType, idx) => {
        if (this.mode === 'edit' && !this.backImgChanged[idx]) {
          images.push(this.model.badge.image.split(',')[idx]);
          return;
        }
        if (_this.defImage[idx]) {
          let imageRecord = _this.get('store').createRecord('def-image-upload', {
            uid          : _this.uid,
            defaultImage : _this.defImageName[idx]
          });

          promises.push(imageRecord.save());

        } else if (_this.imageData[idx]) {
          let custImgFile = _this.get('store').createRecord('cust-img-file', {
            uid       : this.uid,
            imageData : this.imageData[idx],
            extension : '.png' });

          promises.push(custImgFile.save());

        } else if (_this.colorImage[idx] && _this.defColor[idx] !== undefined && _this.defColor[idx] !== '') {
          let imageRecord = _this.get('store').createRecord('bg-color', {
            uid      : _this.uid,
            bg_color : _this.defColor[idx]
          });

          promises.push(imageRecord.save());

        } else {
          _this.get('notifications').clearAll();
          _this.get('notifications').error('No background source specified', {
            autoClear     : true,
            clearDuration : 1500
          });
          this.set('showProgress', false);
          this.set('progress', 0);
          this.set('progressState', '');
          return;
        }
      });

      Promise.all(promises)
        .then(records => {
          records.forEach(record => {
            images.push(record.filename);
          });
          badgeData.image = images.join(',');
          _this.set('progress', 60);
          _this.set('progressState', 'Preparing your badges');
          _this.send('sendLogoImg', badgeData);
        })
        .catch(error => {
          let userErrors = this.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
            userErrors.forEach(error => {
              _this.get('notifications').clearAll();
              _this.get('notifications').error(error.message, {
                autoClear     : true,
                clearDuration : 1500
              });
              _this.set('showProgress', false);
              _this.set('progress', 0);
              _this.set('progressState', '');
            });
          }
        });
    },

    sendLogoImg(badgeData) {
      const _this = this;
      if (this.mode === 'edit' && !this.logoImgChanged) {
        this.send('sendBadge', badgeData);
        this.set('showProgress', true);
        this.set('progress', 70);
        this.set('progressState', 'Preparing your badges');
        return;
      }
      if (this.custLogoImage && this.logoImageData) {
        this.get('store').createRecord('cust-img-file', {
          uid       : this.uid,
          imageData : this.logoImageData,
          extension : '.png' })
          .save()
          .then(record => {
            badgeData.logo_image = record.filename;
            _this.send('sendBadge', badgeData);
            this.set('progress', 70);
            this.set('progressState', 'Preparing your badges');
          })
          .catch(error => {
            let userErrors = this.get('errors.user');
            if (userErrors !== undefined) {
              _this.set('userError', userErrors);
              userErrors.forEach(error => {
                _this.get('notifications').clearAll();
                _this.get('notifications').error(error.message, {
                  autoClear     : true,
                  clearDuration : 1500
                });
                this.set('showProgress', false);
                this.set('progress', 0);
                this.set('progressState', '');
              });
            }
          });
      } else if (!_this.custLogoImage && _this.logoBackColor) {
        let imageRecord = _this.get('store').createRecord('bg-color', {
          uid      : _this.uid,
          bg_color : _this.logoBackColor
        });
        imageRecord.save()
          .then(record => {
            badgeData.logo_text = _this.logo_text;
            badgeData.logo_image = record.filename;
            badgeData.logo_color = '#' + _this.logoFontColor;
            _this.send('sendBadge', badgeData);
            this.set('progress', 70);
            this.set('progressState', 'Preparing your badges');
          })
          .catch(error => {
            let userErrors = imageRecord.get('errors.user');
            if (userErrors !== undefined) {
              _this.set('userError', userErrors);
              userErrors.forEach(error => {
                _this.get('notifications').clearAll();
                _this.get('notifications').error(error.message, {
                  autoClear     : true,
                  clearDuration : 1500
                });
                this.set('showProgress', false);
                this.set('progress', 0);
                this.set('progressState', '');
              });
            }
          });
      } else {
        _this.get('notifications').clearAll();
        _this.get('notifications').error('No Logo background source specified', {
          autoClear     : true,
          clearDuration : 1500
        });
        this.set('showProgress', false);
        this.set('progress', 0);
        this.set('progressState', '');
      }
    },

    sendBadge(badgeData) {
      const _this = this;
      if (this.mode === 'edit') {
        let { badge } = this.get('model');
        badge.setProperties(badgeData);
        return badge.save()
          .then(record => {
            this.set('overlay', false);
            this.set('badgeGenerated', true);
            this.set('genBadge', record);
            this.set('progress', 100);
            this.set('progressState', '');
            this.set('badgeGeneratedLink', record.download_link);
          })
          .catch(err => {
            console.log(err);
            _this.set('overlay', false);
            _this.get('notifications').clearAll();
            _this.get('notifications').error('Unable to generate badge', {
              autoClear     : true,
              clearDuration : 1500
            });
            this.set('showProgress', false);
            this.set('progress', 0);
          });
      }
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
          _this.get('notifications').clearAll();
          _this.get('notifications').error('Unable to generate badge', {
            autoClear     : true,
            clearDuration : 1500
          });
          this.set('showProgress', false);
          this.set('progress', 0);
        });
    },

    uploadCSV(csvData) {
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
          _this.get('notifications').clearAll();
          _this.get('notifications').success('CSV uploaded Successfully', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(err => {
          let userErrors = csv_.get('errors.user');
          if (userErrors !== undefined) {
            _this.set('userError', userErrors);
            userErrors.forEach(error => {
              _this.get('notifications').clearAll();
              _this.get('notifications').error(error.message, {
                autoClear     : true,
                clearDuration : 1500
              });
            });
          }
        });
    },

    mutateCSV(csvData) {
      this.csvClicked('basic');
      this.send('uploadCSV', csvData);
    },

    mutateEventyayCSV(csvData) {
      this.csvClicked('eventyay');
      let csv = atob(csvData.substr(21));
      let csvTextLines = csv.split(/\r\n|\n/);
      var headers = csvTextLines[0].split(',');
      let ticketTypes = new Set();
      for (var i = 1; i < csvTextLines.length; i++) {
        var data = csvTextLines[i].split(',');
        if (data.length == headers.length) {
          ticketTypes.add(data[10]);
        }
      }
      console.log(ticketTypes);
      this.set('ticketTypes', [...ticketTypes]);
      this.send('uploadCSV', csvData);
    },

    mutateText(txtData) {
      this.manualClicked();
      this.set('textData', txtData);
      let prevData = txtData.trim().split('\n')[0].split(',');
      this.set('firstName', prevData[0]);
      this.set('lastName', prevData[1]);
      this.set('designation', prevData[2]);
      this.set('organization', prevData[3]);
      this.set('socialHandle', prevData[4]);
    },

    mutateName(namData) {
      this.set('nameData', namData);
    },

    mutateBackground(idx, id) {
      this.defImageClicked(idx);
      let defImageRecord = this.get('store').peekRecord('def-image', id);
      let defImageName = this.get('defImageName');
      defImageName.set(idx, defImageRecord.name);
    },

    mutateDefColor(idx, color) {
      this.bgColorClicked(idx);
      let defColor = this.get('defColor');
      let backColor = this.get('backColor');
      defColor.set(idx, color);
      backColor.set(idx, color);
    },

    mutateLogoFontColor(color) {
      console.log(color);
      this.set('logoFontColor', color);
    },

    mutateLogoBackColor(color) {
      console.log(color);
      this.set('logoBackColor', color);
    },

    mutateCustomImage(idx, image) {
      this.custImgClicked(idx);
      let imageData = this.get('imageData');
      imageData.set(idx, image);
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


    mutateCustomFont(values) {
      const [fonttype1, fonttype2, fonttype3, fonttype4, fonttype5] = values;
      if (fonttype1 !== '') {
        this.set('defFontType1', fonttype1);
      }
      if (fonttype2 !== '') {
        this.set('defFontType2', fonttype2);
      }
      if (fonttype3 !== '') {
        this.set('defFontType3', fonttype3);
      }
      if (fonttype4 !== '') {
        this.set('defFontType4', fonttype4);
      }
      if (fonttype5 !== '') {
        this.set('defFontType5', fonttype5);
      }
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
        this.set('previewHeight', false);
      } else {
        this.set('previewHeight', true);
      }
      this.set('badgeSize', value);
    },
    mutateFontCol(values) {
      const [font1, font2, font3, font4, font5] = values;
      if (font1 !== '') {
        this.set('defFontCol1', font1);
      }
      if (font2 !== '') {
        this.set('defFontCol2', font2);
      }
      if (font3 !== '') {
        this.set('defFontCol3', font3);
      }
      if (font4 !== '') {
        this.set('defFontCol4', font4);
      }
      if (font5 !== '') {
        this.set('defFontCol5', font5);
      }

    },

    customlogoimage() {
      this.set('custLogoImage', true);
      this.set('logoImgChanged', true);
      this.set('logo_text', '');
      document.getElementById('custlogoimg').style.display = 'block';
      document.getElementById('custlogocol').style.display = 'none';
    },

    customlogocol() {
      this.set('custLogoImage', false);
      this.set('logoImgChanged', true);
      document.getElementById('custlogoimg').style.display = 'none';
      document.getElementById('custlogocol').style.display = 'block';
    },

    togglePreview() {
      this.set('previewToggled', !this.previewToggled);
      document.getElementsByClassName('checkswitch')[0].checked = !document.getElementsByClassName('checkswitch')[0].checked;
    }

  }
});

export default CreateBadges;
