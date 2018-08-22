#!/usr/local/bin/python3

import os
import subprocess
import sys

# Pre-push hook that executes the Python/JS linters on all files that
# deviate from develop.
# To bypass the validation upon `git push` use the following command:
# `git push REMOTE BRANCH --no-verify`
# Change the first line of this file if your python3 installation
# is elsewhere.


def main():

    # flake8 linting tests for backend.
    # Make sure flake8 is installed in the virtual environment or give
    # the path where flake8 is installed.
    print('Running flake8 tests...')
    result = subprocess.run([os.getcwd() + '/venv/bin/flake8', 'api/'], stdout=subprocess.PIPE)
    check = result.stdout.decode('utf-8')
    if check:
        print('Please correct the linting errors: ')
        print(result.stdout.decode('utf-8'))
        sys.exit(1)
    print('Flake8 tests passed.')

    # ember tests for frontend.
    print('Running ember tests...')
    result_front = subprocess.run(['ember', 'test'], cwd='frontend', stdout=subprocess.PIPE)
    if result_front.returncode:
        print(result_front.stdout.decode('utf-8'))
        sys.exit(1)
    print('Ember tests passed.')


if __name__ == '__main__':
    main()
