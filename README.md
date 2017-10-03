# badgeyay

[![Travis branch](https://img.shields.io/travis/fossasia/badgeyay/development.svg?style=flat-square)](https://travis-ci.org/fossasia/badgeyay)
[![Codecov branch](https://img.shields.io/codecov/c/github/fossasia/badgeyay/development.svg?style=flat-square&label=Codecov+Coverage)](https://codecov.io/gh/fossasia/badgeyay)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-ff006f.svg?style=flat-square)][gitter]

The goal of badgeyay is to provide a simple badge generator with the following features:
* a simple web UI to add data and generate printable badges in a zip
* Fields should include:
   * choose size of badges
   * choose background of badges and upload logo and background image
   * upload CSV or copy/paste text for badges including name, type of attendee, nick/handle, organization/project
   
   
To get a better idea about the working of badgeyay ,you can check out the following:
![Alt text](app/working.gif)
[![Alt Watch](https://user-images.githubusercontent.com/8705386/30831526-438f8c4c-a237-11e7-83fc-c12046f12e18.png)](https://www.youtube.com/watch?v=Gh8j_01LIoQ)

This first step is to provide a simple script to generate the badges for the FOSSASIA conference. The next step is to provide a web UI.

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

### Input

- The input is a set of csv files in the same folder, UTF-8.
- The csv file is named after the badge type to take. 
  Example: `vip.png.csv` uses the picture `vip.png`.
- The CSV has up to 4 columns for the name and the twitter handle.
  They will be filled if this number is filled:
  - `__X_`
  - `__XX`
  - `_XXX`
  - `XXXX`

### Output

The output file is svg / pdf / multipage pdf of size A3.
Each badge has the size A6.
The outputs are in a folder derived form the input csv.
The outputs can be either of the two types, viz ZIPs or PDFs, or both. User has the choice to choose from either of
the two or from both of them.

### Customization

You can change the font style, font size, color etc from the `.svg` file in the folder badges.
Inkscape is generally used for editing of such files.

### Usage

You need Ubuntu.

You can run the `merge_badges.py` file.
It generates badges for every csv file and combines them to one.
There is a travis build which build the badges automatically.
When a PR is merged into the master branch, the current badges can be downloaded.

### Install Dependencies

Badgeyay requires the following dependencies to be installed
- python3
- rsvg-convert
- pdftk

For Ubuntu/Debian based Package Managers
```
sudo apt-get update
sudo apt-get python3 librsvg2-bin pdftk
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
5. Install the requirements. ```pip install -r requirements.txt```
6. Go to badgeyay/app directory. ```cd badgeyay/app```
7. Run ```python main.py``` to start server.
* Remember: ```main.py``` should only be executed from app directory.

Contributions, Bug Reports, Feature Requests
--------------
This is an Open Source project and we would be happy to see contributors who report bugs and file feature requests submitting pull requests as well. Please report issues in the [GitHub tracker](https://github.com/fossasia/badgeyay/issues/new).

Also read [CONTRIBUTING.md](https://github.com/fossasia/badgeyay/blob/development/.github/CONTRIBUTING.md)

Installation
--------------
Badgeyay can be easily deployed on a variety of platforms. Currently it can be deployed in following ways.

1. [Local Installation](/docs/installation/local.md)

2. [Deployment on Heroku](/docs/installation/heroku.md)

3. [Deployment with Docker](/docs/installation/docker.md)

One-click Docker and Heroku deployment is also available:

[![Deploy to Docker Cloud](https://files.cloud.docker.com/images/deploy-to-dockercloud.svg)](https://cloud.docker.com/stack/deploy/?repo=https://github.com/fossasia/badgeyay) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


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

You can reach the maintainers,
ping them personally by looking at the [Badgeyay team][team].

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
1. Someone creates an issue to ask for removal, e.g. because if inactivity or a violation.
2. An admin removes you.


[gitter]: https://gitter.im/fossasia/badgeyay
[cccc]: https://rfc.zeromq.org/spec:42/C4
[team]: https://github.com/orgs/fossasia/teams/badgeyay-admin/members
