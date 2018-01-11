"use strict";



define('badgeyay-frontend/app', ['exports', 'badgeyay-frontend/resolver', 'ember-load-initializers', 'badgeyay-frontend/config/environment'], function (exports, _resolver, _emberLoadInitializers, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  var App = Ember.Application.extend({
    modulePrefix: _environment.default.modulePrefix,
    podModulePrefix: _environment.default.podModulePrefix,
    Resolver: _resolver.default
  });

  (0, _emberLoadInitializers.default)(App, _environment.default.modulePrefix);

  exports.default = App;
});
define('badgeyay-frontend/components/badge-front', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Component.extend({
    didInsertElement: function didInsertElement() {
      this._super.apply(this, arguments);
      var elemnt = this.$('#colorpick');
      elemnt.colpick({
        layout: 'hex',
        submit: 0,
        colorScheme: 'light',
        onChange: function onChange(hsb, hex, rgb, el, bySetColor) {
          elemnt.css('border-color', '#' + hex);
          // Fill the text box just if the color was set using the picker, and not the colpickSetColor function.
          if (!bySetColor) elemnt.val("#" + hex);
        }
      }).keyup(function () {
        elemnt.colpickSetColor(this.$('#colorpick').value);
      });
    },


    /* listening for events  */
    actions: {

      /* data source radio selection changed */
      datasourceChanged: function datasourceChanged(source) {
        if (source == 'csv') {
          /*  Show the csv task*/
          this.$(".csv-upload").css({
            'display': 'block'
          });
          this.$(".manual-data").css({
            'display': 'none'
          });
        } else if (source == 'manual') {
          /*  Show the manual task*/
          this.$(".manual-data").css({
            'display': 'block'
          });
          this.$(".csv-upload").css({
            'display': 'none'
          });
        }
      },


      /* background source radio chaned events*/
      backgroundsourceChanged: function backgroundsourceChanged(source) {
        if (source == 'png') {
          /*  Show current task*/
          this.$(".png-background").css({
            'display': 'block'
          });
          this.$(".default-image-background").css({
            'display': 'none'
          });
          this.$(".custom-background").css({
            'display': 'none'
          });
        } else if (source == 'defaults') {
          this.$(".png-background").css({
            'display': 'none'
          });
          this.$(".default-image-background").css({
            'display': 'block'
          });
          this.$(".custom-background").css({
            'display': 'none'
          });
        } else if (source == 'color') {
          this.$(".png-background").css({
            'display': 'none'
          });
          this.$(".default-image-background").css({
            'display': 'none'
          });
          this.$(".custom-background").css({
            'display': 'block'
          });
        }
      },


      /* text source radio changed  event */
      textsourceChanged: function textsourceChanged(source) {
        if (source == 'text') {
          /*  Show the text task*/
          this.$(".custom-text").css({
            'display': 'block'
          });
          this.$(".config-json").css({
            'display': 'none'
          });
        } else if (source == 'json') {
          /*  Show the json task*/
          this.$(".config-json").css({
            'display': 'block'
          });
          this.$(".custom-text").css({
            'display': 'none'
          });
        }
      }
    }

  });
});
define('badgeyay-frontend/components/stylish-button', ['exports', 'ember-stylish-buttons/components/stylish-button', 'badgeyay-frontend/config/environment'], function (exports, _stylishButton, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  var config = _environment.default['ember-stylish-buttons'] || {};

  exports.default = _stylishButton.default.extend({
    type: config.defaultTheme || 'winona'
  });
});
define('badgeyay-frontend/components/welcome-page', ['exports', 'ember-welcome-page/components/welcome-page'], function (exports, _welcomePage) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _welcomePage.default;
    }
  });
});
define('badgeyay-frontend/helpers/app-version', ['exports', 'badgeyay-frontend/config/environment', 'ember-cli-app-version/utils/regexp'], function (exports, _environment, _regexp) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.appVersion = appVersion;
  var version = _environment.default.APP.version;
  function appVersion(_) {
    var hash = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};

    if (hash.hideSha) {
      return version.match(_regexp.versionRegExp)[0];
    }

    if (hash.hideVersion) {
      return version.match(_regexp.shaRegExp)[0];
    }

    return version;
  }

  exports.default = Ember.Helper.helper(appVersion);
});
define('badgeyay-frontend/helpers/pluralize', ['exports', 'ember-inflector/lib/helpers/pluralize'], function (exports, _pluralize) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _pluralize.default;
});
define('badgeyay-frontend/helpers/singularize', ['exports', 'ember-inflector/lib/helpers/singularize'], function (exports, _singularize) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _singularize.default;
});
define('badgeyay-frontend/initializers/app-version', ['exports', 'ember-cli-app-version/initializer-factory', 'badgeyay-frontend/config/environment'], function (exports, _initializerFactory, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  var name = void 0,
      version = void 0;
  if (_environment.default.APP) {
    name = _environment.default.APP.name;
    version = _environment.default.APP.version;
  }

  exports.default = {
    name: 'App Version',
    initialize: (0, _initializerFactory.default)(name, version)
  };
});
define('badgeyay-frontend/initializers/container-debug-adapter', ['exports', 'ember-resolver/resolvers/classic/container-debug-adapter'], function (exports, _containerDebugAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: 'container-debug-adapter',

    initialize: function initialize() {
      var app = arguments[1] || arguments[0];

      app.register('container-debug-adapter:main', _containerDebugAdapter.default);
      app.inject('container-debug-adapter:main', 'namespace', 'application:main');
    }
  };
});
define('badgeyay-frontend/initializers/data-adapter', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: 'data-adapter',
    before: 'store',
    initialize: function initialize() {}
  };
});
define('badgeyay-frontend/initializers/ember-data', ['exports', 'ember-data/setup-container', 'ember-data'], function (exports, _setupContainer) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: 'ember-data',
    initialize: _setupContainer.default
  };
});
define('badgeyay-frontend/initializers/export-application-global', ['exports', 'badgeyay-frontend/config/environment'], function (exports, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.initialize = initialize;
  function initialize() {
    var application = arguments[1] || arguments[0];
    if (_environment.default.exportApplicationGlobal !== false) {
      var theGlobal;
      if (typeof window !== 'undefined') {
        theGlobal = window;
      } else if (typeof global !== 'undefined') {
        theGlobal = global;
      } else if (typeof self !== 'undefined') {
        theGlobal = self;
      } else {
        // no reasonable global, just bail
        return;
      }

      var value = _environment.default.exportApplicationGlobal;
      var globalName;

      if (typeof value === 'string') {
        globalName = value;
      } else {
        globalName = Ember.String.classify(_environment.default.modulePrefix);
      }

      if (!theGlobal[globalName]) {
        theGlobal[globalName] = application;

        application.reopen({
          willDestroy: function willDestroy() {
            this._super.apply(this, arguments);
            delete theGlobal[globalName];
          }
        });
      }
    }
  }

  exports.default = {
    name: 'export-application-global',

    initialize: initialize
  };
});
define('badgeyay-frontend/initializers/injectStore', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: 'injectStore',
    before: 'store',
    initialize: function initialize() {}
  };
});
define('badgeyay-frontend/initializers/store', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: 'store',
    after: 'ember-data',
    initialize: function initialize() {}
  };
});
define('badgeyay-frontend/initializers/transforms', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: 'transforms',
    before: 'store',
    initialize: function initialize() {}
  };
});
define("badgeyay-frontend/instance-initializers/ember-data", ["exports", "ember-data/instance-initializers/initialize-store-service"], function (exports, _initializeStoreService) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: "ember-data",
    initialize: _initializeStoreService.default
  };
});
define('badgeyay-frontend/resolver', ['exports', 'ember-resolver'], function (exports, _emberResolver) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberResolver.default;
});
define('badgeyay-frontend/router', ['exports', 'badgeyay-frontend/config/environment'], function (exports, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  var Router = Ember.Router.extend({
    location: _environment.default.locationType,
    rootURL: _environment.default.rootURL
  });

  Router.map(function () {
    this.route('app');
  });

  exports.default = Router;
});
define('badgeyay-frontend/services/ajax', ['exports', 'ember-ajax/services/ajax'], function (exports, _ajax) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _ajax.default;
    }
  });
});
define("badgeyay-frontend/templates/application", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "clXWZaa9", "block": "{\"symbols\":[],\"statements\":[[6,\"div\"],[9,\"class\",\"background\"],[7],[0,\"\\n\"],[6,\"h1\"],[9,\"style\",\"text-align: center;\"],[9,\"class\",\"style\"],[7],[0,\"BADGEYAY\"],[8],[0,\"\\n  \"],[1,[18,\"badge-front\"],false],[0,\"\\n\"],[8],[0,\"\\n\"],[1,[18,\"outlet\"],false]],\"hasEval\":false}", "meta": { "moduleName": "badgeyay-frontend/templates/application.hbs" } });
});
define("badgeyay-frontend/templates/components/badge-front", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "k1w9e4tc", "block": "{\"symbols\":[\"&default\"],\"statements\":[[11,1],[0,\"\\n\"],[6,\"link\"],[9,\"href\",\"https://fonts.googleapis.com/css?family=Roboto+Slab:700\"],[9,\"rel\",\"stylesheet\"],[7],[8],[0,\"\\n\"],[6,\"link\"],[9,\"rel\",\"stylesheet\"],[9,\"href\",\"https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css\"],[7],[8],[0,\"\\n\"],[6,\"link\"],[9,\"rel\",\"stylesheet\"],[9,\"href\",\"button/css/style.css\"],[7],[8],[0,\"\\n\\n\"],[6,\"script\"],[9,\"src\",\"js/color.js\"],[7],[8],[0,\"\\n\\n\"],[6,\"link\"],[9,\"rel\",\"stylesheet\"],[9,\"href\",\"https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css\"],[7],[8],[0,\"\\n\"],[6,\"link\"],[9,\"rel\",\"stylesheet\"],[9,\"href\",\"textarea/css/style.css\"],[7],[8],[0,\"\\n\"],[6,\"script\"],[9,\"src\",\"textarea/js/index.js\"],[7],[8],[0,\"\\n\\n\\n\"],[6,\"link\"],[9,\"rel\",\"stylesheet\"],[9,\"href\",\"toggle/css/style.css\"],[7],[8],[0,\"\\n\\n\\n\"],[6,\"div\"],[9,\"id\",\"app\"],[7],[0,\"\\n  \"],[6,\"form\"],[9,\"action\",\"\"],[7],[0,\"\\n    \"],[6,\"div\"],[9,\"class\",\"pad\"],[7],[0,\"\\n\\n\"],[0,\"  \"],[6,\"div\"],[9,\"style\",\"width:100%\"],[9,\"id\",\"r8-balloon-radio\"],[9,\"class\",\"container\"],[7],[0,\"\\n    \"],[6,\"p\"],[9,\"style\",\"font-family: 'Bungee';\"],[7],[0,\"Choose your Data Source\"],[8],[6,\"p\"],[9,\"style\",\"font-family: 'Bangers';\"],[7],[6,\"br\"],[7],[8],[6,\"br\"],[7],[8],[0,\"\\n    \"],[6,\"ul\"],[7],[0,\"\\n        Add CSV file                 \"],[6,\"li\"],[7],[6,\"input\"],[9,\"id\",\"csv\"],[9,\"class\",\"radio r8-radio-float\"],[9,\"type\",\"radio\"],[9,\"name\",\"data-source\"],[9,\"value\",\"0\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"datasourceChanged\",\"csv\"],null],null],[7],[8],[8],[6,\"br\"],[7],[8],[0,\"\\n        Enter Data Manually \"],[6,\"li\"],[7],[6,\"input\"],[9,\"id\",\"manual\"],[9,\"class\",\"radio r8-radio-float\"],[9,\"type\",\"radio\"],[9,\"name\",\"data-source\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"datasourceChanged\",\"manual\"],null],null],[9,\"value\",\"1\"],[7],[8],[8],[0,\"\\n      \"],[8],[0,\"\\n    \"],[8],[6,\"br\"],[7],[8],[6,\"br\"],[7],[8],[0,\"\\n  \"],[8],[0,\"\\n\"],[6,\"section\"],[9,\"class\",\"csv-upload\"],[7],[0,\"\\n        \"],[6,\"p\"],[9,\"style\",\"font-family: 'Chewy';\"],[7],[0,\"Add CSV file containing fields Name,Organization and Handle\"],[8],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"file\"],[9,\"name\",\"csv-file\"],[9,\"id\",\"csv-file-upload\"],[7],[8],[0,\"\\n\"],[8],[0,\"\\n\"],[6,\"section\"],[9,\"class\",\"manual-data\"],[7],[0,\"\\n        \"],[6,\"p\"],[9,\"style\",\"font-family: 'Chewy';\"],[7],[0,\"Enter One Name per Line\"],[8],[0,\"\\n        \"],[6,\"textarea\"],[9,\"style\",\"resize: none;width:100%\"],[9,\"name\",\"names-csv\"],[9,\"id\",\"names-csv\"],[9,\"placeholder\",\"Eg. Hong Phuc,Dang,@hpdang,FOSSASIA \"],[7],[8],[0,\"\\n\"],[8],[0,\"\\n\\n\\n\"],[0,\"\\n\"],[6,\"div\"],[9,\"style\",\"width:100%\"],[9,\"id\",\"r8-balloon-radio\"],[9,\"class\",\"container\"],[7],[0,\"\\n    \"],[6,\"p\"],[9,\"style\",\"font-family: 'Bungee';\"],[7],[0,\"Choose your Badge Background\"],[8],[6,\"p\"],[9,\"style\",\"font-family: 'Bangers';\"],[7],[6,\"br\"],[7],[8],[6,\"br\"],[7],[8],[0,\"\\n    \"],[6,\"ul\"],[7],[0,\"\\n        Add PNG file         \"],[6,\"li\"],[7],[6,\"input\"],[9,\"class\",\"radio r8-radio-float\"],[9,\"type\",\"radio\"],[9,\"value\",\"0\"],[9,\"id\",\"png-image\"],[9,\"name\",\"badge-background\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"backgroundsourceChanged\",\"png\"],null],null],[7],[8],[8],[6,\"br\"],[7],[8],[0,\"\\n        Add Default Image\"],[6,\"li\"],[7],[6,\"input\"],[9,\"class\",\"radio r8-radio-float\"],[9,\"type\",\"radio\"],[9,\"id\",\"default-image\"],[9,\"name\",\"badge-background\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"backgroundsourceChanged\",\"defaults\"],null],null],[9,\"value\",\"1\"],[7],[8],[8],[6,\"br\"],[7],[8],[0,\"\\n\\t\\tAdd Custom color \"],[6,\"li\"],[7],[6,\"input\"],[9,\"class\",\"radio r8-radio-float\"],[9,\"type\",\"radio\"],[9,\"id\",\"background-custom\"],[9,\"name\",\"badge-background\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"backgroundsourceChanged\",\"color\"],null],null],[9,\"value\",\"2\"],[7],[8],[8],[0,\"\\n      \"],[8],[0,\"\\n    \"],[8],[0,\"\\n\"],[8],[0,\"\\n\\n\"],[6,\"section\"],[9,\"class\",\"png-background\"],[7],[0,\"\\n        \"],[6,\"p\"],[7],[0,\"Upload a PNG file for badge background\"],[8],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"file\"],[9,\"name\",\"png-background-file\"],[9,\"id\",\"csv-file-upload\"],[7],[8],[0,\"\\n\"],[8],[0,\"\\n\\n\"],[6,\"section\"],[9,\"class\",\"custom-background\"],[7],[0,\"\\n\"],[0,\"\\t\"],[6,\"br\"],[7],[8],[6,\"div\"],[9,\"id\",\"wrapper\"],[9,\"style\",\"min-height: 100%;\\n  display: flex;\\n  flex-direction: column;\\n  justify-content: center;\\n  align-items: center;\\n  background-color: #aaa;\"],[7],[0,\"\\n\\t\\t\"],[6,\"input\"],[9,\"id\",\"in\"],[9,\"type\",\"color\"],[9,\"value\",\"#ffffff\"],[9,\"oninput\",\"changeColor()\"],[9,\"style\",\"background-color: #ffffff;\\n  width: 150px;\\n  height: 30px;\\n  border: 10px outset #222;\\n  border-radius: 15px;\\n  padding: none;\"],[7],[8],[0,\"\\n\\t\"],[8],[0,\"\\n\"],[8],[0,\"\\n\\t  \\n\"],[6,\"div\"],[9,\"style\",\"width:100%\"],[9,\"id\",\"r8-balloon-radio\"],[9,\"class\",\"container\"],[7],[0,\"\\n      \"],[6,\"br\"],[7],[8],[6,\"br\"],[7],[8],[6,\"p\"],[9,\"style\",\"font-family: 'Bungee';\"],[7],[0,\"Customise Badges (Optional)\"],[8],[6,\"p\"],[9,\"style\",\"font-family: 'Bangers';\"],[7],[6,\"br\"],[7],[8],[6,\"br\"],[7],[8],[0,\"\\n      \"],[6,\"ul\"],[7],[0,\"\\n        Add Custom text\"],[6,\"li\"],[7],[6,\"input\"],[9,\"class\",\"radio r8-radio-float\"],[9,\"type\",\"radio\"],[9,\"id\",\"text\"],[9,\"name\",\"text-source\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"textsourceChanged\",\"text\"],null],null],[9,\"value\",\"0\"],[7],[8],[8],[6,\"br\"],[7],[8],[0,\"\\n        Add JSON file        \"],[6,\"li\"],[7],[6,\"input\"],[9,\"class\",\"radio r8-radio-float\"],[9,\"type\",\"radio\"],[9,\"id\",\"json\"],[9,\"name\",\"text-source\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"textsourceChanged\",\"json\"],null],null],[9,\"value\",\"1\"],[7],[8],[8],[6,\"br\"],[7],[8],[0,\"\\n      \"],[8],[0,\"\\n\\t  \"],[8],[6,\"br\"],[7],[8],[0,\"\\n\"],[8],[0,\"\\n\\n\\n\"],[6,\"section\"],[9,\"class\",\"custom-text\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"text\"],[9,\"name\",\"custom-text\"],[9,\"id\",\"custom-text\"],[9,\"placeholder\",\"The text entered here will appear on badges\"],[7],[8],[0,\"\\n\"],[8],[0,\"\\n\"],[6,\"section\"],[9,\"class\",\"config-json\"],[7],[0,\"\\n        \"],[6,\"p\"],[9,\"style\",\"font-family: 'Chewy';\"],[7],[0,\"Upload a config file.\"],[8],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"file\"],[9,\"name\",\"config-json-file\"],[9,\"id\",\"config-json-file\"],[7],[8],[0,\"\\n\"],[8],[0,\"\\n    \"],[8],[0,\"\\n\"],[6,\"div\"],[9,\"class\",\"button\"],[7],[0,\"\\n      \"],[6,\"a\"],[9,\"href\",\"loading.html\"],[9,\"id\",\"preview\"],[7],[6,\"button\"],[9,\"style\",\"font-family: 'Bangers';width:100%\"],[9,\"class\",\"btn draw-border\"],[7],[0,\"Preview Badges!\"],[8],[8],[0,\"\\n    \"],[8],[0,\"\\n      \"],[6,\"div\"],[7],[0,\"\\n\\t  \\t\"],[6,\"p\"],[9,\"style\",\"font-family: 'Bangers';font-size: 25px !important;\"],[7],[0,\"Finalize Badges?\"],[8],[0,\"\\n        \"],[6,\"input\"],[9,\"onclick\",\"finalize()\"],[9,\"type\",\"checkbox\"],[9,\"id\",\"pure-toggle-2\"],[9,\"hidden\",\"\"],[7],[8],[0,\"\\n        \"],[6,\"label\"],[9,\"class\",\"pure-toggle impossible\"],[9,\"for\",\"pure-toggle-2\"],[7],[6,\"span\"],[9,\"class\",\"fontawesome-remove\"],[7],[8],[6,\"span\"],[9,\"class\",\"fontawesome-ok\"],[7],[8],[8],[0,\"\\n      \"],[8],[0,\"\\n\"],[8],[0,\"\\n    \"],[6,\"div\"],[9,\"class\",\"button\"],[7],[0,\"\\n      \"],[6,\"a\"],[9,\"href\",\"loading.html\"],[9,\"style\",\"display: none;\"],[9,\"id\",\"gen\"],[7],[6,\"button\"],[9,\"style\",\"width:100%\"],[9,\"class\",\"btn draw-border\"],[7],[0,\"Generate Badges!\"],[8],[8],[0,\"\\n    \"],[8],[0,\"\\n\"],[6,\"div\"],[9,\"id\",\"r8-logo-coin\"],[7],[8],[0,\"\\n\"],[8],[0,\"\\n\\n\\n\"],[6,\"script\"],[7],[0,\"\\nfunction finalize() {\\n    var x = document.getElementById(\\\"gen\\\");\\n    if (x.style.display === \\\"none\\\") {\\n        x.style.display = \\\"block\\\";\\n    } else {\\n        x.style.display = \\\"none\\\";\\n    }\\n}\\n\"],[8]],\"hasEval\":false}", "meta": { "moduleName": "badgeyay-frontend/templates/components/badge-front.hbs" } });
});


define('badgeyay-frontend/config/environment', [], function() {
  var prefix = 'badgeyay-frontend';
try {
  var metaName = prefix + '/config/environment';
  var rawConfig = document.querySelector('meta[name="' + metaName + '"]').getAttribute('content');
  var config = JSON.parse(unescape(rawConfig));

  var exports = { 'default': config };

  Object.defineProperty(exports, '__esModule', { value: true });

  return exports;
}
catch(err) {
  throw new Error('Could not read config from meta tag with name "' + metaName + '".');
}

});

if (!runningTests) {
  require("badgeyay-frontend/app")["default"].create({"name":"badgeyay-frontend","version":"0.0.0+ef13451d"});
}
//# sourceMappingURL=badgeyay-frontend.map
