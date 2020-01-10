# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

from inginious.frontend.pages.utils import INGIniousAuthPage, INGIniousPage
import web

class AdaptivePage(INGIniousAuthPage):

    def GET(self, courseid):
        course = self.get_course(courseid)
        return self.show_page(course)

    def get_course(self, courseid):
        """ Return the course """
        try:
            course = self.course_factory.get_course(courseid)
        except:
            raise web.notfound()

        return course

    def is_available(self, node, course):
        parents = node["content"]["parent"]
        print(parents)
        for parent in parents:
            if not self.is_complete(parent, course):
                return False
        return True

    def is_complete(self, node, course):
        username = self.user_manager.session_username()
        #course = self.course_factory.get_course(courseid)
        #tasks = [task for taskid, task in course.get_tasks().items() if self in task.get_categories()]
        tasks = course.get_tasks()
        user_tasks = self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})
        for user_task in user_tasks:
            task = course.get_task(user_task["taskid"])
            if node in task.get_categories() and not user_task["succeeded"]:
                return False
        return True

    def get_tasks_data(self, course):
        username = self.user_manager.session_username()
        #course = self.course_factory.get_course(courseid)
        tasks = course.get_tasks() # return taskid as str
        # tasks.items return taskid, task
        user_tasks = self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})
        bases = course.get_descriptor().get('adaptive', [])["base"]
        tree = course.get_descriptor().get('adaptive', [])["tree"]
        '''
        for node in tree:
            if node["content"]["parent"]:
                print(node["content"]["parent"].keys())
            for parent in node["content"]["parent"]:
                print(parent)
        '''
        tasks_data = {}
        is_admin = self.user_manager.has_staff_rights_on_course(course, username)

        tasks_score = [0.0, 0.0]

        for taskid, task in tasks.items():
            #tasks_data[taskid] = {"visible": task.get_accessible_time().after_start() or is_admin, "succeeded": False,
            #                      "grade": 0.0}
            tasks_data[taskid] = {"visible": False or is_admin, "succeeded": False,
                                  "grade": 0.0}
            #tasks_data[taskid] = {"visible": False, "succeeded": False,
            #"grade": 0.0}
            tasks_score[1] += task.get_grading_weight() if tasks_data[taskid]["visible"] else 0

        for node in tree:
            if self.is_available(node, course):
                for user_task in user_tasks:
                    task = course.get_task(user_task["taskid"])
                    tags = task.get_categories()
                    if node["node"] in tags:
                        tasks_data[user_task["taskid"]]["visible"] = task.get_accessible_time().after_start() or is_admin
                        tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
                        tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]

                        weighted_score = user_task["grade"]*tasks[user_task["taskid"]].get_grading_weight()
                        tasks_score[0] += weighted_score if tasks_data[user_task["taskid"]]["visible"] else 0

        '''
        for user_task in user_tasks:
            task = course.get_task(user_task["taskid"])
            tag = task.get_categories()
            tasks_data[user_task["taskid"]]["visible"] = task.get_accessible_time().after_start() or is_admin
            tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
            tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]

            weighted_score = user_task["grade"]*tasks[user_task["taskid"]].get_grading_weight()
            tasks_score[0] += weighted_score if tasks_data[user_task["taskid"]]["visible"] else 0
        '''

        '''
        for user_task in user_tasks:
            tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
            tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]

            weighted_score = user_task["grade"]*tasks[user_task["taskid"]].get_grading_weight()
            tasks_score[0] += weighted_score if tasks_data[user_task["taskid"]]["visible"] else 0
        '''
        course_grade = round(tasks_score[0]/tasks_score[1]) if tasks_score[1] > 0 else 0

        '''
        for user_task in user_tasks:
            print(user_task)
            if user_task.get_categories() in bases:
                tasks_data[user_task["taskid"]]["visible"] = user_task.get_accessible_time().after_start() or is_admin
            else:
                for node in tree:
                    if self.is_available(node, tree, courseid):
                        tasks_data[user_task["taskid"]]["visible"] = user_task.get_accessible_time().after_start() or is_admin
                    else:
                        tasks_data[user_task["taskid"]]["visible"] = False
            tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
            tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]
            tasks_score[1] += user_task.get_grading_weight() if tasks_data[user_task["taskid"]]["visible"] else 0
            weighted_score = user_task["grade"]*tasks[user_task["taskid"]].get_grading_weight()
            tasks_score[0] += weighted_score if tasks_data[user_task["taskid"]]["visible"] else 0

        course_grade = round(tasks_score[0]/tasks_score[1]) if tasks_score[1] > 0 else 0
        '''
        #print(tasks_data)
        return {"grade": course_grade, "data": tasks_data}

    def show_page(self, course):
        """ Prepares and shows the course page """
        username = self.user_manager.session_username()
        if not self.user_manager.course_is_open_to_user(course, lti=False):
            return self.template_helper.get_renderer().course_unavailable()
        else:
            tasks = course.get_tasks()
            last_submissions = self.submission_manager.get_user_last_submissions(5, {"courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})

            for submission in last_submissions:
                submission["taskname"] = tasks[submission['taskid']].get_name(self.user_manager.session_language())
            '''
            tasks_data = {}
            user_tasks = self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})
            is_admin = self.user_manager.has_staff_rights_on_course(course, username)

            tasks_score = [0.0, 0.0]

            for taskid, task in tasks.items():
                tasks_data[taskid] = {"visible": task.get_accessible_time().after_start() or is_admin, "succeeded": False,
                                       "grade": 0.0}
                tasks_score[1] += task.get_grading_weight() if tasks_data[taskid]["visible"] else 0

            for user_task in user_tasks:
                tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
                tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]

                weighted_score = user_task["grade"]*tasks[user_task["taskid"]].get_grading_weight()
                tasks_score[0] += weighted_score if tasks_data[user_task["taskid"]]["visible"] else 0

            course_grade = round(tasks_score[0]/tasks_score[1]) if tasks_score[1] > 0 else 0
            '''

            get_tasks_data = self.get_tasks_data(course)
            course_grade = get_tasks_data["grade"]
            tasks_data = get_tasks_data["data"]

            tag_list = course.get_tags()
            user_info = self.database.users.find_one({"username": username})
        return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').course(user_info, course, last_submissions, tasks, tasks_data, course_grade, tag_list)

def course_menu(course, template_helper):
    """ Displays the link to the adaptive view on the course page, if the plugin is activated for this course """
    adaptive = course.get_descriptor().get('adaptive', [])

    if adaptive != []:
        return str(template_helper.get_custom_renderer('frontend/plugins/adaptive', layout=False).course_menu(course))
    else:
        return None

def init(plugin_manager, _, _2, _3):
    """ Init the plugin """
    page_pattern_course = r'/adaptive/([a-z0-9A-Z\-_]+)'
    plugin_manager.add_page(page_pattern_course, AdaptivePage)
    plugin_manager.add_hook('course_menu', course_menu)