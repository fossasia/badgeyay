
# Badgeyay
![Badgeyay](/frontend/public/images/Badgeyay-artwork.png)

[![Gitter](https://img.shields.io/badge/chat-on%20gitter-ff006f.svg?style=flat-square)](https://gitter.im/fossasia/badgeyay)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1ac554483fac462797ffa5a8b9adf2fa?style=flat-square)](https://www.codacy.com/app/fossasia/badgeyay)
[![Travis branch](https://api.travis-ci.org/fossasia/badgeyay.svg?branch=development&style=flat-square)](https://travis-ci.org/fossasia/badgeyay)
[![Codecov branch](https://codecov.io/gh/fossasia/badgeyay/branch/development/graph/badge.svg?style=flat-square)](https://codecov.io/gh/fossasia/badgeyay)

> **Badgeyay provide an interface to event organizers for generating badges of events from concerts to conferences and meet-ups.**

Badgeyay is a Badge generator with a simple web UI to add data and generate printable badges in a PDF.

The user can:
  * Choose size of badges
  * Choose background of badges and upload logo and background image
  * Upload a CSV file or manually enter CSV data as: name, type of attendee, designation, nick/handle, organization/project

## Communication

* Please join our **[mailing list](https://groups.google.com/forum/#!forum/open-event)** to discuss questions regarding the project.
> https://groups.google.com/forum/#!forum/open-event

* Our chat channel is on **[Gitter](https://gitter.im/fossasia/badgeyay)**
> [gitter.im/fossasia/badgeyay](https://gitter.im/fossasia/badgeyay)

## Installation

Badgeyay frontend and backend can be deployed easily and detailed installation instruction of frontend and backend have been provided below.

1. [Badgeyay Frontend](/frontend/README.md)
1. [Badgeyay Backend](/api/README.md)
* **Installing git pre-push hook:**
    * Run file `scripts/install-hook.py`. It will copy contents of `scripts/pre-push-hook.py` to `.git/hooks/pre-push`. Make sure that you have `.git/hooks/pre-push.sample` in your `.git` directory before performing this step.
    * This will install git `pre-push-hook` in your local `.git` directory. It will run the commits against linting tests before pushing to a remote. See `scripts/pre-push-hook.py` if you encounter any errors.


## Technology Stack

Please get familiar with the different components of the project in order to be able to contribute.

* Backend Web Framework - [Flask](http://flask.pocoo.org/)
* Frontend Web Framework - [Ember.js](https://emberjs.com/)

## Branch Policy

We have the following branches :
 * **development**
	 All development goes on in this branch. If you're making a contribution, please make a pull request to _development_.
	 PRs to must pass a build check and all tests check on Travis.

 * **master**
   This contains shipped code. After significant features/bug-fixes are accumulated on development, we make a version update, and make a release.

## Contributions Best Practices

**Commits**
* Write clear meaningful git commit messages (Do read http://chris.beams.io/posts/git-commit/)
* Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (More info at https://github.com/blog/1506-closing-issues-via-pull-requests )
* When you make very very minor changes to a PR of yours (like for example fixing a failing travis build or some small style corrections or minor changes requested by reviewers) make sure you squash your commits afterwards so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at https://davidwalsh.name/squash-commits-git )
* When you're submitting a PR for a UI-related issue, it would be really awesome if you add a screenshot of your change or a link to a deployment where it can be tested out along with your PR. It makes it very easy for the reviewers and you'll also get reviews quicker.

**Feature Requests and Bug Reports**
* When you file a feature request or when you are submitting a bug report to the [Issue tracker](https://github.com/fossasia/badgeyay/issues), make sure you add steps to reproduce it. Especially if that bug is some weird/rare one.

**Join the development**
* Before you join development, please set up the system on your local machine and go through the application completely. Press on any link/button you can find and see where it leads to. Explore. (Don't worry ... Nothing will happen to the app or to you due to the exploring :wink: Only thing that will happen is, you'll be more familiar with what is where and might even get some cool ideas on how to improve various aspects of the app.)
* If you would like to work on an issue, drop in a comment at the issue. If it is already assigned to someone, but there is no sign of any work being done, please free to drop in a comment so that the issue can be assigned to you if the previous assignee has dropped it entirely.

## License

This project is currently licensed under the **[GNU General Public License v3](/LICENSE)**.

> To obtain the software under a different license, please contact [FOSSASIA](http://blog.fossasia.org/contact/).
