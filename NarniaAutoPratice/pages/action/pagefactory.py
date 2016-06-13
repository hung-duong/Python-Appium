__author__ = 'hung.duong'

from pages.action.parent_ui_action.parent_settings_action import ParentSettings
from pages.action.parent_ui_action.child_settings_action import ChildControls
from pages.action.parent_ui_action.add_another_child_action import AddAnotherChild
from pages.action.parent_ui_action.view_usage_details_action import ViewUsageDetails
from pages.action.parent_ui_action.edit_profile_action import EditProfile
from pages.action.parent_ui_action.profile_permission_action import ProfilePermission
from pages.action.parent_ui_action.time_controls_action import TimeControls
from pages.action.camera_action.camera_action import Camera
from pages.action.kid_ui.kid_ui_action import KidUI
from pages.action.title_launch_action.title_end_1_action import TitleEnd1
from pages.action.title_launch_action.title_end_2_action import TitleEnd2
from pages.action.title_launch_action.title_stretchy_monkey_action import TitleStretchyMonkey


def page_factory(page_name):
    test_obj = None
    page_name = page_name.lower()

    if page_name == 'parent settings':
        test_obj = ParentSettings()
    elif page_name == 'child controls':
        test_obj = ChildControls()
    elif page_name == 'add another child':
        test_obj = AddAnotherChild()
    elif page_name == 'view usage details':
        test_obj = ViewUsageDetails()
    elif page_name == 'profile permission':
        test_obj = ProfilePermission()
    elif page_name == 'edit profile':
        test_obj = EditProfile()
    elif page_name == 'time controls':
        test_obj = TimeControls()
    elif page_name == 'camera':
        test_obj = Camera()
    elif page_name == 'kid ui':
        test_obj = KidUI()
    elif page_name == 'end 1':
        test_obj = TitleEnd1()
    elif page_name == 'end 2':
        test_obj = TitleEnd2()
    elif page_name == 'stretchy monkey':
        test_obj = TitleStretchyMonkey()

    return test_obj
