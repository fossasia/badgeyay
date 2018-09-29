# Local Development Setup

The instructions on this page will guide you in setting up a local development
environment in your system. First things first, BadgeYay needs 'Python 3' to run.
Most of the distros come bundled with that but if it is not there please install it first.

These are some additional depencies that you will need:

```sh
$ sudo apt-get update
```

## Steps

Make sure you have the dependencies mentioned above installed before proceeding further.

* **Step 0** - For a start, fork BadgeYay to your own github account. Then, clone it to your local system. You will need to ```cd``` into your local badgeyay directory.

* **Step 1**
```sh
$ git clone -b development https://github.com/<your_username>/badgeyay.git
```
![screenshot from 2018-09-29 13-10-52](https://user-images.githubusercontent.com/17084322/46242938-06e26a80-c3ec-11e8-8619-11414dbe2f12.png)

![screenshot from 2018-09-29 13-11-02](https://user-images.githubusercontent.com/17084322/46242953-1bbefe00-c3ec-11e8-80cd-6238a8b7c933.png)
![screenshot from 2018-09-29 13-12-08](https://user-images.githubusercontent.com/17084322/46242962-28dbed00-c3ec-11e8-868a-5119622df54f.png)
![screenshot from 2018-09-29 13-12-23](https://user-images.githubusercontent.com/17084322/46242966-35f8dc00-c3ec-11e8-8938-c5302c8ddc03.png)

Add an upstream remote so that you can push your patched branches for starting a PR .

```sh
$ cd badgeyay
$ git remote add upstream https://github.com/fossasia/badgeyay.git
```
![screenshot from 2018-09-29 13-12-32](https://user-images.githubusercontent.com/17084322/46242967-3f824400-c3ec-11e8-8288-d9c8d9614ec8.png)


* **Step 1** - Install the python requirements. You need to be present in the root directory of the project.

* System Wide Installation

```sh
sudo -H pip3 install -r api/requirements.txt
```
hint: You may need to upgrade your pip version and install following packages if you encounter errors while installing the requirements.

![screenshot from 2018-09-29 13-12-54](https://user-images.githubusercontent.com/17084322/46242980-62145d00-c3ec-11e8-832b-3c581d3cc3fa.png)

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
![screenshot from 2018-09-29 13-13-33](https://user-images.githubusercontent.com/17084322/46242982-65a7e400-c3ec-11e8-98ce-d858359198b2.png)

![screenshot from 2018-09-29 13-13-43](https://user-images.githubusercontent.com/17084322/46242991-84a67600-c3ec-11e8-8888-ca99c9346e9a.png)
![screenshot from 2018-09-29 13-13-53](https://user-images.githubusercontent.com/17084322/46242993-95ef8280-c3ec-11e8-8690-1a14cf7b0c59.png)



> **source 'which virtualenvwrapper.sh'** is used to prevent from breaking the 'mkvirtualenv' command, you can find more about the issue, [here](https://stackoverflow.com/questions/13855463/bash-mkvirtualenv-command-not-found).

* Now, since you are inside a virtual environment, you can setup 'badgeyay' as an editable package.
* Install all the requirements.

```sh
(badgeyay)$ pip install -r api/requirements.txt
```
![screenshot from 2018-09-29 13-14-08](https://user-images.githubusercontent.com/17084322/46242994-9720af80-c3ec-11e8-93a0-70beb8915a57.png)

* **Step 2** - Create the database. For that we first open the psql shell. Go to the directory where your postgres file is stored.

```sh
$ sudo -u postgres psql
```
![screenshot from 2018-09-29 13-18-45](https://user-images.githubusercontent.com/17084322/46242998-aa337f80-c3ec-11e8-9c53-adc8a16abc9b.png)

While inside psql, create a user for badgeyay and then using the user create the database.

For ease of development, you should create Postgres user with the same username as your OS account. For example, if your OS login account is _tom_, then you should create _tom_ user in Postgres. By this, you can skip entering password when using database.

```sql
CREATE USER tom WITH PASSWORD 'start';
CREATE DATABASE badgeyay WITH OWNER tom;
```

![screenshot from 2018-09-29 13-19-23](https://user-images.githubusercontent.com/17084322/46243000-ab64ac80-c3ec-11e8-834a-27c36988f9a1.png)


Once database is created, exit the psql shell with `\q` followed by ENTER.
![screenshot from 2018-09-29 13-20-14](https://user-images.githubusercontent.com/17084322/46243014-c46d5d80-c3ec-11e8-83f4-4484f2ab3591.png)


If you want a graphical interface for this, you can try [pgAdmin](https://www.pgadmin.org/).

* **Step 3** - Adding the credentials in [Config file](https://github.com/fossasia/badgeyay/blob/development/api/config/config.py)

According to the name of the user and its password that you have created, you will need to change the credentials in the config.py file.

* By default, the user and password is 'postgres'. So if you make the user with the same credentials, there is not need to chagne them in the config file.

* **Step 4** - Change the ENV variable in [Config file](https://github.com/fossasia/badgeyay/blob/development/api/config/config.py)

While in the config file, change the `ENV` variable to `LOCAL`
```
ENV = 'LOCAL'
```

![screenshot from 2018-09-29 13-21-36](https://user-images.githubusercontent.com/17084322/46243033-df3fd200-c3ec-11e8-87fc-990154b73f6b.png)

* When inside psql, create a user 'postgres' for badgeyay and then using the user create the database.

* **Step 5** - Start the postgresql service

You need to have postgresql running in the background.

```sh
sudo service postgresql restart
```

![screenshot from 2018-09-29 13-22-02](https://user-images.githubusercontent.com/17084322/46243037-f7175600-c3ec-11e8-8725-8adaa404b8c1.png)

* **Step 5** - Start the application

* To run the project on a local machine (default mode).

First run the ember server as given [here](https://github.com/fossasia/badgeyay/blob/development/frontend/README.md).
It is necessary to run both the ember server and as well as the python backend server to get the service up and running.

Then, in a terminal, type

```sh
(badgeyay/api) $ export FLASK_APP=run.py
(badgeyay/api)$ flask run
```
![screenshot from 2018-09-29 13-22-06](https://user-images.githubusercontent.com/17084322/46243038-f8488300-c3ec-11e8-9884-664cd7410ca7.png)

![screenshot from 2018-09-29 13-22-25](https://user-images.githubusercontent.com/17084322/46243053-1a420580-c3ed-11e8-8064-d686d9756a85.png)
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
