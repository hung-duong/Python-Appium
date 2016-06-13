__author__ = 'hung.duong'

from lib.const_page import PageName
from pages.action.pagefactory import page_factory
from behave import given, when, then


@given('open parent settings page')
def step_open_parent_settings_page(context):
    page_factory(PageName.PARENT_SETTINGS).launch_page(context.packageApp, context.activityApp)
