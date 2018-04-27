# Badgeyay Frontend

> **Badgeyay provide an interface to event organizers for generating badges of events from concerts to conferences and meet-ups.**

Badgeyay is a Badge generator with a simple web UI to add data and generate printable badges in a PDF.

This directory contains the frontend for badgeyay.

> Note to mobile users: On google chrome of mobile device, you need to **disable data saver** option in settings to open the [website](http://badgeyay.com/). Try clearing cache and cookies if the problem still persists.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [Node.js](https://nodejs.org/) (with npm)
* [Ember CLI](https://ember-cli.com/)
* [Google Chrome](https://google.com/chrome/) (for testing purposes only)

## Installation

To install the app, run the following commands in a command line:

* `git clone https://github.com/fossasia/badgeyay`
* `cd badgeyay/frontend`
* `npm install`

## Running locally:

To run the app locally on your machine, run the following commands in a command line:

* `ember serve`
* Visit your app at [http://localhost:4200](http://localhost:4200).
* Visit your tests at [http://localhost:4200/tests](http://localhost:4200/tests).

### Running Tests

* `ember test`
* `ember test --server`

### Building

* `ember build` (development)
* `ember build --environment production` (production)

### Deploying on Kubernetes

For deploying on Kubernetes, you need following things properly installed on your local machine:

* [Docker](https://docs.docker.com/install/)
* [Docker Machine](https://docs.docker.com/machine/install-machine/)
* [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts)
* [VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads)

  #### Enabling Google Kubernetes Engine API:
  *  Visit the [Kubernetes Engine page](https://console.cloud.google.com/projectselector/kubernetes?_ga=2.190554988.-672712410.1518259944) in the Google Cloud Platform Console.
  * Create or select a project.
  * Wait for the API and related services to be enabled.

  ##### Creating local VM
  * `docker-machine create --driver virtualbox default`
  * `docker-machine env default`
  * `eval "$(docker-machine env default)"`

  ##### Installing Kubernetes Command line tool:
  * `gcloud components install kubectl`

  ##### Building and deploying the container image:
  * `export PROJECT_ID="$(gcloud config get-value project -q)"`
  * `docker build -t gcr.io/${PROJECT_ID}/badgeyay:v1 .` (Build Container Image)
  * `gcloud docker -- push gcr.io/${PROJECT_ID}/badgeyay:v1` (Push Container Image)
  * `gcloud container clusters create badgeyay-cluster --num-nodes=3` (Create Container cluster)
  * `kubectl run badgeyay-web --image=gcr.io/${PROJECT_ID}/badgeyay:v1 --port 4200` (Deploy your application)
  * `kubectl expose deployment badgeyay-web --type=LoadBalancer --port 80 --target-port 4200` (Expose deployment over the Internet)
  * `kubectl get service`
  * Copy the External-IP from the showed list corresponding to your cluster's name and run it in your browser.


## Further Reading / Useful Links

* [ember.js](https://emberjs.com/)
* [ember-cli](https://ember-cli.com/)
* Development Browser Extensions
  * [ember inspector for chrome](https://chrome.google.com/webstore/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi)
  * [ember inspector for firefox](https://addons.mozilla.org/en-US/firefox/addon/ember-inspector/)
