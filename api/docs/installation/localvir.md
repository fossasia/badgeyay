# Local Development Setup

The instructions on this page will guide you in setting up a local development
environment in your system. First things first, BadgeYay needs 'Python 3' to run.
Most of the distros come bundled with that but if it is not there please install it first.

These are some additional depencies that you will need:

```sh
$ sudo apt-get update
```

## Video Installation


<p><a href="https://www.youtube.com/watch?v=oUakEOavgbo&feature=youtu.be" rel="nofollow"><img src="https://i.ytimg.com/vi/oUakEOavgbo/hqdefault.jpg" alt="Demo YouTube" style="max-width:100%;"></a></p>

## Steps

Make sure you have the dependencies mentioned above installed before proceeding further.

* **Step 0** - For a start, fork BadgeYay to your own github account. Then, clone it to your local system. You will need to ```cd``` into your local badgeyay directory.

* **Step 1**
```sh
$ git clone -b development https://github.com/<your_username>/badgeyay.git
$ cd badgeyay
```

Add an upstream remote so that you can push your patched branches for starting a PR .

```sh
$ cd badgeyay
$ git remote add upstream https://github.com/fossasia/badgeyay.git
```


* **Step 1** - Install the python requirements. You need to be present in the root directory of the project.

* System Wide Installation

```sh
sudo -H pip3 install -r api/requirements.txt
```
hint: You may need to upgrade your pip version and install following packages if you encounter errors while installing the requirements.

* Installation in Virtual Environment

 It is recommended that you use [`virtualenv`](https://virtualenv.pypa.io/en/stable/installation/)
and [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) to maintain a clean Python 3 environment. Create a `virtualenv`:

```sh
$ source `which virtualenvwrapper.sh`
$ mkvirtualenv -p python3 badgeyay
(badgeyay) $ deactivate         # To deactivate the virtual environment
$ workon badgeyay               # To activate it again
```

OR

```sh
$ sudo apt-get install python3-venv
$ python3 -m venv badgeyay
$ source badgeyay/bin/activate
```



> **source 'which virtualenvwrapper.sh'** is used to prevent from breaking the 'mkvirtualenv' command, you can find more about the issue, [here](https://stackoverflow.com/questions/13855463/bash-mkvirtualenv-command-not-found).

* Now, since you are inside a virtual environment, you can setup 'badgeyay' as an editable package.
* Install all the requirements.

```sh
(badgeyay)$ pip install -r api/requirements.txt
```
* **Step 2** - Create the database. For that we first open the psql shell. Go to the directory where your postgres file is stored.

```sh
$ sudo -u postgres psql
```

While inside psql, create a user for badgeyay and then using the user create the database.

For ease of development, you should create Postgres user with the same username as your OS account. For example, if your OS login account is _tom_, then you should create _tom_ user in Postgres. By this, you can skip entering password when using database.

```sql
CREATE USER tom WITH PASSWORD 'start';
CREATE DATABASE badgeyay WITH OWNER tom;
```

Once database is created, exit the psql shell with `\q` followed by ENTER.

If you want a graphical interface for this, you can try [pgAdmin](https://www.pgadmin.org/).

* **Step 3** - Setup the .env file similar to [.env.example file](https://github.com/fossasia/badgeyay/blob/development/.env.example)

According to the name of the user and its password that you have created, you will need to set the credentials in the .env file.

* By default, the user and password is 'postgres'. So if you make the user with the same credentials, there is no need to set these variables.

* **Step 4** - Setup the .env file similar to [.env.example file](https://github.com/fossasia/badgeyay/blob/development/.env.example)

In the .env file, set the `BADGEYAY_ENV` variable to `LOCAL`
```
BADGEYAY_ENV = 'LOCAL'
```
* When inside psql, create a user 'postgres' for badgeyay and then using the user create the database.

* **Step 5** - Start the postgresql service

You need to have postgresql running in the background.

```sh
sudo service postgresql restart
```


* **Step 5** - Start the application

* To run the project on a local machine (default mode).

First run the ember server as given [here](https://github.com/fossasia/badgeyay/blob/development/frontend/README.md).
It is necessary to run both the ember server and as well as the python backend server to get the service up and running.

Then, in a terminal, type

```sh
(badgeyay/api) $ export FLASK_APP=run.py
(badgeyay/api)$ flask run
```

 * To run the project on a local machine (debug mode).
```sh
(badgeyay/api) $ export FLASK_DEBUG=1
(badgeyay/api)$ flask run
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
