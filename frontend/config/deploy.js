/* jshint node: true */

module.exports = function(deployTarget) {
  var ENV = {
    build: {},
    // include other plugin configuration that applies to all deploy targets here
  };


if (deployTarget === 'gh-pages') {
     ENV.build.environment = 'production'; 
     ENV.git = {
       repo: `https://ParthS007:${process.env.GH_TOKEN}@github.com/fossasia/badgeyay`,
       branch: 'gh-pages',
       commitMessage: 'Deployed %@'
     };
   }

  return ENV;
};
