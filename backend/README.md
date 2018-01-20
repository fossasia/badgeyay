# BadgeYAY Backend

[![Travis branch](https://img.shields.io/travis/fossasia/badgeyay/development.svg?style=flat-square)](https://travis-ci.org/fossasia/badgeyay)
[![Codecov branch](https://img.shields.io/codecov/c/github/fossasia/badgeyay/development.svg?style=flat-square&label=Codecov+Coverage)](https://codecov.io/gh/fossasia/badgeyay)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-ff006f.svg?style=flat-square)][gitter]

`badgeyay` is a simple badge generator with a simple web UI to add data and generate printable badges in a pdf.

The user can:
  * Choose size of badges
  * Choose background of badges and upload logo and background image
  * Upload a CSV file or manually enter CSV data as: name, type of attendee, nick/handle, organization/project

# Deploy
One-click Docker, Heroku, Scalingo and Bluemix deployment is also available:

[![Deploy to Docker Cloud](https://files.cloud.docker.com/images/deploy-to-dockercloud.svg)](https://cloud.docker.com/stack/deploy/?repo=https://github.com/fossasia/badgeyay) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/fossasia/badgeyay/tree/development) [![Deploy on Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy?source=https://github.com/fossasia/badgeyay#development) [![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/fossasia/badgeyay&branch=development)
<!-- Replace with backend specific demo
Checkout badgeyay backend in action:

 ![Demo GIF](app/working.gif)

[![Demo YouTube](https://user-images.githubusercontent.com/8705386/30831526-438f8c4c-a237-11e7-83fc-c12046f12e18.png)](https://www.youtube.com/watch?v=Gh8j_01LIoQ)-->

Our current goal is to provide an interface to generate badges for the FOSSASIA conference.

If you like to join developing,

- you can [chat on gitter][gitter], mentioning the maintainers.
- you can find/create [issues](https://github.com/fossasia/badgeyay/issues) and solve them.
  - When you solve an issue, you do not own it. Share your progress via a Pull-Requst as soon as possible.
  - Discuss with others who work on the issue about the best solution. It is your responsibility, not the maintainer's to choose the best solution.
- If in doubt, let's follow [CCCC][cccc].

Data model
----------

### Request

/api/v1.0/generate_badges
- Method: POST
- Parameters:
   - custfont: Font to use. if it is null or not present the default font will be used.
   - file: .csv which contains user data
   - csv: CSV data as plain text seperated by a comma (,)
   
   (Either file or csv must be present in the query if both are present, file will be processed)
   - img-default: The dafault image to use. (Required)
   - bg_color: Hex code of background colour of the badge. Will only be parsed if the value of img-default is "user_defined.png"
   - image: The custom background image (in .png format) of the badge which will be uploaded
   
   (Either img-default or image must be present in the query if both are present, image will be processed)

### Response

```json
[{
"type" : "success",
"message" : "pdf generation completed successfully",
"download_link" : "https://badgeyay-dev.herokuapp.com/static/badges/team-png-csv-badges.pdf"
}]
```

Specification
-------------

### Technologies Used

Badgeyay backend uses a number of open source projects:

* [Flask](http://flask.pocoo.org/) - Microframework powered by python
* [Bootstrap](https://getbootstrap.com/docs/3.3/) - Responsive frontend framework
* [Shell](https://en.wikipedia.org/wiki/Unix_shell) - Script used for merging badges of different types
* [Heroku](https://www.heroku.com/) - Webapp deployed here
* [Travis](travis-ci.org) - Continuous Integration of the project
* [Github Release](https://help.github.com/articles/creating-releases/) - Releases are GitHub's way of packaging and providing software to the users

### Testing Methodology Used

* [Python Unit tests](https://docs.python.org/3/library/unittest.html) - for assertion, with the help of [Selenium](https://github.com/SeleniumHQ/Selenium) for web browser automation.

The guidelines for setting up and running the tests are mentioned in the [testing docs](docs/test/testing.md).



### Customization

You can change the font style, font size, color etc from the `.svg` file in the folder badges.
Inkscape is generally used for editing of such files.

### Usage

You need Ubuntu to run the application. We are working on integrating vagrant to make it easier to run on windows. Check out the [User Input Guide](https://badgeyay-dev.herokuapp.com/guide) for more details.

### Install Dependencies

Badgeyay backend requires the following dependencies to be installed
- python3

For Ubuntu/Debian based Package Managers
```
sudo apt-get update
sudo apt-get install python3
```

For Fedora/CentOS/RPM based package managers
```
sudo -i
yum install python3
exit
```

For Arch based package managers:
```
sudo pacman -S python-cairosvg
sudo pacman -S python-lxml
```

Installation
--------------
Badgeyay backend can be easily deployed on a variety of platforms. Currently it can be deployed in following ways.

1. [Local Installation using Virtual environment](/docs/installation/localvir.md)

2. [Local Installation using Vagrant environment](/docs/installation/localvag.md)

3. [Deployment on Heroku](/docs/installation/heroku.md)

4. [Deployment with Docker](/docs/installation/docker.md)


Contributions, Bug Reports, Feature Requests
--------------
This is an Open Source project and we would be happy to see contributors who report bugs and file feature requests by submitting pull requests as well. Please report issues in the [GitHub tracker](https://github.com/fossasia/badgeyay/issues/new).

## Issue and Branch Policy

Before making a pull request, please file an issue. So, other developers have the chance to give feedback or discuss details. Match every pull request with an issue please and add the issue number in description e.g. like "Fixes #123".

We have the following branches   
 * **development**   
   All development goes on in this branch. If you're making a contribution,
   you are supposed to make a pull request to _development_.
   PRs to master must pass a build check and a unit-test check on Travis.
 * **master**   
   This contains shipped code. After significant features/bugfixes are accumulated on development, we make a version update, and make a release.


Also read [CONTRIBUTING.md](https://github.com/fossasia/badgeyay/blob/development/.github/CONTRIBUTING.md)


Implementation
--------------

[generate_badges.py](/app/generate-badges.py) creates svg files from the `csv`, `png` and
[badges/8BadgesOnA3.svg](badges/8BadgesOnA3.svg).

[merge_badges.py](/app/merge_badges.py) converts them into pdf files and merges
them together into one.

[Travis](https://github.com/fossasia/badgeyay/blob/development/.travis.yml) creates new releases with the `all-badges.pdf` file.

License
-------------------

Badgeyay - A simple badge generator. Its main purpose is to generate badges for events/conferences under the Open Event project of FOSSASIA. The Open Event project aims to make server and client software required for hosting events/conferences easy to build and configure. Copyright (C) 2016, FOSSASIA. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.


Maintainers
-------------------

You can reach the maintainers and ping them personally by looking at the [Badgeyay team][team].

You can become a maintainer by following the project and contributing code to it.
Please see your role in the [CCCC][cccc].

The project is maintained by the [Badgeyay maintainer's team][team].
To join the team:
1. Contribute
2. You or someone else proposes you in an issue to become a member of the team.
3. A Badgeyay admin adds you.

To stay a maintainer in the team:
1. Follow the rules of [CCCC][cccc] or [Badgeyay](.github/CONTRIBUTING.md) and do not violate them willingly or in a harmful way.

To be removed from the team:
1. Someone creates an issue to ask for removal, e.g. because of inactivity or a violation.
2. An admin removes you.


[gitter]: https://gitter.im/fossasia/badgeyay
[cccc]: https://rfc.zeromq.org/spec:42/C4
[team]: https://github.com/orgs/fossasia/teams/badgeyay-admin/members


