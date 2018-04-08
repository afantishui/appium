from appium import webdriver
import selenium

import time
desired_caps = {
            'platformName': 'Android',
            'fastReset': 'false',
            'deviceName': 'XXXXXX',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'fullReset': 'false',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True',
            'noReset': 'True',
            'chromeOptions': {
                'androidProcess': 'com.tencent.mm:appbrand0'
                }
            }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
print(driver.page_source)
driver.find_element_by_name("发现").click()
driver.find_element_by_name("小程序").click()
driver.find_element_by_name("X东购物").click()
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
time.sleep(5)
print(driver.page_source)