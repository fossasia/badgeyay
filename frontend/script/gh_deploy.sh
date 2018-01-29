#!/bin/bash

git config --global user.name "Travis CI"
git config --global user.email "noreply+travis@fossasia.org"


export DEPLOY_BRANCH=${DEPLOY_BRANCH:-development}

if [ "$TRAVIS_PULL_REQUEST" != "false" -o "$TRAVIS_REPO_SLUG" != "fossasia/badgeyay" -o "$TRAVIS_BRANCH" != "$DEPLOY_BRANCH" ]; then
    echo "Skipping deploy; The request or commit is not on development:)"
    exit 0
fi

echo $DEPLOY_DOMAIN >> public/CNAME
ember deploy gh-pages-with-domain
