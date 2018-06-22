import Service from '@ember/service';

export default Service.extend({
  sessionToken: null,

  init() {
    this._super(...arguments);
  },

  updateToken(token) {
    this.set('sessionToken', token);
  },

  getToken() {
    return this.get('sessionToken');
  },

  removeToken() {
    this.set('sessionToken', null);
  }
});
