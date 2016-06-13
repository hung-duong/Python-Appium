__author__ = 'hung.duong'

import unittest, time, os
from appium import webdriver
from time import sleep

class Android_Parent_Screen(unittest.TestCase):
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'EIV8OBFMQCJNKRRC'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'com.android.launcher'
        desired_caps['appActivity'] = 'com.android.launcher2.Launcher'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
    def test_parents_screen(self):
        header_txt = self.driver.find_element_by_id('com.android.launcher:id/testTextView')
        self.assertEqual("Parents", header_txt.text)

        # Go to Child Controls
        child_controls_btn = self.driver.find_element_by_name("Child Controls")
        self.assertIsNot(None, child_controls_btn)
        child_controls_btn.click()
        header_txt = self.driver.find_element_by_id('com.quanta.childsettings:id/txt_title_text')
        self.assertEqual("Child Controls", header_txt.text)

        # Add Profile
        add_child_lbl = self.driver.find_element_by_name("Add another child")
        add_child_lbl.click()
        header_txt = self.driver.find_element_by_id('com.quanta.childsettings:id/add_profile_subheader')
        self.assertEqual("Who will play with this device?", header_txt.text)

        first_name_txt = self.driver.find_element_by_id('com.quanta.childsettings:id/txt_first_name')
        first_name_txt.send_keys("Hung Duong")

        self.driver.find_element_by_id('com.quanta.childsettings:id/spn_month_md').click()
        self.driver.find_element_by_name('Set').click()

        self.driver.find_element_by_id('com.quanta.childsettings:id/spn_gender').click()
        self.driver.find_element_by_id('com.quanta.childsettings:id/radio_male').click()
        self.driver.find_element_by_id('com.quanta.childsettings:id/btn_info_set').click()

        self.driver.find_element_by_id('com.quanta.childsettings:id/spn_gender').click()
        self.driver.find_element_by_id('com.quanta.childsettings:id/btn_info_set').click()

        self.driver.find_element_by_id('com.quanta.childsettings:id/btn_next').click()
        self.driver.find_element_by_id('com.quanta.childsettings:id/btn_next').click()

        self.driver.find_element_by_id('com.quanta.childsettings:id/btn_title_home').click()

        # Go to App Manager
        app_manager_btn = self.driver.find_element_by_name("App Manager")
        self.assertIsNot(None, app_manager_btn)
        app_manager_btn.click()
        header_txt = self.driver.find_element_by_id('android:id/action_bar_title')
        self.assertEqual("App Manager", header_txt.text)
        self.driver.find_element_by_id('android:id/home').click()

        # Go to App Manager
        device_btn = self.driver.find_element_by_name("Device")
        self.assertIsNot(None, device_btn)
        device_btn.click()
        header_txt = self.driver.find_element_by_id('com.quanta.parentsettings:id/txt_title_text')
        self.assertEqual("Device", header_txt.text)
        self.driver.find_element_by_id('com.quanta.parentsettings:id/btn_title_home').click()

        # Go to System Info
        system_info_btn = self.driver.find_element_by_name("System Info")
        self.assertIsNot(None, system_info_btn)
        system_info_btn.click()
        header_txt = self.driver.find_element_by_id('android:id/action_bar_title')
        self.assertEqual("System Info", header_txt.text)
        self.driver.find_element_by_id('android:id/home').click()

        # Go to All Apps
        all_apps = self.driver.find_element_by_class_name('android.widget.ImageView')
        all_apps.click()
        header_txt = self.driver.find_element_by_class_name('android.widget.TextView')
        self.assertEqual("Apps", header_txt.text)

        # Go to Calendar
        calendar_btn = self.driver.find_element_by_name("Calendar")
        self.assertIsNot(None, calendar_btn)
        calendar_btn.click()
        month_title = self.driver.find_element_by_id('com.leapfrog.ANDS.app.x00280015.NUTL:id/listView_monthtitle')
        self.assertEqual("March, 2015", header_txt.text)
        self.driver.back()

        # Go to Camera
        camera_btn = self.driver.find_element_by_name("Camera")
        self.assertIsNot(None, camera_btn)
        camera_btn.click()
        camera_mode_btn = self.driver.find_element_by_id('com.android.gallery3d:id/camera_mode')
        self.assertIsNot(None, camera_mode_btn)
        shutter_photo_btn = self.driver.find_element_by_id('com.android.gallery3d:id/shutter_button_photo')
        self.assertIsNot(None, shutter_photo_btn)
        self.driver.back()

        # Go to Dev Tools
        dev_tools_btn = self.driver.find_element_by_name("Dev Tools")
        self.assertIsNot(None, dev_tools_btn)
        dev_tools_btn.click()
        header_txt = self.driver.find_element_by_id('android:id/action_bar_title')
        self.assertEqual("Dev Tools", header_txt.text)
        self.driver.back()

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_Parent_Screen)
    unittest.TextTestRunner(verbosity=2).run(suite)
