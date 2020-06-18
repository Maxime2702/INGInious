""" Task page """
import json
import mimetypes
import posixpath
import urllib.error
import urllib.parse
import urllib.request
import random
import time
import math

import web
from bson.objectid import ObjectId
from pymongo import ReturnDocument

from inginious.common import exceptions
from inginious.frontend.pages.utils import INGIniousPage

from inginious.frontend.plugins.adaptive import Adaptive_course


class BaseTaskPage(object):
    """ Display a task (and allow to reload old submission/file uploaded during a submission) """

    def __init__(self, calling_page):
        self.cp = calling_page
        self.submission_manager = self.cp.submission_manager
        self.user_manager = self.cp.user_manager
        self.database = self.cp.database
        self.course_factory = self.cp.course_factory
        self.template_helper = self.cp.template_helper
        self.default_allowed_file_extensions = self.cp.default_allowed_file_extensions
        self.default_max_file_size = self.cp.default_max_file_size
        self.webterm_link = self.cp.webterm_link
        self.plugin_manager = self.cp.plugin_manager

    def get_data(self, course, level_student):
        username = self.user_manager.session_username()
        tasks = course.get_tasks()

        user_tasks = list(self.database.user_tasks.find({"username": username, "courseid": course.get_id(), "taskid": {"$in": list(tasks.keys())}}))
        tree = course.get_descriptor().get('adaptive', [])["tree"]
        tasks_data = {}
        is_admin = self.user_manager.has_staff_rights_on_course(course, username)

        tasks_score = [0.0, 0.0, 0.0]

        for taskid, task in tasks.items():
            tasks_data[taskid] = {"visible": False, "succeeded": False,
                                  "grade": 0.0, 'tried': 0, "tasks_parents": []}

        for user_task in user_tasks:
            tasks_data[user_task["taskid"]]["succeeded"] = user_task["succeeded"]
            tasks_data[user_task["taskid"]]["grade"] = user_task["grade"]
            tasks_data[user_task["taskid"]]["tried"] = user_task["tried"]

        for node in tree:
            if self.is_available(node, course, level_student):
                for taskid, task in tasks.items():
                    tags = task.get_categories()
                    if not tags:
                        tasks_data[taskid]["visible"] = False
                    elif node["node"] in tags:
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

    def is_complete(self, node, course):
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
        if grade_total == 0:
            return False
        grade_min = course.get_descriptor().get('adaptive')["grade_min"]
        success_ratio = course.get_descriptor().get('adaptive')["success_ratio"]
        if grade/grade_total > grade_min/100 and succes/len(node_tasks) > success_ratio:
            return True
        return False

    def is_available(self, node, course, level_student):
        parents = node["content"]["parent"]
        if node["level"] <= level_student:
            return True
        else:
            if not parents:
                if node["level"] <= level_student:
                    return True
                else:
                    return False
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

    def get_course(self, courseid):
        """ Return the course """
        try:
            course = self.course_factory.get_course(courseid)
        except:
            raise web.notfound()

        return course

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


    def set_selected_submission(self, course, task, submissionid):
        """ Set submission whose id is `submissionid` to selected grading submission for the given course/task.
            Returns a boolean indicating whether the operation was successful or not.
        """

        submission = self.submission_manager.get_submission(submissionid)

        # Do not continue if submission does not exist or is not owned by current user
        if not submission:
            return False

        # Check if the submission if from this task/course!
        if submission["taskid"] != task.get_id() or submission["courseid"] != course.get_id():
            return False

        is_staff = self.user_manager.has_staff_rights_on_course(course, self.user_manager.session_username())

        # Do not enable submission selection after deadline
        if not task.get_accessible_time().is_open() and not is_staff:
            return False

        # Only allow to set submission if the student must choose their best submission themselves
        if task.get_evaluate() != 'student' and not is_staff:
            return False

        # Check if task is done per group
        if task.is_group_task() and not is_staff:
            group = self.database.groups.find_one({"courseid": task.get_course_id(),
                                                   "students": self.user_manager.session_username()})
            students = group["students"]
        else:
            students = [self.user_manager.session_username()]

        # Check if group/group is the same
        if students == submission["username"]:
            self.database.user_tasks.update_many(
                {"courseid": task.get_course_id(), "taskid": task.get_id(), "username": {"$in": students}},
                {"$set": {"submissionid": submission['_id'],
                          "grade": submission['grade'],
                          "succeeded": submission["result"] == "success"}})
            return True
        else:
            return False

    def GET(self, courseid, taskid, isLTI):
        """ GET request """
        username = self.user_manager.session_username()

        # Fetch the course
        try:
            course = self.course_factory.get_course(courseid)
        except exceptions.CourseNotFoundException as ex:
            raise web.notfound(str(ex))

        if isLTI and not self.user_manager.course_is_user_registered(course):
            self.user_manager.course_register_user(course, force=True)

        if not self.user_manager.course_is_open_to_user(course, username, isLTI):
            return self.template_helper.get_renderer().course_unavailable()

        # Fetch the task
        try:
            tasks = Adaptive_course.tasks_recommended

            if taskid not in tasks.keys():
                tasks = Adaptive_course.tasks_list
            task = tasks[taskid]
        except KeyError:
            raise web.notfound()

        if not self.user_manager.task_is_visible_by_user(task, username, isLTI):
            return self.template_helper.get_renderer().task_unavailable()

        tasks_data = self.get_data(course, Adaptive_course.level_student_global)

        keys = list(tasks.keys())
        index = keys.index(taskid)

        # Compute all possible taskid for next tasks :
        tree = course.get_descriptor().get("adaptive", [])["tree"]

        # if not attempted :
        not_attempted_taskid = list(tasks.keys())[index+1] if index < len(keys)-1 else list(tasks.keys())[0]

        # if success :
        for node in tree:
            if node["node"] in task.get_categories():
                if self.is_complete(node["node"], course):
                    for child in node["content"]["child"]:
                        for node_child in tree:
                            if node_child["node"]==child:
                                if self.is_available(node_child, course, Adaptive_course.level_student_global):
                                    for taskid_child, task_child in Adaptive_course.tasks_list.items():
                                        if child in task_child.get_categories():
                                            Adaptive_course.tasks_recommended.update({taskid_child: task_child})

        tasks = Adaptive_course.tasks_list
        keys = list(tasks.keys())
        index = keys.index(taskid)
        next_taskid = list(tasks.keys())[index+1] if index < len(keys) -1 else None

        # if failed :
        possible_parent = {}
        for node in tree:
            if node["node"] in task.get_categories():
                for parent in node["content"]["parent"]:
                    for taskid_parent, task_parent in Adaptive_course.tasks_list.items():
                        if parent in task_parent.get_categories():
                            possible_parent.update({taskid_parent: task_parent})
                            if not tasks_data["data"][taskid]["succeeded"] and tasks_data["data"][taskid]["tried"]!=0:
                                Adaptive_course.tasks_recommended.update({taskid_parent: task_parent})
        if not possible_parent:
            taskid_previous = None
        else:
            taskid_previous, task_previous = possible_parent.popitem()
        previous_taskid = taskid_previous

        new_value = self.calc_level_student(course, 0, 6)
        if new_value is not None:
            Adaptive_course.level_student_global = new_value
            print(Adaptive_course.level_student_global)
        else:
            pass

        self.user_manager.user_saw_task(username, courseid, taskid)

        is_staff = self.user_manager.has_staff_rights_on_course(course, username)

        userinput = web.input()
        if "submissionid" in userinput and "questionid" in userinput:
            # Download a previously submitted file
            submission = self.submission_manager.get_submission(userinput["submissionid"], user_check=not is_staff)
            if submission is None:
                raise web.notfound()
            sinput = self.submission_manager.get_input_from_submission(submission, True)
            if userinput["questionid"] not in sinput:
                raise web.notfound()

            if isinstance(sinput[userinput["questionid"]], dict):
                # File uploaded previously
                mimetypes.init()
                mime_type = mimetypes.guess_type(urllib.request.pathname2url(sinput[userinput["questionid"]]['filename']))
                web.header('Content-Type', mime_type[0])
                return sinput[userinput["questionid"]]['value']
            else:
                # Other file, download it as text
                web.header('Content-Type', 'text/plain')
                return sinput[userinput["questionid"]]
        else:
            # Generate random inputs and save it into db
            random.seed(str(username if username is not None else "") + taskid + courseid + str(
                time.time() if task.regenerate_input_random() else ""))
            random_input_list = [random.random() for i in range(task.get_number_input_random())]

            user_task = self.database.user_tasks.find_one_and_update(
                {
                    "courseid": task.get_course_id(),
                    "taskid": task.get_id(),
                    "username": self.user_manager.session_username()
                },
                {
                    "$set": {"random": random_input_list}
                },
                return_document=ReturnDocument.AFTER
            )

            submissionid = user_task.get('submissionid', None)
            eval_submission = self.database.submissions.find_one({'_id': ObjectId(submissionid)}) if submissionid else None

            students = [self.user_manager.session_username()]
            if task.is_group_task() and not self.user_manager.has_admin_rights_on_course(course, username):
                group = self.database.groups.find_one({"courseid": task.get_course_id(),
                                                       "students": self.user_manager.session_username()})
                if group is not None:
                    students = group["students"]
                # we don't care for the other case, as the student won't be able to submit.

            submissions = self.submission_manager.get_user_submissions(task) if self.user_manager.session_logged_in() else []
            user_info = self.database.users.find_one({"username": username})

            # Display the task itself
            return self.template_helper.get_custom_renderer('frontend/plugins/adaptive').task_adaptive(user_info, course, task, submissions,
                                                            students, eval_submission, user_task, previous_taskid, not_attempted_taskid, next_taskid, self.webterm_link, random_input_list)

    def POST(self, courseid, taskid, isLTI):
        """ POST a new submission """
        username = self.user_manager.session_username()

        course = self.course_factory.get_course(courseid)
        if not self.user_manager.course_is_open_to_user(course, username, isLTI):
            return self.template_helper.get_renderer().course_unavailable()

        task = course.get_task(taskid)
        if not self.user_manager.task_is_visible_by_user(task, username, isLTI):
            return self.template_helper.get_renderer().task_unavailable()

        self.user_manager.user_saw_task(username, courseid, taskid)

        is_staff = self.user_manager.has_staff_rights_on_course(course, username)
        is_admin = self.user_manager.has_admin_rights_on_course(course, username)

        userinput = web.input()
        if "@action" in userinput and userinput["@action"] == "submit":
            # Verify rights
            if not self.user_manager.task_can_user_submit(task, username, isLTI):
                return json.dumps({"status": "error", "text": _("You are not allowed to submit for this task.")})

            # Retrieve input random and check still valid
            random_input = self.database.user_tasks.find_one({"courseid": task.get_course_id(), "taskid": task.get_id(), "username": username}, { "random": 1 })
            random_input = random_input["random"] if "random" in random_input else []
            for i in range(0, len(random_input)):
                s = "@random_" + str(i)
                if s not in userinput or float(userinput[s]) != random_input[i]:
                    return json.dumps({"status": "error", "text": _("Your task has been regenerated. This current task is outdated.")})

            # Reparse user input with array for multiple choices
            init_var = {
                problem.get_id(): problem.input_type()()
                for problem in task.get_problems() if problem.input_type() in [dict, list]
            }
            userinput = task.adapt_input_for_backend(web.input(**init_var))

            if not task.input_is_consistent(userinput, self.default_allowed_file_extensions, self.default_max_file_size):
                web.header('Content-Type', 'application/json')
                return json.dumps({"status": "error", "text": _("Please answer to all the questions and verify the extensions of the files "
                                                                "you want to upload. Your responses were not tested.")})
            del userinput['@action']

            # Get debug info if the current user is an admin
            debug = is_admin
            if "@debug-mode" in userinput:
                if userinput["@debug-mode"] == "ssh" and debug:
                    debug = "ssh"
                del userinput['@debug-mode']

            # Start the submission
            try:
                submissionid, oldsubids = self.submission_manager.add_job(task, userinput, debug)
                web.header('Content-Type', 'application/json')
                return json.dumps({"status": "ok", "submissionid": str(submissionid), "remove": oldsubids, "text": _("<b>Your submission has been sent...</b>")})
            except Exception as ex:
                web.header('Content-Type', 'application/json')
                return json.dumps({"status": "error", "text": str(ex)})

        elif "@action" in userinput and userinput["@action"] == "check" and "submissionid" in userinput:
            result = self.submission_manager.get_submission(userinput['submissionid'], user_check=not is_staff)
            if result is None:
                web.header('Content-Type', 'application/json')
                return json.dumps({'status': "error", "text": _("Internal error")})
            elif self.submission_manager.is_done(result, user_check=not is_staff):
                web.header('Content-Type', 'application/json')
                result = self.submission_manager.get_input_from_submission(result)
                result = self.submission_manager.get_feedback_from_submission(result, show_everything=is_staff)

                # user_task always exists as we called user_saw_task before
                user_task = self.database.user_tasks.find_one({
                    "courseid":task.get_course_id(),
                    "taskid": task.get_id(),
                    "username": {"$in": result["username"]}
                })

                default_submissionid = user_task.get('submissionid', None)
                if default_submissionid is None:
                    # This should never happen, as user_manager.update_user_stats is called whenever a submission is done.
                    return json.dumps({'status': "error", "text": _("Internal error")})

                return self.submission_to_json(task, result, is_admin, False, default_submissionid == result['_id'], tags=course.get_tags())
            else:
                web.header('Content-Type', 'application/json')
                return self.submission_to_json(task, result, is_admin, False, tags=course.get_tags())

        elif "@action" in userinput and userinput["@action"] == "load_submission_input" and "submissionid" in userinput:
            submission = self.submission_manager.get_submission(userinput["submissionid"], user_check=not is_staff)
            submission = self.submission_manager.get_input_from_submission(submission)
            submission = self.submission_manager.get_feedback_from_submission(submission, show_everything=is_staff)
            if not submission:
                raise web.notfound()
            web.header('Content-Type', 'application/json')

            return self.submission_to_json(task, submission, is_admin, True, tags=course.get_tags())

        elif "@action" in userinput and userinput["@action"] == "kill" and "submissionid" in userinput:
            self.submission_manager.kill_running_submission(userinput["submissionid"])  # ignore return value
            web.header('Content-Type', 'application/json')
            return json.dumps({'status': 'done'})
        elif "@action" in userinput and userinput["@action"] == "set_submission" and "submissionid" in userinput:
            web.header('Content-Type', 'application/json')
            if task.get_evaluate() != 'student':
                return json.dumps({'status': "error"})

            if self.set_selected_submission(course, task, userinput["submissionid"]):
                return json.dumps({'status': 'done'})
            else:
                return json.dumps({'status': 'error'})
        else:
            raise web.notfound()

    def submission_to_json(self, task, data, debug, reloading=False, replace=False, tags=None):
        """ Converts a submission to json (keeps only needed fields) """

        if tags is None:
            tags = []

        if "ssh_host" in data:
            return json.dumps({'status': "waiting", 'text': "<b>SSH server active</b>",
                               'ssh_host': data["ssh_host"], 'ssh_port': data["ssh_port"],
                               'ssh_password': data["ssh_password"]})

        # Here we are waiting. Let's send some useful information.
        waiting_data = self.submission_manager.get_job_queue_info(data["jobid"]) if "jobid" in data else None
        if waiting_data is not None and not reloading:
            nb_tasks_before, approx_wait_time = waiting_data
            wait_time = round(approx_wait_time)
            if nb_tasks_before == -1 and wait_time <= 0:
                text = _("<b>INGInious is currently grading your answers.<b/> (almost done)")
            elif nb_tasks_before == -1:
                text = _("<b>INGInious is currently grading your answers.<b/> (Approx. wait time: {} seconds)").format(
                    wait_time)
            elif nb_tasks_before == 0:
                text = _("<b>You are next in the waiting queue!</b>")
            elif nb_tasks_before == 1:
                text = _("<b>There is one task in front of you in the waiting queue.</b>")
            else:
                text = _("<b>There are {} tasks in front of you in the waiting queue.</b>").format(nb_tasks_before)

            return json.dumps({'status': "waiting", 'text': text})

        tojson = {
            'status': data['status'],
            'result': data.get('result', 'crash'),
            'id': str(data["_id"]),
            'submitted_on': str(data['submitted_on']),
            'grade': str(data.get("grade", 0.0)),
            'replace': replace and not reloading  # Replace the evaluated submission
        }

        if "text" in data:
            tojson["text"] = data["text"]
        if "problems" in data:
            tojson["problems"] = data["problems"]

        if debug:
            tojson["debug"] = self._cut_long_chains(data)

        if tojson['status'] == 'waiting':
            tojson["title"] = _("<b>Your submission has been sent...</b>")
        elif tojson["result"] == "failed":
            tojson["title"] = _("There are some errors in your answer. Your score is {score}%.").format(score=data["grade"])
        elif tojson["result"] == "success":
            tojson["title"] = _("Your answer passed the tests! Your score is {score}%.").format(score=data["grade"])
        elif tojson["result"] == "timeout":
            tojson["title"] = _("Your submission timed out. Your score is {score}%.").format(score=data["grade"])
        elif tojson["result"] == "overflow":
            tojson["title"] = _("Your submission made an overflow. Your score is {score}%.").format(score=data["grade"])
        elif tojson["result"] == "killed":
            tojson["title"] = _("Your submission was killed.")
        else:
            tojson["title"] = _("An internal error occurred. Please retry later. "
                                "If the error persists, send an email to the course administrator.")

        tojson["title"] += " " + _("[Submission #{submissionid}]").format(submissionid=data["_id"])
        tojson["title"] = self.plugin_manager.call_hook_recursive("feedback_title", task=task, submission=data, title=tojson["title"])["title"]

        tojson["text"] = data.get("text", "")
        tojson["text"] = self.plugin_manager.call_hook_recursive("feedback_text", task=task, submission=data, text=tojson["text"])["text"]

        if reloading:
            # Set status='ok' because we are reloading an old submission.
            tojson["status"] = 'ok'
            # And also include input
            tojson["input"] = data.get('input', {})

        if "tests" in data:
            tojson["tests"] = {}
            for key, tag in tags.items():  # Tags only visible for admins should not appear in the json for students.
                if tag.get_type() in [0, 1] and (tag.is_visible_for_student() or debug) and key in data["tests"]:
                    tojson["tests"][key] = data["tests"][key]
            if debug: #We add also auto tags when we are admin
                for tag in data["tests"]:
                    if tag.startswith("*auto-tag-"):
                        tojson["tests"][tag] = data["tests"][tag]

        # allow plugins to insert javascript to be run in the browser after the submission is loaded
        tojson["feedback_script"] = "".join(self.plugin_manager.call_hook("feedback_script", task=task, submission=data))

        return json.dumps(tojson, default=str)

    def _cut_long_chains(self, data, limit=1000):
        """ Cut all strings and byte chains in a dictionary
            if they exceed a limit in characters or bytes """

        if isinstance(data, dict):
            new_data = {}
            for key, value in data.items():
                if isinstance(value, bytes) and len(value) > limit:
                    new_data[key] = value[:limit] + _(" <truncated>").encode("utf-8")
                elif isinstance(value, str) and len(value) > limit:
                    new_data[key] = value[:limit] + _(" <truncated>")
                elif isinstance(value, dict):
                    new_data[key] = self._cut_long_chains(value)
                else:
                    new_data[key] = value
            return new_data
        return data


