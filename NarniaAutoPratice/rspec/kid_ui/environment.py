__author__ = 'hung.duong'

from pages.action.common_page import CommonPage

def before_all(context):
    context.common_page = CommonPage()
    context.packageApp = 'com.lvlstudio.leapfrog.kidlauncher'
    context.activityApp = 'com.lvl.kidlauncher.KidActivity'


def after_scenario(context, scenario):
    context.common_page.close_driver()
