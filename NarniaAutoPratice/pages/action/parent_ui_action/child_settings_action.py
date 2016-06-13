__author__ = 'hung.duong'

from pages.action.common_page import CommonPage
from pages.screen.parent_ui_screen import child_controls_screen


class ChildControls(CommonPage):
    def title(self):
        return self.driver.find_element_by_id(child_controls_screen.title_screen_ID).text

    def click_back_home(self):
        self.driver.find_element_by_id(child_controls_screen.home_ID).click()

    def click_add_another_child(self):
        self.driver.find_element_by_id(child_controls_screen.add_another_child_ID).click()

    def click_first_child(self):
        self.driver.find_element_by_name(child_controls_screen.first_child_Name).click()

    def click_view_usage_details(self):
        self.driver.find_element_by_id(child_controls_screen.view_usage_detail_link_ID).click()

    def click_edit_profile(self):
        self.driver.find_element_by_id(child_controls_screen.edit_profile_link_ID).click()

    def click_profile_permission(self):
        self.driver.find_element_by_name(child_controls_screen.profile_permission_Name).click()

    def click_time_controls(self):
        self.driver.find_element_by_name(child_controls_screen.time_controls_Name).click()