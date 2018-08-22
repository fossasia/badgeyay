'use strict';

const EmberApp = require('ember-cli/lib/broccoli/ember-app');
const writeFile = require('broccoli-file-creator');
const MergeTrees = require('broccoli-merge-trees');
const Funnel = require('broccoli-funnel');
const md5 = require('md5');

module.exports = function(defaults) {
  const fingerprintHash = md5(Date.now());

  let app = new EmberApp(defaults, {
    // Add options here
    'ember-cli-babel': {
      includePolyfill: true
    },
    fingerprint: {
      extensions : ['js', 'css', 'png'], // list of extensions to fingerprint
      customHash : fingerprintHash // use a single fingeprint/hash for all assets
    }
  });

  app.import('bower_components/Croppie/croppie.css');
  app.import('bower_components/Croppie/croppie.min.js');
  // Use `app.import` to add additional libraries to the generated
  // output files.
  //
  // If you need to use different assets in different
  // environments, specify an object as the first parameter. That
  // object's keys should be the environment name and the values
  // should be the asset to use in that environment.
  //
  // If the library that you are including contains AMD or ES6
  // modules that you would like to import into your application
  // please specify an object with the list of modules as keys
  // along with the exports of each module as its value.

  var assetFingerprintTree = writeFile('./assets/assets-fingerprint.js', `(function(_window){ _window.ASSET_FINGERPRINT_HASH = "${(app.env === 'production' ? `-${fingerprintHash}` : '')}"; })(window);`);
  var appTree = app.toTree(assetFingerprintTree);
  return new MergeTrees([appTree, new Funnel(appTree, {
    files: ['index.html'],
    getDestinationPath() {
      return '404.html';
    }
  })]);
};
