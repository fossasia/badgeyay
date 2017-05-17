eventyay-badge-generator
========================

This script generates the badges for an exported list of speakers of the eventyey platform.

[![Build Status](https://travis-ci.org/niccokunzmann/fossasia-badge-generator.svg?branch=master)][travis]

Conversion
----------

The input form eventyay is a json list of speakers.
It must be in the speakers.json file.

```
[
    {
        "id": 2503, 
        "name": "Nicco Kunzmann", 
        "email": "niccokunzmann@asdfg.com", 
        "mobile": "", 
        "photo": "https://storage.googleapis.com/eventyay.com/events/69/speakers/2503/photo/TmpqTmxjVX/bd9e6b8b-31c2-4af2-9977-2e8443510f12.png", 
        "organisation": "Coderdojo", 
        "position": "", 
        "country": "", 
        "short_biography": "<p>CoderDojo ist ein Programmierklub für Mädchen und Jungen im Alter von 5-17 Jahren. Hier könnt ihr euch kreativ mit Technik auseinandersetzen und Programmieren lernen.</p><p>Alle Materielien findet ihr unter <a href=\"http://coderdojopotsdam.github.io\" rel=\"nofollow\" target=\"_blank\">coderdojopotsdam.github.io</a>, nachdem ihr auch \"View More\" oder \"mehr anzeigen\" klickt.</p>", 
        "long_biography": "", 
        "website": "", 
        "twitter": "", 
        "facebook": "", 
        "github": "", 
        "linkedin": "", 
        "city": "", 
        "featured": false, 
        "gender": "", 
        "heard_from": "", 
        "icon": "https://storage.googleapis.com/eventyay.com/events/69/speakers/2503/icon/T3BCMXdRWU/8cc480fb-b3ae-46c5-8b6c-4fe07b4c7223.jpg", 
        "sessions": [
            {
                "id": 3699, 
                "title": "Python Workshop"
            }, 
            {
                "id": 3296, 
                "title": "Coderdojo"
            }
        ], 
        "small": "https://storage.googleapis.com/eventyay.com/events/69/speakers/2503/small/dVdxZU1nY0/fbd66dcf-51ba-45c2-a5e0-54ae33526744.jpg", 
        "speaking_experience": "", 
        "sponsorship_required": "", 
        "thumbnail": "https://storage.googleapis.com/eventyay.com/events/69/speakers/2503/thumbnail/MlR1dVI3bW/bacafb8c-beab-4ede-ba5c-0d20740a8e56.jpg"
    }
]
```

To generate the `speaker.png.csv` file and the all-badges.png file, execute

```
./generate-speaker-csv.py && ./merge_badges.sh
```

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

Maintainers
-------------------

The project is maintained by
 - Nicco Kunzmann ([@niccokunzmann](https://github.com/niccokunzmann))
 - Tarun Kumar ([@meets2tarun](https://github.com/meets2tarun))
