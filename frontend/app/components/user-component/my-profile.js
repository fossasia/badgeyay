import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  actions: {
    updateProfileImage() {
      document.getElementById('profileImageSelector').click();
    },

    profileImageSelected(event) {
      const reader = new FileReader();
      const { target } = event;
      const { files } = target;
      const [file] = files;
      const _this = this;

      reader.onload = () => {
        _this.get('sendProfileImage')(reader.result, file.type.split('/')[1]);
      };

      reader.readAsDataURL(file);
    }
  }
});
