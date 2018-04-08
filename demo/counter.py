import unittest
import time
from appium import webdriver

class AndroidTests(unittest.TestCase):

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		#desired_caps['platformVersion'] = '7.0'
		desired_caps['deviceName'] = 'd'	
		desired_caps['appPackage'] = 'com.miui.calculator'
		desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity'
		#remote = 'https://127.0.0.1:4723/wd/hub'
		self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
		

	def tearDown(self):
		self.driver.quit()

	def test_plus(self):
		self.driver.find_element_by_xpath("//android.widget.Button[@text='1']").click()
		self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="加"]').click()
		self.driver.find_element_by_xpath("//android.widget.Button[@text='9']").click()
		self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="等于"]').click()
		time.sleep(1)
		result = self.driver.find_element_by_xpath("//android.widget.TextView[@text='10']") #android.widget.TextView[2]
		if result is not None:
			print('pass')
		else:
			print('fail')

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
	unittest.TextTestRunner(verbosity = 2).run(suite)