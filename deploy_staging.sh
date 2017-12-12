#!/bin/bash
SOURCE_BRANCH="master"

if [ "$TRAVIS_PULL_REQUEST" != "false" -o "$TRAVIS_BRANCH" != "$SOURCE_BRANCH" ]; then
    echo "Skipping deploy; The request or commit is not on master"
    exit 0
fi

set -e

docker build -t badgeyay:$TRAVIS_COMMIT ./docker
docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker tag badgeyay:$TRAVIS_COMMIT badgeyay:latest
docker push badgeyay
echo $GCLOUD_SERVICE | base64 --decode -i > ${HOME}/gcloud-service-key.json
gcloud auth activate-service-account --key-file ${HOME}/gcloud-service-key.json

gcloud --quiet config set project $PROJECT_NAME_STG
gcloud --quiet config set container/cluster $CLUSTER_NAME_STG
gcloud --quiet config set compute/zone ${CLOUDSDK_COMPUTE_ZONE}
gcloud --quiet container clusters get-credentials $CLUSTER_NAME_STG

kubectl config view
kubectl config current-context

kubectl set image deployment/${KUBE_DEPLOYMENT_NAME} ${KUBE_DEPLOYMENT_CONTAINER_NAME}=badgeyay:$TRAVIS_COMMIT
