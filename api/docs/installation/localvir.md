# Local Development Setup

The instructions on this page will guide you in setting up a local development
environment in your system. First things first, BadgeYay needs 'Python 3' to run.
Most of the distros come bundled with that but if it is not there please install it first.

These are some additional depencies that you will need:

```sh
$ sudo apt-get update
```

Make sure you have the dependencies mentioned above installed before proceeding further.
For a start, fork BadgeYay to your own github account. Then, clone it to your local system.

* **Step 1**
```sh
$ git clone -b development https://github.com//badgeyay.git
```

Add an upstream remote so that you can push your patched branches for starting a PR .

```sh
$ cd badgeyay
$ git remote add upstream https://github.com/fossasia/badgeyay.git
```

* **Step 2**

```sh
$ sudo apt-get install python3-venv
$ python3 -m venv badgeyay
$ source badgeyay/bin/activate
```

OR

* It is recommended that you use ['virtualenv'](https://virtualenv.pypa.io/en/stable/installation/)
and ['virtualenvwrapper'](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) to maintain a clean Python 3 environment. Create a 'virtualenv':

```sh
$ source 'which virtualenvwrapper.sh'
$ mkvirtualenv -p python3 badgeyay
(badgeyay) $ deactivate # To deactivate the virtual environment
$ workon badgeyay # To activate it again
```

> **source 'which virtualenvwrapper.sh'** is used to prevent from breaking the 'mkvirtualenv' command, you can find more about the issue, [here](https://stackoverflow.com/questions/13855463/bash-mkvirtualenv-command-not-found).

* Now, since you are inside a virtual environment, you can setup 'badgeyay' as an editable package.
* Install all the requirements.

```sh
(badgeyay)$ pip install -r requirements.txt
```

* **Step 3** Changing the Configs for development

```sh
Go to Config file:
```
[Config](/api/config/config.py)

```sh
Now Change the 'ENV' variable to 'LOCAL'
```

* **Step 4** Now creating database and user

# For linux users
```sh
sudo -u postgres psql
```
# For macOS users
```sh
psql -d postgres
```
* When inside psql, create a user 'postgres' for badgeyay and then using the user create the database.

```sh
CREATE USER postgres WITH PASSWORD 'postgres';
```
* If user already exists,then setting password for user 'postgres's
```sh
ALTER USER postgres PASSWORD 'postgres';
```

* Creating the database

```sh
CREATE DATABASE badgeyay WITH OWNER postgres;
```
* Once database is created, exit the psql shell with \q followed by ENTER.

* **Step 5** - Start the postgres service.

```sh
sudo service postgresql restart
```

* **Step 6**
* To run the project on a local machine (default mode).

```sh
(badgeyay) $ export FLASK_APP=run.py
(badgeyay)$ flask run

```

* To run the project on a local machine (debug mode).

```sh
(badgeyay) $ export FLASK_DEBUG=1
(badgeyay)$ flask run
```

## Preferred Development Workflow

1. Activate the virtual environment.

```sh
$ workon badgeyay # To activate it again
(badgeyay) $
```

2. Get the latest copy of code from upstream.

```sh
(badgeyay) $ git pull upstream development
```

3. Once you get assigned an issue, create a new branch from 'development'.

```sh
(badgeyay) $ git checkout -b XXX-mock-issue # XXX is the issue number
```

4. Work on your patch, test it and when it's done, push it to your fork.

```sh
(badgeyay) $ git push origin XXX-mock-issue
```
5. File a PR and wait for the maintainers to suggest reviews or in the best case
merge the PR. Then just update 'development' of your local clone.

```sh
(badgeyay) $ git pull upstream master
```

And then loop back again. For contribution guidelines, refer [here](https://github.com/fossasia/badgeyay/blob/development/.github/CONTRIBUTING.md)