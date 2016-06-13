__author__ = 'hung.duong'

from pages.action.common_page import CommonPage
from pages.screen.parent_ui_screen import view_usage_details_screen


class ViewUsageDetails(CommonPage):
    def title(self):
        return self.driver.find_element_by_id(view_usage_details_screen.title_screen_ID).text

    def click_close(self):
        self.driver.find_element_by_id(view_usage_details_screen.close_ID).click()