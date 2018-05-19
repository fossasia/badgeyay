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
});

export default router;
