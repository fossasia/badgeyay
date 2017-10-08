#!/usr/bin/env bash
python app/main.py > /dev/null &
nosetests app/tests/test.py --with-coverage