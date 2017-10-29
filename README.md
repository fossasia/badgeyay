# badgeyay

[![Travis branch](https://img.shields.io/travis/fossasia/badgeyay/development.svg?style=flat-square)](https://travis-ci.org/fossasia/badgeyay)
[![Codecov branch](https://img.shields.io/codecov/c/github/fossasia/badgeyay/development.svg?style=flat-square&label=Codecov+Coverage)](https://codecov.io/gh/fossasia/badgeyay)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-ff006f.svg?style=flat-square)][gitter]

`badgeyay` is a simple badge generator with a simple web UI to add data and generate printable badges in a zip.

The user should be able to:
  * Choose size of badges
  * Choose background of badges and upload logo and background image
  * Upload a CSV file or manually enter CSV data as: name, type of attendee, nick/handle, organization/project

Checkout badgeyay in action:

![Demo GIF](app/working.gif)

[![Demo YouTube](https://user-images.githubusercontent.com/8705386/30831526-438f8c4c-a237-11e7-83fc-c12046f12e18.png)](https://www.youtube.com/watch?v=Gh8j_01LIoQ)

Our current goal is to provide an interface to generate badges for the FOSSASIA conference.

If you like to join developing,

- you can [chat on gitter][gitter], mentioning the maintainers.
- you can find/create [issues](https://github.com/fossasia/badgeyay/issues) and solve them.
  - When you solve an issue, you do not own it. Share your progress via a Pull-Requst as soon as possible.
  - Discuss with others who work on the issue about the best solution. It is your responsibility, not the maintainer's to choose the best solution.
- If in doubt, let's follow [CCCC][cccc].

Specification
-------------

### Technologies Used

Badgeyay uses a number of open source projects:

* [Flask](http://flask.pocoo.org/) - Microframework powered by python
* [Bootstrap](https://getbootstrap.com/docs/3.3/) - Responsive frontend framework
* [Shell](https://en.wikipedia.org/wiki/Unix_shell) - Script used for merging badges of different types
* [Heroku](https://www.heroku.com/) - Webapp deployed here
* [Travis](travis-ci.org) - Continuous Integration of the project
* [Github Release](https://help.github.com/articles/creating-releases/) - Releases are GitHub's way of packaging and providing software to the users

### Testing Methodology Used

* [Python Unit tests](https://docs.python.org/3/library/unittest.html) - for assertion, with the help of [Selenium](https://github.com/SeleniumHQ/Selenium) for web browser automation.

The guidelines for setting up and running the tests are mentioned in the [testing docs](docs/test/testing.md).

### Input

- The input is a set of csv files in the same folder, UTF-8.
- The csv file is named after the badge type to take. Example: `vip.png.csv` uses the picture `vip.png`.
- The CSV has up to 4 columns for the name and the twitter handle. They will be filled if this number is filled:
  - `__X_`
  - `__XX`
  - `_XXX`
  - `XXXX`
- Optional configuration file in json format to customise badges.
- A sample configuration file is shown below
  ```
  {
    "options": {
        "badge_wrap": true,
        "paper_size_format": "A3"
    }
  }
  ```

  - badge_wrap: It can be **true** or **false**. If set to true then for each entry in the csv file two badges
                will be generated so that they can be wrapped around the badge card.
  - paper_size_format: As of now it's value can be either **"A3"** or **"A4"**. The value will decide the size
                       of the page on which the badges (in groups of 8) will be printed. Not required if width
                       and height of parameters are explicitly mentioned.
  - width: Width of the page on which badges (in groups of 8) will be printed. Value should be in mm.
           For example: **"297mm"**
  - height: Height of the page on which badges (in groups of 8) will be printed. Value should be in mm.
            For example: **"420mm"**.

### Output

The output file is svg / pdf / multipage pdf of size A3.
Each badge has the size A6.
The outputs are in a folder derived from the input csv.
The outputs can be either of the two types, viz ZIPs or PDFs, or both. User has the choice to choose from either of the two or from both of them.

### Customization

You can change the font style, font size, color etc from the `.svg` file in the folder badges.
Inkscape is generally used for editing of such files.

### Usage

You need Ubuntu to run the application. We are working on integrating vagrant to make it easier to run on windows. Check out the [User Input Guide](https://badgeyay-dev.herokuapp.com/guide) for more details.

### Install Dependencies

Badgeyay requires the following dependencies to be installed
- python3
- rsvg-convert
- pdftk

For Ubuntu/Debian based Package Managers
```
sudo apt-get update
sudo apt-get install python3 librsvg2-bin pdftk
```

For Fedora/CentOS/RPM based package managers
```
sudo -i
dnf install librsvg2 librsvg2-tools
dnf install gcc gcc-c++ libXrandr gtk2 libXtst libart_lgpl
wget http://mirror.centos.org/centos/6/os/x86_64/Packages/libgcj-4.4.7-18.el6.x86_64.rpm
wget https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/pdftk-2.02-1.el6.x86_64.rpm
rpm -ivh --nodeps libgcj-4.4.7-11.el6.x86_64.rpm
rpm -i pdftk-2.02-1.el6.x86_64.rpm
exit
```

### Running locally
1. [Fork the main repo](https://github.com/fossasia/badgeyay/fork).
2. Clone your local repo. ```git clone https://github.com/<your_username>/badgeyay.git```
3. Create a virtual environment. ```virtualenv -p python3 venv```
4. Activate the virtual environment. ```source activate venv```
5. Go to badgeyay directory. ```cd badgeyay```
6. Install the requirements. ```pip install -r requirements.txt```
7. Run ```python app/main.py``` to start server.
* Remember: ```python app/main.py``` should only be executed from root directory.


### Vagrant Installation Instructions
1. Install Vagrant from [Vagrant Download Page](https://www.vagrantup.com/downloads.html)
2. Install Virtualbox from [Vitualbox Download Page](https://www.virtualbox.org/wiki/Downloads)
3. Clone the project from `git clone https://github.com/<your_username>/badgeyay.git`
4. Enter the directory using `cd badgeyay`
5. In Terminal in the "badgeyay" directory, type `vagrant up` to bring up the virtual machine. This will start installation of a ubuntu box within which the server will run with all its components. If after typing "vagrant up" you received an error stating “valid providers not found ...", type `vagrant up --provider=virtualbox`
6. After the installation is completed `ssh` into vagrant environment using `vagrant ssh`. This will bring you to the root directory of the Virtual Machine
7. Move to your project using `cd /vagrant`
8. To Run the flask server you need to be in the "app" directory. Do `cd app`
9. Run flask server in port `0.0.0.0`
   ```
   export FLASK_APP=main.py
   python -m flask run --host=0.0.0.0
   ```
10. Now your server is up and running. To view the badgeyay page go to localhost:8001

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

Installation
--------------
Badgeyay can be easily deployed on a variety of platforms. Currently it can be deployed in following ways.

1. [Local Installation](/docs/installation/local.md)

2. [Deployment on Heroku](/docs/installation/heroku.md)

3. [Deployment with Docker](/docs/installation/docker.md)

One-click Docker, Heroku, Scalingo and Bluemix deployment is also available:

[![Deploy to Docker Cloud](https://files.cloud.docker.com/images/deploy-to-dockercloud.svg)](https://cloud.docker.com/stack/deploy/?repo=https://github.com/fossasia/badgeyay) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/fossasia/badgeyay/tree/development) [![Deploy on Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy?source=https://github.com/fossasia/badgeyay#development) [![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/fossasia/badgeyay&branch=development)


Implementation
--------------

[generate_badges.py](/app/generate_badges.py) creates svg files from the `csv`, `png` and
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
