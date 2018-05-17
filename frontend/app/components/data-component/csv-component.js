import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  actions: {

    encodeCSV(event) {
      const reader = new FileReader();
      const { target } = event;
      const { files } = target;
      const [file] = files;
      const _this = this;

      reader.onload = () => {
        _this.get('sendCSV')(reader.result);
      };

      reader.readAsDataURL(file);
    }
  }
});
