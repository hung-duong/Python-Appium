__author__ = 'hung.duong'

from lib.const_page import PageName
from pages.action.pagefactory import page_factory
from behave import given, when, then
import time


@given('open Kid UI page')
def step_open_kid_ui_page(context):
    page_factory(PageName.KID_UI).launch_page(context.packageApp, context.activityApp)


@given('launch to title {name}')
def step_open_kid_ui_page(context, name):
    if name == 'end 1':
        context.packageApp = 'com.leapfrog.weeklyengagement'
        context.activityApp = 'com.leapfrog.weeklyengagement.MainActivity'
        page_factory(PageName.TITLE_END_1).launch_page(context.packageApp, context.activityApp)
    elif name == 'end 2':
        context.packageApp = 'com.leapfrog.dailyengagement'
        context.activityApp = 'com.leapfrog.dailyengagement.MenuActivity'
        page_factory(PageName.TITLE_END_2).launch_page(context.packageApp, context.activityApp)
    elif name == 'stretchy monkey':
        context.packageApp = 'com.leapfrog.ANDS.app.x00200026.AP_SM2'
        context.activityApp = 'com.leapfrog.ANDS.app.x00200026.AP_SM2.LFMainActivity'
        page_factory(PageName.TITLE_STRETCHY_MONKEY).launch_page(context.packageApp, context.activityApp)

    time.sleep(30)


@when('enter game')
def step_enter_game(context):
    return


@when('play game 5 minutes')
def step_play_game(context):
    return

