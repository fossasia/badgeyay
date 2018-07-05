/* jshint strict:false */

import Ember from 'ember';
import config from './config/environment';

const { Router } = Ember;

const router = Router.extend({
  location : config.locationType,
  rootURL  : config.rootURL
});

router.map(function() {
  this.route('login');
  this.route('signup');
  this.route('create-badges');
  this.route('my-badges');
  this.route('not-found');
  this.route('not-found-catch', { path: '/*path' });
  this.route('my-profile');
  this.route('forgotpwd');

  this.route('reset', function() {
    this.route('password');
  });
  this.route('user-guide');
  this.route('verify', function() {
    this.route('email');
  });
  this.route('admin', function() {
    this.route('users', function() {
      this.route('list', { path: '/:users_status' });
      this.route('view');
    });
    this.route('reports');
    this.route('settings');
    this.route('permissions', function() {
      this.route('system-roles');
    });
    this.route('modules');
    this.route('content', function() {
      this.route('system-images');
    });
  });
});

export default router;
