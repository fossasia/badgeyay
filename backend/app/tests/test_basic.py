#!/usr/bin/env python3

"""Tests for Basic Functions"""
import sys
import json
import unittest

sys.path.append("../..")
from app.main import *


class TestFunctions(unittest.TestCase):

    def setup(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_output(self):
        with app.test_request_context():
            out = output('error', 'Test Error', 'local_host')
            response = [
                {
                    'type': 'error',
                    'message': 'Test Error',
                    'download_link': 'local_host'
                }
            ]
            data = json.loads(out.get_data(as_text=True))
            self.assertEqual(data['response'], response)


if __name__ == '__main__':
    unittest.main()
