# Deploying on Heroku :

## Prerequisites

You will need the following things properly installed on your computer.

Git
Node.js (with NPM)
Ember CLI
PhantomJS
Running Locally

## Deploying to Heroku

````
$ heroku create --buildpack https://codon-buildpacks.s3.amazonaws.com/buildpacks/heroku/emberjs.tgz
$ git push heroku master
$ heroku open
````



## Further Reading / Useful Links

* [Heroku Ember.js Buildpack](https://github.com/heroku/heroku-buildpack-emberjs)
* [ember.js](https://emberjs.com/)
* [ember-cli](https://ember-cli.com/)
* Development Browser Extensions
  * [ember inspector for chrome](https://chrome.google.com/webstore/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi)
  * [ember inspector for firefox](https://addons.mozilla.org/en-US/firefox/addon/ember-inspector/)