from selenium import webdriver
import unittest
import time

class BadgeyayTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		super(BadgeyayTest, cls).setUpClass()

	def test_title(self):
		self.driver.get('http://localhost:5000')
		self.assertEqual(self.driver.title, 'BadgeYay')

	def test_menu(self):
		self.driver.get('http://localhost:5000')
		elem = self.driver.find_element_by_css_selector(".custom-menu-content")
		self.assertFalse(elem.is_displayed())
		self.driver.find_element_by_css_selector(".glyphicon-th").click()
		self.assertTrue(elem.is_displayed())
		self.driver.find_element_by_css_selector(".glyphicon-th").click()
		self.assertFalse(elem.is_displayed())

	def test_error(self):
		self.driver.get('http://localhost:5000')
		self.driver.find_element_by_css_selector("form .btn-danger").click()
		time.sleep(2)
		success = self.driver.find_element_by_css_selector(".flash-error")
		self.assertIn(u'Please select a CSV file to Upload!', success.text)


	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		super(BadgeyayTest, cls).tearDownClass()
