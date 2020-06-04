import math

from inginious.frontend.pages.utils import INGIniousAuthPage, INGIniousPage
import web
import webbrowser
from inginious.frontend.plugins.adaptive.Adaptive_course import AdaptivePage

class TestPage(INGIniousAuthPage):

    level_student = 1
    prob_success = {}
    tasks_success = {}
    tasks_level = {}
    number_of_success = [0, 0]

    def GET(self, courseid):

        course = self.get_course(courseid)

        result_test, level_student = self.test_succeeded(course)
        print(level_student)

        if result_test:
            #todo load first task
            AdaptivePage.level_student_global = level_student
            return AdaptivePage().GET(course.get_id(), level_student)

        else:
            #todo : continue test
            return self.show_page(course)

    def test_succeeded(self, course):

        for task in self.tasks_success:
            if task == 0:
                return False

        username = self.user_manager.session_username()
        tasks = course.get_tasks()
        user_tasks = list(self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}}))
        user_tests = [task for task in user_tasks if task["succeeded"]]

        #student_level = self.level_student
        student_level = self.calc_level_student(course, 0, 6)
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
            if success:
                value_min = value_min + math.exp(level)/(math.exp(level)+math.exp(borne_level_min))
                value_max = value_max + math.exp(level)/(math.exp(level)+math.exp(borne_level_max))
                value_mean = value_mean + math.exp(level)/(math.exp(level)+math.exp(borne_level_mean))
            else:
                value_min = value_min - math.exp(borne_level_min)/(math.exp(level)+math.exp(borne_level_min))
                value_max = value_max - math.exp(borne_level_max)/(math.exp(level)+math.exp(borne_level_max))
                value_mean = value_mean - math.exp(borne_level_mean)/(math.exp(level)+math.exp(borne_level_mean))

        if math.pow(value_max-value_mean, 2) < 0.01 or math.pow(value_min-value_mean, 2) < 0.01:
            return borne_level_mean

        if value_min <= 0 <= value_mean or value_mean <= 0 <= value_min:
            return self.calc_level_student(course, borne_level_min, borne_level_mean)
        elif value_mean <= 0 <= value_max or value_max <= 0 <= value_mean:
            return self.calc_level_student(course, borne_level_mean, borne_level_max)
        else:
            if math.fabs(value_max - value_mean) > math.fabs(value_mean - value_min):
                return self.calc_level_student(course, borne_level_min, borne_level_mean)
            else:
                return self.calc_level_student(course, borne_level_mean, borne_level_max)

#######################

# self.number_of_success[1]=0
# for user_task in user_tasks:
#     if "test" in tasks[user_task["taskid"]].get_categories():
#         if user_task["succeeded"]:
#             self.tasks_success[user_task["taskid"]] = 1
#             self.number_of_success[1] += 1
#         elif user_task["tried"] != 0:
#             self.tasks_success[user_task["taskid"]] = -1
#         else:
#             self.tasks_success[user_task["taskid"]] = 0
# #print(self.tasks_success)
#
# if self.number_of_success[0] != self.number_of_success[1]:
#     for taskid, task in tasks.items():
#         if "test" in tasks[taskid].get_categories():
#             for level in tests:
#                 if taskid in level["tasks"]:
#                     self.tasks_level[taskid] = level["level"]
#             #print(self.tasks_level)
#             expo = math.exp(self.level_student[-1]-self.tasks_level[taskid])
#             self.prob_success[taskid] = expo/(1+expo)
#             #print(self.prob_success)
#
#     sum = 0
#     tot = 0
#     #print(user_tasks)
#     for user_task in user_tasks:
#         if "test" in tasks[user_task["taskid"]].get_categories():
#             sum += (self.tasks_success[user_task["taskid"]])*(self.tasks_level[user_task["taskid"]])*(1-self.prob_success[user_task["taskid"]])
#             #print("sum : "+str(sum))
#             tot += self.tasks_level[user_task["taskid"]]*(1-self.prob_success[user_task["taskid"]])
#             #print("tot : "+str(tot))
#     correction = sum/tot
#     #print("correction : " +str(correction))
#     new_level = self.level_student[-1] + correction
#     self.level_student.append(new_level)
#     #print(new_level)
#     #print(self.level_student)
#
#     #print(self.number_of_success[0])
#     #print(self.number_of_success[1])
#     self.number_of_success[0] += self.number_of_success[1]
#     self.number_of_success[1] = 0
#
# #print(self.level_student)
# if len(self.level_student) > 2 and math.pow(self.level_student[-1] - self.level_student[-2],2)<=0.1:
#     #print("if")
#     #print("MSE")
#     #return True
#     return True, round(self.level_student[-1])
# else:
#     if len(user_tasks) >= course.get_descriptor().get('adaptive', [])["minimal_questions"]:
#         #print("if2")
#         # for user_task in user_tasks:
#         #     if "test" in tasks[user_task["taskid"]].get_categories():
#         #         print(user_task)
#         #         if not user_task["succeeded"]:
#         #             return False, round(self.level_student[-1])
#         #print("all_quest")
#         return True, round(self.level_student[-1])
#     else:
#         #print("else")
#         return False, round(self.level_student[-1])

#####################

# def show_page(self, course):
#     """ Prepares and shows the course page """
#     username = self.user_manager.session_username()
#     if not self.user_manager.course_is_open_to_user(course, lti=False):
#         return self.template_helper.get_renderer().course_unavailable()
#     else:
#         ''' '''
#         tasks = course.get_tasks()
#         last_submissions = self.submission_manager.get_user_last_submissions(5, {"courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})
#
#         for submission in last_submissions:
#             submission["taskname"] = tasks[submission['taskid']].get_name(self.user_manager.session_language())
#
#         get_data = self.get_data(course)
#         visible_grade = get_data["visible_grade"]
#         course_grade = get_data["course_grade"]
#         grade = {"visible_grade": visible_grade, "course_grade": course_grade}
#         tasks_data = get_data["data"]
#         #print(tasks_data)
#
#         tree = course.get_descriptor().get('adaptive', [])["tree"]
#         recommendations = self.get_recommendations(course, tree, tasks_data)
#         print(recommendations)
#
#         tag_list = course.get_tags()
#         user_info = self.database.users.find_one({"username": username})
#     #return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').course(user_info, course, last_submissions, tasks, tasks_data, recommendations, grade, tag_list)
#     return "First test for Test page"