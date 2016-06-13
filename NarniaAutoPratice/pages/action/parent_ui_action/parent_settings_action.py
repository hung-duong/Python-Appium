__author__ = 'hung.duong'

from pages.action.common_page import CommonPage
from pages.screen.parent_ui_screen import parent_settings_screen


class ParentSettings(CommonPage):
    def title(self):
        return self.driver.find_element_by_id(parent_settings_screen.title_screen_ID)

    def click_child_controls(self):
        self.driver.find_element_by_name("Child Controls").click()

    def click_app_manager(self):
        self.driver.find_element_by_name("App Manager").click()

    def click_camera(self):
        self.driver.find_element_by_name("Camera").click()

    def click_all_apps(self):
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
