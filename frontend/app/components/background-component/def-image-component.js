import Component from '@ember/component';

export default Component.extend({
  init() {
    // To be inflated from the backend data
    this.image = '';
    // this.images = [{ 'id': 0, 'name': 'Test 0' }, { 'id': 1, 'name': 'Test 1' }];
    return this._super(...arguments);
  }
});

