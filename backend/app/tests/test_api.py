from time import sleep
import unittest
import requests
import os
import json


class APITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.CSVPath = os.path.abspath(os.path.join(os.getcwd(), 'backend/sample/vip.png.csv'))
        cls.ImagePath = os.path.abspath(os.path.join(os.getcwd(), 'backend/badges/badge_1.png'))
        cls.ResponsesPath = os.path.abspath(os.path.join(os.getcwd(), 'backend/app/tests/expected_responses.json'))
        cls.Responses = json.load(open(cls.ResponsesPath))
        cls.URL = 'http://127.0.0.1:5000/api/v1.0/generate_badges'
        super(APITest, cls).setUpClass()

    def test_user_entered_data(self):
        # Tests manual entering of data with a default image
        Data = {
            'csv': 'test,test,test,test',
            'img-default': 'user_defined.png',
            'bg_color': '000000'
        }
        sleep(2)
        r = requests.post(self.URL, data=Data, timeout=10)
        self.assertEqual(json.loads(r.text)['response'], self.Responses['test_user_entered_data'])

    def test_csv_upload(self):
        # Tests uploading csv with a default image
        File = {'file': open(self.CSVPath, 'rb')}
        Data = {
            'img-default': 'user_defined.png',
            'bg_color': '000000'
        }
        sleep(2)
        r = requests.post(self.URL, data=Data, files=File, timeout=10)
        self.assertEqual(json.loads(r.text)['response'], self.Responses['test_csv_upload'])

    def test_img_upload(self):
        # Tests uploading background image
        File = {
            'image': open(self.ImagePath, 'rb'),
            'file': open(self.CSVPath, 'rb')
        }
        sleep(2)
        r = requests.post(self.URL, files=File, timeout=10)
        self.assertEqual(json.loads(r.text)['response'], self.Responses['test_img_upload'])

    def test_bg_color(self):
        # Tests using a color as background
        File = {'file': open(self.CSVPath, 'rb')}
        Data = {
            'img-default': 'user_defined.png',
            'bg_color': '000000'
        }
        sleep(2)
        r = requests.post(self.URL, data=Data, files=File, timeout=10)
        self.assertEqual(json.loads(r.text)['response'], self.Responses['test_bg_color'])

    def test_custom_font(self):
        # Tests choosing custom font
        File = {'file': open(self.CSVPath, 'rb')}
        Data = {
            'img-default': 'user_defined.png',
            'bg_color': '000000',
            'custfont': 'sans'
        }
        sleep(2)
        r = requests.post(self.URL, data=Data, files=File, timeout=10)
        self.assertEqual(json.loads(r.text)['response'], self.Responses['test_custom_font'])

    @classmethod
    def tearDownClass(cls):
        super(APITest, cls).tearDownClass()
