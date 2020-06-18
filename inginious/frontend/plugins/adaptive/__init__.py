# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

from inginious.frontend.plugins.adaptive.Adaptive_course import *
from inginious.frontend.plugins.adaptive.Test_Page import *
from inginious.frontend.plugins.adaptive.TaskAdaptivePage import *
from inginious.frontend.plugins.adaptive.TaskTestPage import *


def course_menu(course, template_helper):
    """ Displays the link to the adaptive view on the course page"""
    adaptive = course.get_descriptor().get('adaptive', [])
    if not adaptive:
        return
    else:
        return str(template_helper.get_custom_renderer('frontend/plugins/adaptive', layout=False).course_menu(course))

def task_menu(course, task, template_helper):
    """ Displays the link to the adaptive view on the task page"""
    adaptive = course.get_descriptor().get('adaptive', [])
    if not adaptive:
        return
    else:
        return str(template_helper.get_custom_renderer('frontend/plugins/adaptive', layout=False).task_menu(course))

def init(plugin_manager, _, _2, _3):
    """ Init the plugin """

    page_pattern_course = r'/adaptive/([a-z0-9A-Z\-_]+)'
    plugin_manager.add_page(page_pattern_course, AdaptivePage)

    page_pattern_task = r'/adaptive/([a-z0-9A-Z\-_]+)/([a-z0-9A-Z\-_]+)'
    plugin_manager.add_page(page_pattern_task, TaskAdaptivePage)

    page_pattern_test = r'/adaptive_test/([a-z0-9A-Z\-_]+)'
    plugin_manager.add_page(page_pattern_test, TestPage)

    page_pattern_test_task = r'/adaptive_test/([a-z0-9A-Z\-_]+)/([a-z0-9A-Z\-_]+)'
    plugin_manager.add_page(page_pattern_test_task, TaskTestPage)

    plugin_manager.add_hook('course_menu', course_menu)

    plugin_manager.add_hook('task_menu', task_menu)
