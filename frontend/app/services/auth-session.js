import Service from '@ember/service';

export default Service.extend({
  sessionToken    : null,
  adminValid      : false,
  isEmailVerified : false,
  permissions     : null,

  init() {
    this._super(...arguments);
  },

  enableAdmin() {
    this.set('adminValid', true);
  },

  toggleAdmin() {
    this.set('adminValid', !this.adminValid);
  },

  setPermission(permissionPayload) {
    this.set('permissions', permissionPayload);
  },

  updateToken(token) {
    this.set('sessionToken', token);
  },

  getToken() {
    return this.get('sessionToken');
  },

  removeToken() {
    this.set('sessionToken', null);
  },

  emailVerified() {
    this.set('isEmailVerified', true);
  }
});
