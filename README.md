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

This first step is to provide a simple script to generate the badges for the FOSSASIA conference. The next step is to provide a web UI.

If you like to join developing,

- you can [chat on gitter][gitter], mentioning the maintainers.
- you can find/create [issues](https://github.com/fossasia/badgeyay/issues) and solve them.
  - When you solve an issue, you do not own it. Share your progress via a Pull-Requst as soon as possible.
  - Discuss with others who work on the issue about the best solution. It is your responsibility, not the maintainer's to choose the best solution.
- If in doubt, let's follow [CCCC](https://rfc.zeromq.org/spec:42/C4).

Specification
-------------

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
The outputs are in a folder derived form the input csv

### Customization

You can change the font style, font size, color,etc from the .svg file in the folder badges.
Inkscape is generally used for editing of such files.

### Usage

You need Ubuntu.

You can run the `merge_badges.sh` file.
It generates badges for every csv file and combines them to one.
There is a travis build which build the badges automatically.
When a PR is merged into the master branch, the current badges canbe downloaded.

Contributions, Bug Reports, Feature Requests
--------------
This is an Open Source project and we would be happy to see contributors who report bugs and file feature requests submitting pull requests as well. Please report issues in the [GitHub tracker][new-issue].

Implementation
--------------

[generate_badges.py](generate_badges.py) creates svg files from the `csv`, `png` and
[badges/8BadgesOnA3.svg](badges/8BadgesOnA3.svg).

[merge_badges.sh](merge_badges.sh) converts there into pdf files and merges
them together into one.

[Travis][travis] creates new [releases][releases] with the `all-badges.pdf` file.

Maintainers
-------------------

The project is maintained by
 - Nicco Kunzmann ([@niccokunzmann](https://github.com/niccokunzmann))
 - Tarun Kumar ([@meets2tarun](https://github.com/meets2tarun))
 
 [gitter]: https://gitter.im/fossasia/open-event-orga-server
