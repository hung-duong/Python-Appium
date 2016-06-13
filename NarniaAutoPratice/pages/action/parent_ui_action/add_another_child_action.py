__author__ = 'hung.duong'

from pages.action.common_page import CommonPage
from pages.screen.parent_ui_screen import add_another_child_screen


class AddAnotherChild(CommonPage):
    def title(self):
        return self.driver.find_element_by_id(add_another_child_screen.title_screen_ID).text

    def click_back_home(self):
        self.driver.find_element_by_id(add_another_child_screen.home_ID).click()