import math

from inginious.frontend.pages.utils import INGIniousAuthPage, INGIniousPage
import web
import webbrowser
from inginious.frontend.plugins.adaptive.Adaptive_course import AdaptivePage

class TestPage(INGIniousAuthPage):

    level_student = [2];
    prob_success = {}
    tasks_success = {}
    tasks_level = {}
    number_of_success = [0, 0]


    def GET(self, courseid):

        '''
        test ici if Test succedeed or not
        '''

        course = self.get_course(courseid)

        if self.test_succeeded(course):
            #todo show course view
            #return self.show_page(course)
            return AdaptivePage.show_page(AdaptivePage(), course, self.level_student)
            #url = 'http://localhost:8080/adaptive/'+courseid
            #webbrowser.open(url, new=2)
            #return "success"+str(self.level_student)
        else:
            #todo : continue test
            #return "Test failed"+str(self.level_student)
            return self.show_page(course)
            #return "failed"

    def test_succeeded(self, course):
        #todo : calculate new level of student
        #todo : Mean square error entre level student
        #todo : only if new tasks tried, sinon, ça recalcule à chaque refresh

        for task in self.tasks_success:
            if task == 0:
                return False


        username = self.user_manager.session_username()
        tasks = course.get_tasks()
        user_tasks = list(self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}}))

        tests = course.get_descriptor().get('adaptive', [])["test"]

        self.number_of_success[1]=0
        for user_task in user_tasks:
            if "test" in tasks[user_task["taskid"]].get_categories():
                if user_task["succeeded"]:
                    self.tasks_success[user_task["taskid"]] = 1
                    self.number_of_success[1] += 1
                elif user_task["tried"] != 0:
                    self.tasks_success[user_task["taskid"]] = -1
                else:
                    self.tasks_success[user_task["taskid"]] = 0
        print(self.tasks_success)

        if self.number_of_success[0] != self.number_of_success[1]:
            for taskid, task in tasks.items():
                if "test" in tasks[taskid].get_categories():
                    for level in tests:
                        if taskid in level["tasks"]:
                            self.tasks_level[taskid] = level["level"]
                    #print(self.tasks_level)
                    expo = math.exp(self.level_student[-1]-self.tasks_level[taskid])
                    self.prob_success[taskid] = expo/(1+expo)
                    #print(self.prob_success)

            sum = 0
            tot = 0
            #print(user_tasks)
            for user_task in user_tasks:
                if "test" in tasks[user_task["taskid"]].get_categories():
                    sum += (self.tasks_success[user_task["taskid"]])*(self.tasks_level[user_task["taskid"]])*(1-self.prob_success[user_task["taskid"]])
                    print("sum : "+str(sum))
                    tot += self.tasks_level[user_task["taskid"]]*(1-self.prob_success[user_task["taskid"]])
                    print("tot : "+str(tot))
            correction = sum/tot
            print("correction : " +str(correction))
            new_level = self.level_student[-1] + correction
            self.level_student.append(new_level)
            #print(new_level)
            #print(self.level_student)

            self.number_of_success[0] += self.number_of_success[1]
            self.number_of_success[1] = 0

        if len(self.level_student) > 2 and math.pow(self.level_student[-1] - self.level_student[-2],2)<=0.1:
            print("MSE")
            #return True
            return True, round(self.level_student[-1])
        else:
            if len(user_tasks) >= course.get_descriptor().get('adaptive', [])["minimal_questions"]:
                for user_task in user_tasks:
                    if "test" in tasks[user_task["taskid"]].get_categories():
                        print(user_task)
                        if not user_task["succeeded"]:
                            return False, round(self.level_student[-1])
                print("all_quest")
                return True, round(self.level_student[-1])
            else:
                return False, round(self.level_student[-1])

    def get_course(self, courseid):
        """ Return the course """
        try:
            course = self.course_factory.get_course(courseid)
        except:
            raise web.notfound()

        return course


    '''
    def show_page(self, course):
        """ Prepares and shows the course page """
        username = self.user_manager.session_username()
        if not self.user_manager.course_is_open_to_user(course, lti=False):
            return self.template_helper.get_renderer().course_unavailable()
        else:
            ''' '''
            tasks = course.get_tasks()
            last_submissions = self.submission_manager.get_user_last_submissions(5, {"courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})

            for submission in last_submissions:
                submission["taskname"] = tasks[submission['taskid']].get_name(self.user_manager.session_language())

            get_data = self.get_data(course)
            visible_grade = get_data["visible_grade"]
            course_grade = get_data["course_grade"]
            grade = {"visible_grade": visible_grade, "course_grade": course_grade}
            tasks_data = get_data["data"]
            #print(tasks_data)

            tree = course.get_descriptor().get('adaptive', [])["tree"]
            recommendations = self.get_recommendations(course, tree, tasks_data)
            print(recommendations)

            tag_list = course.get_tags()
            user_info = self.database.users.find_one({"username": username})
        ''' '''
            #return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').course(user_info, course, last_submissions, tasks, tasks_data, recommendations, grade, tag_list)
            return "First test for Test page"
            '''

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

            return self.template_helper.get_renderer().course(user_info, course, last_submissions, tasks, tasks_data, course_grade, tag_list)


        '''
        Page de Test same as page the course. Si page de Test complètement réussie, débloque la page normale de l'adaptive view
        
        les tests à faire passer sont des tâches autres mais qui reprennet les concepts du cours. Peuvent être same que celle du cours actuels
        
        tester si le user a des tries pour une task
        
        définir un tag pour les tasks de tests. Suffit de tester si ces tasks sont tries/succeeded
        
        init.py hook_manager : different actions en fonction de Test or not.
        '''