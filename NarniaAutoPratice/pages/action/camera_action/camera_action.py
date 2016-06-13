__author__ = 'hung.duong'

from pages.action.common_page import CommonPage
from pages.screen.camera_screen import camera_screen
import os


class Camera(CommonPage):
    def get_camera_open(self):
        cmd = "adb shell dumpsys media.camera | grep 'Device is'"
        res = str(os.popen(cmd).read()).split('\n')

        if res[0].find("open") > 0:
            return "Back"
        elif res[1].find("open") > 0:
            return "Front"

    def take_front_camera(self):
        if Camera().get_camera_open() == "Back":
            self.driver.find_element_by_id(camera_screen.camera_flip_btn).click()
        self.driver.find_element_by_id(camera_screen.shutter_photo_btn).click()

    def take_back_camera(self):
        if Camera().get_camera_open() == "Front":
            self.driver.find_element_by_id(camera_screen.camera_flip_btn).click()
        self.driver.find_element_by_id(camera_screen.shutter_photo_btn).click()

    def is_taken_picture(self):
        cmd = "adb shell ls /sdcard/DCIM/Camera/"
        res = str(os.popen(cmd).read()).split('\n')
        if len(res) == 1:
            return 1

        return 0

    def delete_all_pictures(self):
        cmd = "adb shell rm -f /sdcard/DCIM/Camera/*"
        os.popen(cmd)