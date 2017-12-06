"use strict";



define('badgeyay-frontend/app', ['exports', 'badgeyay-frontend/resolver', 'ember-load-initializers', 'badgeyay-frontend/config/environment'], function (exports, _resolver, _emberLoadInitializers, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  var Application = Ember.Application;


  var App = Application.extend({
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
  var Component = Ember.Component;
  exports.default = Component.extend({
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
  var EmberRouter = Ember.Router;


  var Router = EmberRouter.extend({
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
  exports.default = Ember.HTMLBars.template({ "id": "lbSGBmCN", "block": "{\"symbols\":[],\"statements\":[[6,\"div\"],[9,\"class\",\"backgorund\"],[7],[0,\"\\n  \"],[6,\"div\"],[9,\"class\",\"flex\"],[7],[0,\"\\n  \"],[6,\"h2\"],[7],[0,\"BadgeYAY\"],[8],[0,\"\\n  \"],[6,\"div\"],[9,\"class\",\"menu\"],[7],[0,\"\\n    \\n  \"],[8],[0,\"\\n\"],[8],[0,\"\\n  \"],[1,[18,\"badge-front\"],false],[0,\"\\n\"],[8],[0,\"\\n\"],[1,[18,\"outlet\"],false]],\"hasEval\":false}", "meta": { "moduleName": "badgeyay-frontend/templates/application.hbs" } });
});
define("badgeyay-frontend/templates/components/badge-front", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "gxfItNP0", "block": "{\"symbols\":[\"&default\"],\"statements\":[[11,1],[0,\"\\n\\n\"],[6,\"div\"],[9,\"id\",\"app\"],[7],[0,\"\\n  \"],[6,\"form\"],[9,\"action\",\"\"],[7],[0,\"\\n    \"],[6,\"div\"],[9,\"class\",\"pad\"],[7],[0,\"\\n\\n\"],[0,\"      \"],[6,\"p\"],[7],[0,\"Choose your Data Source\"],[8],[0,\"\\n      \"],[6,\"label\"],[9,\"class\",\"fieldset\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"radio\"],[9,\"id\",\"csv\"],[9,\"name\",\"data-source\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"datasourceChanged\",\"csv\"],null],null],[7],[8],[0,\"\\n        Add CSV file\\n      \"],[8],[0,\"\\n      \"],[6,\"label\"],[9,\"class\",\"fieldset\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"radio\"],[9,\"id\",\"manual\"],[9,\"name\",\"data-source\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"datasourceChanged\",\"manual\"],null],null],[7],[8],[0,\"\\n        Enter Data Manually\\n      \"],[8],[0,\"\\n\"],[0,\"      \"],[6,\"section\"],[9,\"class\",\"csv-upload\"],[7],[0,\"\\n        \"],[6,\"p\"],[7],[0,\"Add CSV file containing fields Name,Organization and Handle\"],[8],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"file\"],[9,\"name\",\"csv-file\"],[9,\"id\",\"csv-file-upload\"],[7],[8],[0,\"\\n      \"],[8],[0,\"\\n      \"],[6,\"scetion\"],[9,\"class\",\"manual-data\"],[7],[0,\"\\n        \"],[6,\"p\"],[7],[0,\"Enter One Name per Line\"],[8],[0,\"\\n        \"],[6,\"textarea\"],[9,\"name\",\"names-csv\"],[9,\"id\",\"names-csv\"],[9,\"placeholder\",\"Eg. Hong Phuc,Dang,@hpdang,FOSSASIA \"],[7],[8],[0,\"\\n      \"],[8],[0,\"\\n\\n\\n\"],[0,\"      \"],[6,\"p\"],[7],[0,\"Choose your Badge Background\"],[8],[0,\"\\n      \"],[6,\"label\"],[9,\"class\",\"fieldset\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"radio\"],[9,\"id\",\"png-image\"],[9,\"name\",\"badge-background\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"backgroundsourceChanged\",\"png\"],null],null],[7],[8],[0,\"\\n        Add PNG file\\n      \"],[8],[0,\"\\n      \"],[6,\"label\"],[9,\"class\",\"fieldset\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"radio\"],[9,\"id\",\"default-image\"],[9,\"name\",\"badge-background\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"backgroundsourceChanged\",\"defaults\"],null],null],[7],[8],[0,\"\\n        Add Default Image\\n      \"],[8],[0,\"\\n      \"],[6,\"label\"],[9,\"class\",\"fieldset\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"radio\"],[9,\"id\",\"background-custom\"],[9,\"name\",\"badge-background\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"backgroundsourceChanged\",\"color\"],null],null],[7],[8],[0,\"\\n        Add Background with custom color\\n      \"],[8],[0,\"\\n\"],[0,\"      \"],[6,\"section\"],[9,\"class\",\"png-background\"],[7],[0,\"\\n        \"],[6,\"p\"],[7],[0,\"Upload a PNG file for badge background\"],[8],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"file\"],[9,\"name\",\"png-background-file\"],[9,\"id\",\"csv-file-upload\"],[7],[8],[0,\"\\n      \"],[8],[0,\"\\n      \"],[6,\"section\"],[9,\"class\",\"default-image-background\"],[7],[0,\"\\n\"],[0,\"      \"],[8],[0,\"\\n      \"],[6,\"section\"],[9,\"class\",\"custom-background\"],[7],[0,\"\\n\"],[0,\"        \"],[6,\"div\"],[9,\"class\",\"ColorPicker\"],[7],[0,\"\\n          \"],[6,\"input\"],[9,\"type\",\"text\"],[9,\"id\",\"colorpick\"],[7],[8],[0,\"\\n        \"],[8],[0,\"\\n      \"],[8],[0,\"\\n\\n\\n\"],[0,\"      \"],[6,\"p\"],[7],[0,\"Customise Badges (Optional)\"],[8],[0,\"\\n      \"],[6,\"label\"],[9,\"class\",\"fieldset\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"radio\"],[9,\"id\",\"text\"],[9,\"name\",\"text-source\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"textsourceChanged\",\"text\"],null],null],[7],[8],[0,\"\\n        Add Custom text\\n      \"],[8],[0,\"\\n      \"],[6,\"label\"],[9,\"class\",\"fieldset\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"radio\"],[9,\"id\",\"json\"],[9,\"name\",\"text-source\"],[10,\"onclick\",[25,\"action\",[[19,0,[]],\"textsourceChanged\",\"json\"],null],null],[7],[8],[0,\"\\n        Add JSON file\\n      \"],[8],[0,\"\\n\"],[0,\"      \"],[6,\"section\"],[9,\"class\",\"custom-text\"],[7],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"text\"],[9,\"name\",\"custom-text\"],[9,\"id\",\"custom-text\"],[9,\"placeholder\",\"The text entered here will appear on badges\"],[7],[8],[0,\"\\n      \"],[8],[0,\"\\n      \"],[6,\"section\"],[9,\"class\",\"config-json\"],[7],[0,\"\\n        \"],[6,\"p\"],[7],[0,\"Upload a config file.\"],[8],[0,\"\\n        \"],[6,\"input\"],[9,\"type\",\"file\"],[9,\"name\",\"config-json-file\"],[9,\"id\",\"config-json-file\"],[7],[8],[0,\"\\n      \"],[8],[0,\"\\n    \"],[8],[0,\"\\n\\n    \"],[6,\"div\"],[9,\"class\",\"button\"],[7],[0,\"\\n      \"],[6,\"input\"],[9,\"type\",\"submit\"],[9,\"value\",\"Generate\"],[9,\"id\",\"submit\"],[7],[8],[0,\"\\n    \"],[8],[0,\"\\n  \"],[8],[0,\"\\n\"],[8]],\"hasEval\":false}", "meta": { "moduleName": "badgeyay-frontend/templates/components/badge-front.hbs" } });
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
  require("badgeyay-frontend/app")["default"].create({"name":"badgeyay-frontend","version":"0.0.0+ca5e7855"});
}
//# sourceMappingURL=badgeyay-frontend.map