class TaskPageStaticDownload(INGIniousPage):
    """ Allow to download files stored in the task folder """

    def is_lti_page(self):
        # authorize LTI sessions to download static files
        return True

    def GET(self, courseid, taskid, path):  # pylint: disable=arguments-differ
        """ GET request """
        try:
            course = self.course_factory.get_course(courseid)
            if not self.user_manager.course_is_open_to_user(course):
                return self.template_helper.get_renderer().course_unavailable()

            path_norm = posixpath.normpath(urllib.parse.unquote(path))

            if taskid == "$common":
                public_folder = course.get_fs().from_subfolder("$common").from_subfolder("public")
            else:

                task = course.get_task(taskid)
                if not self.user_manager.task_is_visible_by_user(task):  # ignore LTI check here
                    return self.template_helper.get_renderer().task_unavailable()

                public_folder = task.get_fs().from_subfolder("public")
            (method, mimetype_or_none, file_or_url) = public_folder.distribute(path_norm, False)

            if method == "local":
                web.header('Content-Type', mimetype_or_none)
                return file_or_url
            elif method == "url":
                raise web.redirect(file_or_url)
            else:
                raise web.notfound()
        except web.HTTPError as error_or_redirect:
            raise error_or_redirect
        except:
            if web.config.debug:
                raise
            else:
                raise web.notfound()


class TaskAdaptivePage(INGIniousPage):
    def GET(self, courseid, taskid):
        return BaseTaskPage(self).GET(courseid, taskid, False)

    def POST(self, courseid, taskid):
        return BaseTaskPage(self).POST(courseid, taskid, False)
