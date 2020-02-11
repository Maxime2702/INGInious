from inginious.frontend.pages.utils import INGIniousAuthPage, INGIniousPage
import web

class TestPage(INGIniousAuthPage):

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

    def show_page(self, course):
        """ Prepares and shows the course page """
        username = self.user_manager.session_username()
        if not self.user_manager.course_is_open_to_user(course, lti=False):
            return self.template_helper.get_renderer().course_unavailable()
        else:
            '''
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
        '''
            #return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').course(user_info, course, last_submissions, tasks, tasks_data, recommendations, grade, tag_list)
            return "First test for Test page"



        '''
        Page de Test same as page the course. Si page de Test complètement réussie, débloque la page normale de l'adaptive view
        
        les tests à faire passer sont des tâches autres mais qui reprennet les concepts du cours. Peuvent être same que celle du cours actuels
        
        tester si le user a des tries pour une task
        
        définir un tag pour les tasks de tests. Suffit de tester si ces tasks sont tries/succeeded
        
        init.py hook_manager : different actions en fonction de Test or not.
        '''