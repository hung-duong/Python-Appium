__author__ = 'hung.duong'

from pages.action.common_page import CommonPage
from pages.screen.parent_ui_screen import time_controls_screen


class TimeControls(CommonPage):
    def title(self):
        return self.driver.find_element_by_id(time_controls_screen.title_screen_ID).text

    def click_back_home(self):
        self.driver.find_element_by_id(time_controls_screen.home_ID).click()