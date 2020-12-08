# Deploying on Kubernetes

## For deploying on Kubernetes, you need following things properly installed on your local machine:

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