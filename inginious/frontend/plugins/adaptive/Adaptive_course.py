from inginious.frontend.pages.utils import INGIniousAuthPage, INGIniousPage
import web
from collections import OrderedDict
from collections import deque

class OrderedDictInsert(OrderedDict):
    def insert(self, index, key, value):
        self[key] = value
        for ii, k in enumerate(list(self.keys())):
            if ii >= index and k != key:
                self.move_to_end(k)


#tasks_recommended = OrderedDictInsert()
tasks_recommended = OrderedDict()
tasks_recommendations = OrderedDict()
tasks_list = OrderedDict()
level_student = 1

class AdaptivePage(INGIniousAuthPage):


    '''def GET(self, courseid):
        course = self.get_course(courseid)
        return self.show_page(course)'''

    def GET(self, courseid,student_level=2):
        course = self.get_course(courseid)
        return self.show_page2(course,student_level)

    def POST(self, courseid,student_level=2):
        course = self.get_course(courseid)
        level_student = student_level
        return self.show_page2(course,student_level)

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

    def is_available2(self, node, course, level_student):
        parents = node["content"]["parent"]
        if node["level"] <= level_student:
            #print(str(node["node"]) + " <= level")
            return True
        else:
            # if not parents:
            #     return True
            if not parents:
                if node["level"] <= level_student:
                    return True
                else:
                    return False
            for parent in parents:
                #if not self.is_complete(parent, course):
                if not self.is_complete2(parent, course):
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

    def is_complete2(self, node, course):
        username = self.user_manager.session_username()
        tasks = course.get_tasks()
        node_tasks = {}
        for taskid, task in tasks.items():
            if node in task.get_categories():
                node_tasks[taskid] = task
        user_tasks = list(self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}}))
        node_user = [task for task in user_tasks if task["taskid"] in node_tasks.keys()]
        succes = 0
        grade = 0
        grade_total = 0
        for user_task in node_user:
            if user_task["succeeded"]:
                succes += 1
            grade += user_task["grade"]
        for task in node_tasks.values():
            grade_total += task.get_grading_weight()
        grade_total = grade_total*100
        # print("node : "+node)
        # print("success : "+str(succes))
        # print("tot : "+str(len(node_tasks)))
        # print("grade : "+str(grade))
        # print("grade_total : "+str(grade_total))
        if grade/grade_total > 0.5 and succes/len(node_tasks) > 0.5:
            # print(node + " available")
            return True
        #print(node + " not")
        return False
        #return True


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
            tasks_score[2] += tasks[data_id].get_grading_weight() if tasks[data_id].get_accessible_time().after_start() and "test" not in tasks[data_id].get_categories() else 0
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

        if not tasks_recommendations:
            for priority, tasks in recommendations.items():
                for taskid, task in tasks.items():
                    tasks_recommendations.update({taskid: course.get_tasks()[taskid]})

        if not tasks_recommendations:
            for taskid, task in course.get_tasks().items():
                if 'test' not in task.get_categories():
                    tasks_recommendations.update({taskid: course.get_tasks()[taskid]})
        print(tasks_recommendations.keys())

        recoms_ordered = self.get_recommendations_ordered(course, tasks_recommendations)
        for taskid, task in recoms_ordered.items():
            tasks_recommended.update({taskid: task})

        print(tasks_recommended.keys())
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

            tree = course.get_descriptor().get('adaptive', [])["tree"]
            recommendations = self.get_recommendations(course, tree, tasks_data)

            tag_list = course.get_tags()
            user_info = self.database.users.find_one({"username": username})
        return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').course(user_info, course, last_submissions, tasks, tasks_data, recommendations, grade, tag_list, tree)

    def show_page2(self, course, level_student):
        """ Prepares and shows the course page """

        username = self.user_manager.session_username()
        tree = course.get_descriptor().get('adaptive', [])["tree"]
        if not self.user_manager.course_is_open_to_user(course, lti=False):
            return self.template_helper.get_renderer().course_unavailable()
        else:
            tasks = course.get_tasks()
            last_submissions = self.submission_manager.get_user_last_submissions(5, {"courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}})

            for submission in last_submissions:
                submission["taskname"] = tasks[submission['taskid']].get_name(self.user_manager.session_language())

            get_data = self.get_data2(course, level_student)
            visible_grade = get_data["visible_grade"]
            course_grade = get_data["course_grade"]
            grade = {"visible_grade": visible_grade, "course_grade": course_grade}
            tasks_data = get_data["data"]

            tree = course.get_descriptor().get('adaptive', [])["tree"]
            recommendations = self.get_recommendations(course, tree, tasks_data)

            tag_list = course.get_tags()
            user_info = self.database.users.find_one({"username": username})

            tasks_ordered = self.get_tasks_ordered(course)
            if not tasks_list:
                for taskid, task in tasks_ordered.items():
                    tasks_list.update({taskid: task})

        return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').course(user_info, course, last_submissions, tasks, tasks_data, recommendations, grade, tag_list, tree)

    def get_data2(self, course, level_student):
        username = self.user_manager.session_username()
        tasks = course.get_tasks()

        user_tasks = list(self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}}))
        tree = course.get_descriptor().get('adaptive', [])["tree"]
        bases = list(course.get_descriptor().get('adaptive', [])["bases"])
        tasks_data = {}
        is_admin = self.user_manager.has_staff_rights_on_course(course, username)

        tasks_score = [0.0, 0.0, 0.0]

        for taskid, task in tasks.items():
            #tasks_data[taskid] = {"visible": set(task.get_categories()).issubset(set(bases)), "succeeded": False,
            #                      "grade": 0.0, 'tried': 0, "tasks_parents": []}
            tasks_data[taskid] = {"visible": False, "succeeded": False,
                                  "grade": 0.0, 'tried': 0, "tasks_parents": []}

        for user_task in user_tasks:
            tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
            tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]
            tasks_data[user_task["taskid"]]["tried"] = user_task["tried"]

        for node in tree:
            if self.is_available2(node, course, level_student):
                #print(str(node["node"])+" available")
                for taskid, task in tasks.items():
                    tags = task.get_categories()
                    if not tags:
                        tasks_data[taskid]["visible"] = False
                    elif node["node"] in tags:
                        #if node["level"] <= level_student:
                        #    tasks_data[taskid]["succeeded"] = True
                        tasks_data[taskid]["visible"] = task.get_accessible_time().after_start() or is_admin

                        #print(tasks_data[taskid]["visible"])
                        for parent in node["content"]["parent"]:
                            for task_p_id, task_p in tasks.items():
                                tags_p = task_p.get_categories()
                                if parent in tags_p:
                                    tasks_data[taskid]["tasks_parents"].append(task_p_id)

        for data_id, data in tasks_data.items():
            weighted_score = data["grade"]*tasks[data_id].get_grading_weight()
            tasks_score[0] += weighted_score if data["visible"] else 0
            tasks_score[1] += tasks[data_id].get_grading_weight() if data["visible"] else 0
            tasks_score[2] += tasks[data_id].get_grading_weight() if tasks[data_id].get_accessible_time().after_start() and "test" not in tasks[data_id].get_categories() else 0
        visible_grade = round(tasks_score[0]/tasks_score[1]) if tasks_score[1] > 0 else 0
        course_grade = round(tasks_score[0]/tasks_score[2]) if tasks_score[2] > 0 else 0
        return {"visible_grade": visible_grade, "course_grade": course_grade, "data": tasks_data}

    def get_skills_ordered(self, course):
        username = self.user_manager.session_username()
        tasks = course.get_tasks()

        tree = course.get_descriptor().get('adaptive', [])["tree"]
        level_max = course.get_descriptor().get('adaptive', [])["level_max"]
        bases = list(course.get_descriptor().get('adaptive', [])["bases"])

        skills_ordered = []
        bag = [deque() for level in range(level_max)]
        discovered = []
        for base in bases:
            for node in tree:
                if node["node"] == base:
                    bag[node["level"]-1].append(base)
                    discovered.append(base)

        for level in range(1, level_max+1):
            while len(bag[level-1]) > 0:
                node = bag[level-1].popleft()
                skills_ordered.append(node)
                for leaf in tree:
                    if leaf["node"] == node:
                        for child in leaf["content"]["child"]:
                            if child not in discovered:
                                for child_leaf in tree:
                                    if child_leaf["node"] == child:
                                        bag[child_leaf["level"]-1].append(child)
                                        discovered.append(child)
        return skills_ordered

    def get_tasks_ordered(self, course):
        skills_ordered = self.get_skills_ordered(course)
        tasks = course.get_tasks()

        tasks_ordered = {}
        for skill in skills_ordered:
            for taskid, task in tasks.items():
                if skill in task.get_categories():
                    tasks_ordered.update({taskid: task})
        #print(tasks_ordered)
        return tasks_ordered

    def get_recommendations_ordered(self, course, recoms):
        skills_ordered = self.get_skills_ordered(course)

        recoms_ordered = {}
        for skill in skills_ordered:
            for taskid, task in recoms.items():
                if skill in task.get_categories():
                    recoms_ordered.update({taskid: task})
        #print(tasks_ordered)
        return recoms_ordered
