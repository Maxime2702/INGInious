import math

from inginious.frontend.pages.utils import INGIniousAuthPage, INGIniousPage
import web
from inginious.frontend.plugins.adaptive.Adaptive_course import AdaptivePage

class TestPage(INGIniousAuthPage):

    level_student = 1
    prob_success = {}
    tasks_success = {}
    tasks_level = {}
    number_of_success = [0, 0]

    def GET(self, courseid):

        course = self.get_course(courseid)

        result_test, level_student = self.test_finished(course)

        if result_test:
            AdaptivePage.level_student_global = level_student
            return AdaptivePage().GET(course.get_id(), level_student)

        else:
            return self.show_page(course)

    def test_finished(self, course):
        """Check if the test has been finished by a student"""

        for task in self.tasks_success:
            if task == 0:
                return False

        username = self.user_manager.session_username()
        tasks = course.get_tasks()
        user_tasks = list(self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}}))
        user_tests = [task for task in user_tasks if task["succeeded"]]

        student_level = self.calc_level_student(course, 0, course.get_descriptor().get('adaptive', [])["level_max"])
        self.level_student = student_level
        if len(user_tests) >= course.get_descriptor().get('adaptive', [])["minimal_questions"]:
            return True, student_level
        else:
            return False, student_level

    def get_course(self, courseid):
        """ Return the course """
        try:
            course = self.course_factory.get_course(courseid)
        except:
            raise web.notfound()

        return course

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

            tasks_data = {}
            user_tasks = self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})
            is_admin = self.user_manager.has_staff_rights_on_course(course, username)

            tasks_score = [0.0, 0.0]

            for taskid, task in tasks.items():
                tasks_data[taskid] = {"visible": task.get_accessible_time().after_start() or is_admin, "succeeded": False,
                                      "grade": 0.0}
                if "test" not in task.get_categories():
                    tasks_data[taskid] = {"visible": False}
                tasks_score[1] += task.get_grading_weight() if tasks_data[taskid]["visible"] else 0

            for user_task in user_tasks:
                tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
                tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]

                weighted_score = user_task["grade"]*tasks[user_task["taskid"]].get_grading_weight()
                tasks_score[0] += weighted_score if tasks_data[user_task["taskid"]]["visible"] else 0

            course_grade = round(tasks_score[0]/tasks_score[1]) if tasks_score[1] > 0 else 0
            tag_list = course.get_tags()
            user_info = self.database.users.find_one({"username": username})

            return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').course_test(user_info, course, last_submissions, tasks, tasks_data, course_grade, tag_list)

    def calc_level_student(self, course, borne_level_min, borne_level_max):
        """estimate the level of a student"""

        username = self.user_manager.session_username()
        tasks = course.get_tasks()
        user_tasks = self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})
        tree = course.get_descriptor().get('adaptive', [])["tree"]

        level_tasks = {}
        successes_tasks = {}

        for user_task in user_tasks:
            for node in tree:
                if node["node"] in course.get_task(user_task["taskid"]).get_categories():
                    level_tasks.update({user_task["taskid"]: node["level"]})
                    if user_task["succeeded"]:
                        successes_tasks.update({user_task["taskid"]: 1})
                    elif user_task["tried"] > 0:
                        successes_tasks.update({user_task["taskid"]: -1})
                    else:
                        successes_tasks.update({user_task["taskid"]: 0})

        borne_level_mean = (borne_level_max + borne_level_min)/2.0

        value_min = 0
        value_max = 0
        value_mean = 0
        for taskid, success in successes_tasks.items():
            level = level_tasks[taskid]
            if success == 1:
                value_min = value_min + math.exp(level)/(math.exp(level)+math.exp(borne_level_min))
                value_max = value_max + math.exp(level)/(math.exp(level)+math.exp(borne_level_max))
                value_mean = value_mean + math.exp(level)/(math.exp(level)+math.exp(borne_level_mean))
            elif success == -1:
                value_min = value_min - math.exp(borne_level_min)/(math.exp(level)+math.exp(borne_level_min))
                value_max = value_max - math.exp(borne_level_max)/(math.exp(level)+math.exp(borne_level_max))
                value_mean = value_mean - math.exp(borne_level_mean)/(math.exp(level)+math.exp(borne_level_mean))

        if borne_level_mean - borne_level_min < 1 and borne_level_max - borne_level_mean < 1:
            return round(borne_level_mean)

        if value_min <= 0 <= value_mean or value_mean <= 0 <= value_min:
            return self.calc_level_student(course, borne_level_min, borne_level_mean)
        elif value_mean <= 0 <= value_max or value_max <= 0 <= value_mean:
            return self.calc_level_student(course, borne_level_mean, borne_level_max)
        else:
            if value_max < value_min < 0 or 0 > value_min > value_max:
                return self.calc_level_student(course, borne_level_min, borne_level_mean)
            else:
                return self.calc_level_student(course, borne_level_mean, borne_level_max)