import Component from '@ember/component';

export default Component.extend({
  input(event) {
    const size = event.target.value;
  }
});
