from selenium import webdriver
import unittest
import time
import os

is_travis = 'TRAVIS' in os.environ
os.environ['MOZ_HEADLESS'] = '1'

class BadgeyayTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://localhost:5000')
        super(BadgeyayTest, cls).setUpClass()

    def test_title(self):
        self.assertEqual(self.driver.title, 'BadgeYay')

    def test_menu_visibility(self):
        # Check that menu is not visible initially
        elem = self.driver.find_element_by_css_selector(".custom-menu-content")
        self.assertFalse(elem.is_displayed())

    def test_menu_click_on_off(self):
        # Check that menu is visible when opened
        elem = self.driver.find_element_by_css_selector(".custom-menu-content")
        self.driver.find_element_by_css_selector(".glyphicon-th").click()
        self.assertTrue(elem.is_displayed())
        self.driver.find_element_by_css_selector(".glyphicon-th").click()
        self.assertFalse(elem.is_displayed())

    def test_error(self):
        self.driver.find_element_by_css_selector("form .btn-primary").click()
        time.sleep(2)
        success = self.driver.find_element_by_css_selector(".flash-error")
        self.assertIn(u'Please select a CSV file to Upload!', success.text)

    def test_select_background_upload(self):
        CSVpath = os.path.abspath(os.path.join(os.getcwd(), 'sample/vip.png.csv'))
        self.driver.find_element_by_name("file").send_keys(CSVpath)
        self.driver.find_element_by_css_selector(".btn-group .dropdown-toggle").click()
        self.driver.find_element_by_css_selector("li[data-item='team.png']").click()
        self.driver.find_element_by_css_selector("form .btn-primary").click()
        time.sleep(3)
        success = self.driver.find_element_by_css_selector(".flash-success")
        self.assertIn(u'Your badges has been successfully generated!', success.text)

    def test_png_upload(self):
        Imagepath = os.path.abspath(os.path.join(os.getcwd(), 'badges/badge_1.png'))
        CSVpath = os.path.abspath(os.path.join(os.getcwd(), 'sample/vip.png.csv'))
        self.driver.find_element_by_name("file").send_keys(CSVpath)
        self.driver.find_element_by_name("image").send_keys(Imagepath)
        self.driver.find_element_by_css_selector("form .btn-primary").click()
        time.sleep(3)
        success = self.driver.find_element_by_css_selector(".flash-success")
        self.assertIn(u'Your badges has been successfully generated!', success.text)

    def test_csv_upload(self):
        CSVpath = os.path.abspath(os.path.join(os.getcwd(), 'sample/vip.png.csv'))
        self.driver.find_element_by_name("file").send_keys(CSVpath)
        self.driver.find_element_by_css_selector("form .btn-primary").click()
        time.sleep(3)
        success = self.driver.find_element_by_css_selector(".flash-error")
        self.assertIn(u'Please upload an image in \'PNG\' format!', success.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(BadgeyayTest, cls).tearDownClass()
