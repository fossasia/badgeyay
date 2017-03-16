fossasia-badge-generator
========================

This script generates the badges for the FOSSASIA conference.

[Download Current Badges](https://niccokunzmann.github.io/download_latest/all-badges.pdf)
[![Build Status](https://travis-ci.org/niccokunzmann/fossasia-badge-generator.svg?branch=master)][travis]

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

Related Repositories
--------------------

- https://github.com/fossasia/fossasia-artwork/tree/master/Badges/Badges-2017

[travis]: https://travis-ci.org/niccokunzmann/fossasia-badge-generator
[releases]: https://github.com/niccokunzmann/fossasia-badge-generator/releases
[new-issue]: https://github.com/niccokunzmann/fossasia-badge-generator/issues/new
