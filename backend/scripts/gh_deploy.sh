#!/bin/bash

git config --global user.name "Travis CI"
git config --global user.email "noreply+travis@fossasia.org"

if [ "$TRAVIS_PULL_REQUEST" != "false" -o "$TRAVIS_REPO_SLUG" != "fossasia/badgeyay" -o "$TRAVIS_BRANCH" != "$DEPLOY_BRANCH" ]; then
    echo "Skipping deploy; The request or commit is not on development:)"
    exit 0
fi

DEPLOY_PATH=/badgeyay/backend/
HEROKU_NAME="badgeyay-api"

rm -rf $DEPLOY_PATH
mkdir -p $DEPLOY_PATH

cd $DEPLOY_PATH
git init
heroku git:remote -a $HEROKU_NAME
git add -A .
git commit -m "deploy"
git push -f heroku master

cd -
rm -rf $DEPLOY_PATH

echo "🚀  https://$HEROKU_NAME"
