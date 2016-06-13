__author__ = 'hung.duong'

from pages.action.common_page import CommonPage
from pages.screen.parent_ui_screen import profile_permission_screen


class ProfilePermission(CommonPage):
    def title(self):
        return self.driver.find_element_by_id(profile_permission_screen.title_screen_ID).text

    def click_back_home(self):
        self.driver.find_element_by_id(profile_permission_screen.home_ID).click()