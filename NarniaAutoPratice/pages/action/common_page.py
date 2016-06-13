__author__ = 'hung.duong'

from appium import webdriver


class CommonPage():
    driver = None

    def launch_page(self, packageApp, activityApp):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'EIV8OBFMQCJNKRRC'

        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = packageApp
        desired_caps['appActivity'] = activityApp
        CommonPage.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def close_driver(self):
        try:
            CommonPage.driver.quit()
        except Exception, e:
            CommonPage.driver = None
            print('Error while closing app:' + e.message)
