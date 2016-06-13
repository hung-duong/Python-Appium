__author__ = 'hung.duong'

from lib.const_page import PageName
from pages.action.pagefactory import page_factory
from behave import given, when, then
from hamcrest import assert_that, equal_to


@when('go to child controls page')
def step_go_to_page(context):
    page_factory(PageName.PARENT_SETTINGS).click_child_controls()

@when('go to add another child page')
def step_go_to_page(context):
    page_factory(PageName.CHILD_SETTINGS).click_add_another_child()

@when('go to first child page')
def step_go_to_page(context):
    page_factory(PageName.CHILD_SETTINGS).click_first_child()

@when('go to view usage details page')
def step_go_to_page(context):
    page_factory(PageName.CHILD_SETTINGS).click_view_usage_details()

@when('go to edit profile page')
def step_go_to_page(context):
    page_factory(PageName.CHILD_SETTINGS).click_edit_profile()

@when('go to profile permission page')
def step_go_to_page(context):
    page_factory(PageName.CHILD_SETTINGS).click_profile_permission()

@when('go to time controls page')
def step_go_to_page(context):
    page_factory(PageName.CHILD_SETTINGS).click_time_controls()


@then('check title {page}')
def step_check_title(context, page):
    if page == PageName.CHILD_SETTINGS:
        assert_that(page_factory(PageName.CHILD_SETTINGS).title(), equal_to("Child Controls"))
    elif page == PageName.ADD_ANOTHER_CHILD:
        assert_that(page_factory(PageName.ADD_ANOTHER_CHILD).title(), equal_to("Who will play with this device?"))
    elif page == PageName.VIEW_USAGE_DETAILS:
        assert_that(page_factory(PageName.VIEW_USAGE_DETAILS).title(), equal_to("Usage Details for Vcc"))
    elif page == PageName.EDIT_PROFILE:
        assert_that(page_factory(PageName.EDIT_PROFILE).title(), equal_to("Edit profile for Vcc"))
    elif page == PageName.PROFILE_PERMISSION:
        assert_that(page_factory(PageName.PROFILE_PERMISSION).title(), equal_to("Profile Permissions"))
    elif page == PageName.TIME_CONTROLS:
        assert_that(page_factory(PageName.TIME_CONTROLS).title(), equal_to("Vcc's Time Controls"))