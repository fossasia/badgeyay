/* eslint-env node */

module.exports = function(environment) {
  var ENV = {
    modulePrefix : 'badgeyay',
    environment,
    rootURL      : '/',
    locationType : 'auto',
    firebase     : {
      apiKey            : 'AIzaSyBZ6M-nLfy-Ig8esqfQmFn8FtF1OQ73VGQ',
      authDomain        : 'badgeyay-195bf.firebaseapp.com',
      databaseURL       : 'https://badgeyay-195bf.firebaseio.com',
      projectId         : 'badgeyay-195bf',
      storageBucket     : 'badgeyay-195bf.appspot.com',
      messagingSenderId : '1033576063262'
    },
    'ember-cli-notifications': {
      includeFontAwesome: true
    },
    torii: {
      sessionServiceName: 'session'
    },
    pace: {
      // addon-specific options to configure theme
      theme : 'minimal',
      color : 'orange'
    },
    contentSecurityPolicy: {
      'script-src'  : '\'self\' \'unsafe-eval\' apis.google.com',
      'frame-src'   : '\'self\' https://*.firebaseapp.com',
      'connect-src' : '\'self\' wss://*.firebaseio.com https://*.googleapis.com'
    },
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      },
      EXTEND_PROTOTYPES: {
        // Prevent Ember Data from overriding Date.parse.
        Date: false
      }
    },
    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
      backLink      : 'http://localhost:5000',
      resetFunction : 'http://localhost:8090/badgeyay-195bf/us-central1/sendResetMail'
    }
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
    ENV.APP.autoboot = false;
  }

  var deployTarget = process.env.DEPLOY_TARGET;

  if (environment === 'production') {
    ENV.APP.backLink = 'https://badgeyay-api.herokuapp.com';
    ENV.APP.resetFunction = 'https://us-central1-badgeyay-195bf.cloudfunctions.net/sendResetMail';
    if (deployTarget && deployTarget === 'gh-pages') {
      ENV.locationType = 'hash';
      ENV.rootURL = `/${process.env.REPO_SLUG || 'badgeyay'}`;
    }
  }

  return ENV;
};
