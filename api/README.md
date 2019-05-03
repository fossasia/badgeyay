# Badgeyay Backend

> **Badgeyay provide an interface to event organizers for generating badges of events from concerts to conferences and meet-ups.**

Badgeyay is an awesome Badge generator with a simple web UI to add data and generate printable badges in a PDF.

## Prerequisites

Badgeyay backend requires the following dependencies to be installed.
   - python3

        * For Ubuntu/Debian based package managers
          ```bash
          sudo apt-get update
          sudo apt-get install python3
          ```

        * For Fedora/CentOS/RPM based package managers
          ```bash
          sudo -i
          yum install python3
          exit
          ```

        * For Arch based package managers:
          ```bash
          sudo pacman -S python-cairosvg
          sudo pacman -S python-lxml
          ```

## Installation

Badgeyay backend can be easily deployed on a variety of platforms. Currently it can be deployed in following ways.

1. [Local Installation using Virtual environment](docs/installation/localvir.md)

2. [Local Installation using Vagrant environment](docs/installation/localvag.md)

3. [Deployment on Heroku](docs/installation/heroku.md)

4. [Deployment with Docker](docs/installation/docker.md)

5. [Deployment on AWS EC2](docs/installation/aws.md)

One-click Docker, Heroku, Scalingo and Bluemix deployment is also available:

[![Deploy to Docker Cloud](https://files.cloud.docker.com/images/deploy-to-dockercloud.svg)](https://cloud.docker.com/stack/deploy/?repo=https://github.com/fossasia/badgeyay) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/fossasia/badgeyay/tree/development)
[![Deploy on Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy?source=https://github.com/fossasia/badgeyay#development)
[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/fossasia/badgeyay&branch=development)


## Testing Methodology Used

* [Python Unit tests](https://docs.python.org/3/library/unittest.html).

## Working

### Input

- The input can be a set of csv files(UTF-8) or a manual entry.
- Detailed Information on the Correct format of Input can be found at [Badgeyay User-Input Guide](http://badgeyay.com/#/guide).

### Output

- The output file is a pdf of size A3.
- Each badge has the size A6.
- The outputs are in a folder derived from the input csv.

### Customization

- You can change the font style, font size, color etc from the `.svg` file in the folder badges.
- Inkscape is generally used for editing of such files.
