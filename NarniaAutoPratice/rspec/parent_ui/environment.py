__author__ = 'hung.duong'

from pages.action.common_page import CommonPage

def before_all(context):
    context.common_page = CommonPage()
    context.packageApp = 'com.android.launcher'
    context.activityApp = 'com.android.launcher2.Launcher'


def after_scenario(context, scenario):
    context.common_page.close_driver()
