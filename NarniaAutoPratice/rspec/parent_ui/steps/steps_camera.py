__author__ = 'hung.duong'

from lib.const_page import PageName
from pages.action.pagefactory import page_factory
from behave import given, when, then
from hamcrest import assert_that, equal_to


@when('go to all apps page')
def step_go_to_page(context):
    page_factory(PageName.PARENT_SETTINGS).click_all_apps()


@when('go to camera page')
def step_go_to_page(context):
    page_factory(PageName.PARENT_SETTINGS).click_camera()

@then('take picture with {type} camera')
def step_take_picture(context, type):
    page_factory(PageName.CAMERA).delete_all_pictures()
    if type == 'front':
        page_factory(PageName.CAMERA).take_front_camera()
    else:
        page_factory(PageName.CAMERA).take_back_camera()

@then('check taken picture')
def step_check_taken_picture(context):
    assert_that(page_factory(PageName.CAMERA).is_taken_picture(), equal_to(1))
    page_factory(PageName.CAMERA).delete_all_pictures()