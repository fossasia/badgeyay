# Local Development Setup

The instructions on this page will guide you in setting up a local development
environment in your system. First things first, BadgeYay needs `Python 3` to run.
Most of the distros come bundled with that but if it is not there please install it first.

These are some additional depencies that you will need:

```sh
$ sudo apt-get update
$ sudo apt-get install librsvg2-bin pdftk
```

Make sure you have the dependencies mentioned above installed before proceeding further.
For a start, fork BadgeYay to your own github account. Then, clone it to your local system.

```sh
$ git clone -b development https://github.com/<your_username>/badgeyay.git
```

Add an upstream remote so that you can push your patched branches for starting a PR .

```sh
$ cd badgeyay
$ git remote add upstream https://github.com/fossasia/badgeyay.git
```

* It is recommended that you use [`virtualenv`](https://virtualenv.pypa.io/en/stable/installation/)
and [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) to maintain a clean Python 3 environment. Create a `virtualenv`:

```sh
$ mkvirtualenv -p python3 badgeyay
(badgeyay) $ deactivate         # To deactivate the virtual environment
$ workon badgeyay               # To activate it again
```

* Now, since you are inside a virtual environment, you can setup `badgeyay` as an editable package.

```sh
(badgeyay) $ pip install -e .
```

* Create application environment variables.

```
cp .env.example .env
```

* To run the project on a local machine.

```sh
(badgeyay) $ python app/main.py
```

## Preferred Development Workflow

1. Activate the virtual environment.

```sh
$ workon badgeyay               # To activate it again
(badgeyay) $
```

2. Get the latest copy of code from upstream.

```sh
(badgeyay) $ git pull upstream development
```

3. Once you get assigned an issue, create a new branch from `development`.

```sh
(badgeyay) $ git checkout -b XXX-mock-issue     # XXX is the issue number
```

4. Work on your patch, test it and when it's done, push it to your fork.

```sh
(badgeyay) $ git push origin XXX-mock-issue
```
5. File a PR and wait for the maintainers to suggest reviews or in the best case
merge the PR. Then just update `development` of your local clone.

```sh
(badgeyay) $ git pull upstream master
```

And then loop back again. For contribution guidelines, refer [here](https://github.com/fossasia/badgeyay/blob/development/.github/CONTRIBUTING.md)
