# -*- coding:utf-8 -*-
from appium import webdriver
import unittest
import time
import sys
import os 
sys.path.append("..")
from Base.Init import *
from Base.imgProcess import getImgCordinate
from Base.monkeyBase import AndroidBaseOperation

# 读取 配置表、匹配图片路径、截图路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
f_config, queryImgPath, sceneFilePath = conf_Init('config.yml')
base = AndroidBaseOperation() # 实例化
# print(queryImgPath)

class GameOpencvTests(unittest.TestCase):
	# 初始化
	def setUp(self):
		desired_caps = {}
		desired_caps["platformName"] = "Android"
		desired_caps["deviceName"] = "d"
		desired_caps["appPackage"] = "com.game37.bayechuanqi" # adb shell pm list packages | find 'testerhome'
		desired_caps["appActivity"] = ".AppActivity" # adb logcat | grep ActivityManager | grep cmp
		desired_caps["noReset"] = "true"  # 不需要再次安装
		desired_caps["fullreset"] = "true"
		desired_caps["defaultCommandTimeout"] = 600
		#desired_caps['unicodeKeyboard'] = 'true'
		#desired_caps['resetKeyboard'] = 'true'
		self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps) # 启动app

	# 测试Case
	def test_findnpc(self):
		# 检查有没有安装app
		if not self.driver.is_app_installed("com.game37.bayechuanqi"):
			print("the app is not install")
			return
			try:
				self.driver.start_activity('com.game37.bayechuanqi','.AppActivity')
			except:
				print("Start the Activity error")
		time.sleep(4)		
		base.click(100,100,1)  # 跳过动画
		base.click(100,100,1)
		base.click(100,100,1)
		time.sleep(3)
		case = getYaml('login.yaml')
		for item in case['testcase']:
			if item['operate_type'] == 'click':
				find_click(queryImgPath,item['query_img'],sceneFilePath,int(item['time']))
			if item['operate_type'] == 'check':
				exist_pic(queryImgPath,item['query_img'],sceneFilePath)
		print('ok')
		# 测试结束清理
	def tearDown(self):
		self.driver.quit()



if __name__ == '__main__':
	unittest.main()


