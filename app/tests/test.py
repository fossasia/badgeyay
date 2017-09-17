from selenium import webdriver
import unittest
import time

class BadgeyayTest(unittest.TestCase):

	@classmethod
	def setup(self):
		self.driver.get('http://localhost:5000')
		
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		super(BadgeyayTest, cls).setUpClass()

	def test_title(self):
		self.assertEqual(self.driver.title, 'BadgeYay')

	def test_menu_visibility(self):
		#elem is div element of right most menu bar ,until glyphicon is not clicked it should not
		#display all menus like (code, bug report etc)
		elem = self.driver.find_element_by_css_selector(".custom-menu-content")
		self.assertFalse(elem.is_displayed())
	
	def test_menu_click_on(self):
		#elem is glyphicon element, when it is clicked it should display menu bar containing
		#(code,bug reports etc)
		elem=self.driver.find_element_by_css_selector(".glyphicon-th").click()
		self.assertTrue(elem.is_displayed())
	
	def test_menu_click_off(self):
		#elem is glyphicon element, when it is clicked again it should hide menu bar containing
		#(code,bug reports etc)		
		elem=self.driver.find_element_by_css_selector(".glyphicon-th").click()
		self.assertFalse(elem.is_displayed())

	def test_error(self):
		self.driver.find_element_by_css_selector("form .btn-danger").click()
		time.sleep(2)
		success = self.driver.find_element_by_css_selector(".flash-error")
		self.assertIn(u'Please select a CSV file to Upload!', success.text)


	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		super(BadgeyayTest, cls).tearDownClass()
