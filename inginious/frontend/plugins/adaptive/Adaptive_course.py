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
        for parent in parents:
            if not self.is_complete(parent, course):
                return False
        return True

    def sort_tasks(self, category, tasks):
        tasks_sorted = tasks.copy()
        for taskid, task in tasks.items():
            if category not in task.get_categories():
                tasks_sorted.pop(taskid)
        return tasks_sorted

    def sort_user_tasks(self, skill_tasks, user_tasks):
        tasks_id = []
        for task in skill_tasks:
            tasks_id.append(task)
        correct_tasks = []
        for user_task in user_tasks:
            if user_task["taskid"] in tasks_id:
                correct_tasks.append(user_task)
        return correct_tasks

    def is_complete(self, node, course):
        username = self.user_manager.session_username()
        tasks = course.get_tasks()
        user_tasks = self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})
        tasks = self.sort_tasks(node, tasks)
        user_tasks = self.sort_user_tasks(tasks, user_tasks)
        if len(tasks) != len(user_tasks):
            return False
        else:
            for user_task in user_tasks:
                if not user_task["succeeded"]:
                    return False
            return True

    def get_data(self, course):
        username = self.user_manager.session_username()
        tasks = course.get_tasks()
        user_tasks = list(self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}}))
        tree = course.get_descriptor().get('adaptive', [])["tree"]
        bases = list(course.get_descriptor().get('adaptive', [])["bases"])
        tasks_data = {}
        is_admin = self.user_manager.has_staff_rights_on_course(course, username)

        tasks_score = [0.0, 0.0, 0.0]

        for taskid, task in tasks.items():
            tasks_data[taskid] = {"visible": set(task.get_categories()).issubset(set(bases)), "succeeded": False,
                                  "grade": 0.0, 'tried': 0, "tasks_parents": []}

        for user_task in user_tasks:
            tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
            tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]
            tasks_data[user_task["taskid"]]["tried"] = user_task["tried"]

        for node in tree:
            if self.is_available(node, course):
                for taskid, task in tasks.items():
                    tags = task.get_categories()
                    if node["node"] in tags:
                        tasks_data[taskid]["visible"] = task.get_accessible_time().after_start() or is_admin
                        for parent in node["content"]["parent"]:
                            for task_p_id, task_p in tasks.items():
                                tags_p = task_p.get_categories()
                                if parent in tags_p:
                                    tasks_data[taskid]["tasks_parents"].append(task_p_id)

        for data_id, data in tasks_data.items():
            weighted_score = data["grade"]*tasks[data_id].get_grading_weight()
            tasks_score[0] += weighted_score if data["visible"] else 0
            tasks_score[1] += tasks[data_id].get_grading_weight() if data["visible"] else 0
            tasks_score[2] += tasks[data_id].get_grading_weight() if tasks[data_id].get_accessible_time().after_start() else 0
        visible_grade = round(tasks_score[0]/tasks_score[1]) if tasks_score[1] > 0 else 0
        course_grade = round(tasks_score[0]/tasks_score[2]) if tasks_score[2] > 0 else 0
        return {"visible_grade": visible_grade, "course_grade": course_grade, "data": tasks_data}

    def get_recommendations(self, course, tree, tasks_data):
        recommendations = {'high': {}, 'medium': {}, 'low': {}}
        for taskid, task in tasks_data.items():
            if task["visible"] and task["tried"] == 0:
                recommendations["low"].update({taskid: task})
            elif task["visible"] and not task["succeeded"]:
                recommendations["medium"].update({taskid: task})
                for task_p_id in task["tasks_parents"]:
                    recommendations["high"].update({task_p_id: tasks_data[task_p_id]})

        return recommendations

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
        return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').course(user_info, course, last_submissions, tasks, tasks_data, recommendations, grade, tag_list)
