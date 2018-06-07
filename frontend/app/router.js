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
  this.route('not-found');
  this.route('not-found-catch', { path: '/*path' });
  this.route('my-profile');
});

export default router;
