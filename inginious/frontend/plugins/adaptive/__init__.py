# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

#from inginious.frontend.pages.utils import INGIniousAuthPage, INGIniousPage
#import web
from inginious.frontend.plugins.adaptive.Adaptive_course import *
from inginious.frontend.plugins.adaptive.Test_page import *

def test_pass(course):
    tasks = course.get_tasks()
    # user_tasks = self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})

    return True

def course_menu(course, template_helper):
    """ Displays the link to the adaptive view on the course page, if the plugin is activated for this course """
    adaptive = course.get_descriptor().get('adaptive', [])

    # username = self.user_manager.session_username()

    '''
    test ici if Test succedeed or not
    '''

    if adaptive != []:
        return str(template_helper.get_custom_renderer('frontend/plugins/adaptive', layout=False).course_menu(course))
    else:
        return None

def init(plugin_manager, _, _2, _3):
    """ Init the plugin """
    page_pattern_course = r'/adaptive/([a-z0-9A-Z\-_]+)'
    plugin_manager.add_page(page_pattern_course, AdaptivePage)
    plugin_manager.add_hook('course_menu', course_menu)
    #plugin_manager.add_hook('submission_done', submission_done)

    page_pattern_test = r'/adaptive/test/([a-z0-9A-Z\-_]+)'
    plugin_manager.add_page(page_pattern_test, TestPage)