from django.shortcuts import render, redirect
from django.views import View
from Application_Classes.App import App

# Create your views here.

a = App()


class BaseView(View):
    def init_logged_in(self, request):
        username = request.session.get("user", "")
        if "user" in request.session and username != "":
            request.session["user"] = username
        else:
            return False


class Home(BaseView):
    def post_response(self, request, user):
        # Get the command if there is one
        command_type = request.POST.get("command", False)
        command_input = request.POST.get("commandStr", False)
        response = ""

        # user exists
        if user is not None:
            if command_type is not False:
                # if the command is logout
                if command_type == 'logout':
                    request.session["user"] = ""
                else:
                    # run any other command
                    if command_input:
                        response = a.command(command_type, command_input)

        # no user, must be logging in
        else:
            if command_type is not False:
                # if the command is to login
                if command_type == 'login':
                    username = request.POST.get('username', '')
                    password = request.POST.get('password', '')

                    # log the user in
                    response = a.command_controller.login(username, password)
                    if response == "Correct login":
                        request.session["user"] = username

        user = a.get_loggedin(request.session.get("user", ""))

        return user, response

    def get(self, request):
        self.init_logged_in(request)

        name = ""
        user = a.get_loggedin(request.session.get("user", ""))
        if user is not None:  # user exists
            name = user['name']

        num_count = a.get_database_count()

        return render(request, "main/index.html", {"navbar": "home", "user": user, "name": name, 'count': num_count})

    def post(self, request):
        self.init_logged_in(request)

        name = ""
        user = a.get_loggedin(request.session.get("user", ""))
        if user is not None:  # user exists
            name = user['name']

        user, response = self.post_response(request, user)  # response tells what is wrong with the login
        num_count = a.get_database_count()

        return render(request, 'main/index.html',
                      {"navbar": "home", "message": response, "user": user, "name": name, 'count': num_count})


class Create(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        name = ""
        user = a.get_loggedin(request.session.get("user", ""))
        if user is not None:
            name = user['name']

        # grabs the type of object the user wishes to create
        create_type = request.GET.get("type", "")

        # return lists of existing objects for dropdown menus
        user_list = None
        course_list = None
        if create_type == 'course':
            # Instructors
            search = {'strict_return': 'role',
                      'string': "instructor"}
            user_list = a.command('search', search)
        elif create_type == 'lab':
            # TAs
            search = {'strict_return': 'role',
                      'string': "ta"}
            user_list = a.command('search', search)
            # Courses
            course_search = {'strict_return': 'all',
                             'string': ""}
            course_list = a.command('searchCourse', course_search)

        return render(request, "main/create.html",
                      {"navbar": "create", "user": user, "name": name, "type": create_type, 'users': user_list,
                       'courses': course_list})

    def post(self, request):
        self.init_logged_in(request)

        name = ""
        response = ""
        user = a.get_loggedin(request.session.get("user", ""))
        current_role = str(user['role'])

        create_type = request.GET.get("type", "")

        # create type user
        if create_type == 'user':
            if user is not None:
                if current_role != "ADMINISTRATOR" and current_role != "SUPERVISOR":
                    response = current_role + " type cannot create"
                else:
                    # grab all the information to create a user from the form
                    name = user['name']
                    user_info = {
                        'data_type': "User",
                        'name': request.POST.get("firstname", "") + " " + request.POST.get("lastname", ""),
                        'username': request.POST.get("username", ""),
                        'password': request.POST.get("password", ""),
                        'role': request.POST.get("role", ""),
                        'email': request.POST.get("email", ""),
                        'phone': request.POST.get("phone", ""),
                        'address': request.POST.get("address", "")
                    }
                    response = a.command('create', user_info)  # create a user

        # create type course
        elif create_type == 'course':
            # grab all the information to create a user from the form
            course_info = {
                'data_type': "Course",
                'course_name': request.POST.get("course_name", ""),
                'course_code': request.POST.get("course_code", ""),
                'course_instructor': a.get_user_object(request.POST.get("course_instructor", ""))
            }
            response = a.command('create', course_info)  # create a course

            # mass create labs if entered
            num_labs = request.POST.get("lab_count", 0)
            for i in range(int(num_labs)):
                lab_info = {
                    'data_type': "Lab",
                    'lab_ta': a.get_user_object("None"),
                    'lab_number': str(100+i),
                    'course_name': a.get_course_object(course_info["course_name"])
                }
                a.command('create', lab_info)  # create a lab

        # create type lab
        elif create_type == 'lab':
            # grab all the information to create a lab from the form
            lab_info = {
                'data_type': "Lab",
                'lab_ta': a.get_user_object(request.POST.get("lab_TA", "")),
                'lab_number': request.POST.get("lab_number", ""),
                'course_name': a.get_course_object(request.POST.get("course_name", ""))
            }
            response = a.command('create', lab_info)  # create a lab

        return render(request, 'main/create.html',
                      {"navbar": "create", "message": response, "user": user, "type": create_type, "name": name})


class Users(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user_name_list = {}
        name = ""
        user = a.get_loggedin(request.session.get("user", ""))

        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)  # gets ?edit from the user to check if the user is editing

        response = ""
        search_string = ""
        lab_list = None
        course_list = None
        user_profile = a.get_user(request.GET.get("user", ""))  # get the username the user wishes to edit

        if user_profile is not None:  # user to edit exists
            # if the profile they are editing are their own, redirect to the account page
            if user_profile['username'] == user['username']:
                return redirect('/account/')

            # split their name into first and last
            user_name = user_profile["name"]
            user_name_list = user_name.split(' ')

            # grab a list of courses that the user teaches
            search = {'strict_return': 'course_instructor',
                      'string': user_profile['username']}
            course_list = a.command('searchCourse', search)

            if course_list.count() == 0:  # no courses, set to None
                course_list = None

            # grab a list of labs that the user TAs for
            search = {'strict_return': 'lab_ta',
                      'string': user_profile['username']}
            lab_list = a.command('searchLab', search)

            if lab_list.count() == 0:  # no labs, set to None
                lab_list = None
        else:
            # the user is not editing. Set the page to searching
            strict_return = request.POST.get("strictReturn", None)
            search_string = request.POST.get("search_string", "")
            if strict_return is None and search_string == "":  # there is no search entry. Return a list of all users
                strict_return = "all"

            search = {'strict_return': strict_return,
                      'string': search_string}
            response = a.command('search', search)  # get list

            if response.count() == 0:  # no search results, set to None
                response = None

        return render(request, "main/users.html",
                      {"navbar": "users", "results": response, "user": user, "name": name, 'search': search_string,
                       "user_profile": user_profile, 'user_profile_name': user_name_list, 'edit': edit,
                       'labs': lab_list, 'courses': course_list})

    def post(self, request):
        self.init_logged_in(request)

        name = ""
        user = a.get_loggedin(request.session.get("user", ""))
        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)

        user_profile = a.get_user(request.GET.get("user", ""))
        search_string = ""
        user_name_list = {}
        lab_list = None
        course_list = None

        # if there is a command, grab it
        command_type = request.POST.get("command", False)
        command_string = request.POST.get("commandStr", "")

        if command_type == 'deleteAccount':  # if there is a command to delete the account
            user_info = {'username': command_string}
            a.command('deleteAccount', user_info)
            return redirect('/users/')  # redirect to the users page to prevent possible errors

        if user_profile is not None:
            # if the profile they are editing are their own, redirect to the account page
            if user_profile['username'] == user['username']:
                return redirect('/account/')

            user_name = user_profile["name"]
            user_name_list = user_name.split(' ')

            # Super complicated code because some reason we thought having one name field was easier
            first = request.POST.get("firstname", "")
            last = request.POST.get("lastname", "")
            # why
            if first == "":
                first = user_name_list[0]
            # why did we do this
            if last == "":
                if len(user_name_list) == 2:
                    last = user_name_list[1]
                else:
                    last = "Undefined"
            # ugh
            user_name = first + ' ' + last

            # just why
            if user_name == " ":
                user_name = user_profile['name']

            # grab the user info from the edit form
            user_info = {
                'name': user_name,
                'username': user_profile['username'],
                'password': request.POST.get("password", ""),  # top notch password security
                'role': request.POST.get("role", ""),
                'email': request.POST.get("email", ""),
                'phone': request.POST.get("phone", ""),
                'address': request.POST.get("address", "")
            }
            response = a.command('editUser', user_info)  # edit this user

            # refresh the information
            user_profile = a.get_user(request.GET.get("user", ""))

            # grab a list of all instructors for the dropdown
            search = {'strict_return': 'course_instructor',
                      'string': user_profile['username']}
            course_list = a.command('searchCourse', search)

            if course_list.count() == 0:  # no results, return None
                course_list = None

            # grab a list of TAs for the dropdown
            search = {'strict_return': 'lab_ta',
                      'string': user_profile['username']}
            lab_list = a.command('searchLab', search)

            if lab_list.count() == 0:  # no results, return None
                lab_list = None

        # user is not editing a user
        else:
            strict_return = request.POST.get("strictReturn", None)
            search_string = request.POST.get("search_string", "")
            if strict_return is None and search_string == "":  # if no search results, return a list of all users
                strict_return = "all"

            search = {'strict_return': strict_return,
                      'string': search_string}
            response = a.command('search', search)

            if response.count() == 0:  # no results, return None
                response = None

        return render(request, 'main/users.html',
                      {"navbar": "users", "results": response, "user": user, "name": name, 'search': search_string,
                       "user_profile": user_profile, 'user_profile_name': user_name_list, 'edit': edit,
                       'labs': lab_list, "courses": course_list})


class Courses(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        name = ""
        user = a.get_loggedin(request.session.get("user", ""))
        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)  # check if ?edit exist to see if the user is editing

        response = ""
        search_string = ""
        lab_list = {}
        course_obj = None
        course = a.get_course(request.GET.get("course", ""))

        search = {'strict_return': 'role',
                  'string': "instructor"}
        user_list = a.command('search', search)

        # course object does not exist
        if course is None:
            strict_return = request.POST.get("strictReturn", None)
            search_string = request.POST.get("search_string", "")
            if strict_return is None and search_string == "":  # no search results, return a list of all courses
                strict_return = "all"

            search = {'strict_return': strict_return,
                      'string': search_string}
            response = a.command('searchCourse', search)

            if response.count() == 0:
                response = None

        # course object exist
        else:
            course_obj = a.get_course_object(request.GET.get("course", ""))  # get the ?course in the url

            search = {'strict_return': 'course',
                      'string': course_obj.course_name}
            lab_list = a.command('searchLab', search)

            if lab_list.count() == 0:
                lab_list = None

        return render(request, "main/courses.html",
                      {"navbar": "courses", "results": response, "user": user, "name": name, 'search': search_string,
                       "course": course, 'course_obj': course_obj, 'edit': edit, 'users': user_list, 'labs': lab_list})

    def post(self, request):
        self.init_logged_in(request)

        name = ""
        user = a.get_loggedin(request.session.get("user", ""))
        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)  # get ?edit from the url to see if they are editing

        course_obj = None
        lab_list = None
        search_string = ""
        command_type = request.POST.get("command", False)  # get the command if there is one
        command_string = request.POST.get("commandStr", "")
        course = a.get_course(request.GET.get("course", ""))  # get the course the user wishes to edit

        # get a list of instructors for the dropdown
        search = {'strict_return': 'role',
                  'string': "instructor"}
        user_list = a.command('search', search)

        if command_type == 'deleteCourse':  # the user wishes to delete the course
            course_info = {'course_name': command_string}
            a.command('deleteCourse', course_info)
            return redirect('/courses/')

        if course is not None:
            # get the course information from the form in order to edit it
            course_info = {
                'course_name': course['course_name'],
                'course_code': request.POST.get("course_code", ""),
                'course_instructor': a.get_user_object(request.POST.get("course_instructor", ""))
            }
            response = a.command('editCourse', course_info)

            # refresh the course object
            course_obj = a.get_course_object(course['course_name'])
            course = a.get_course(course['course_name'])

            # grab a list of labs associated with the course
            search = {'strict_return': 'course',
                      'string': course_obj.course_name}
            lab_list = a.command('searchLab', search)

        # course doesn't exist, do search
        else:
            strict_return = request.POST.get("strictReturn", None)
            search_string = request.POST.get("search_string", "")
            if strict_return is None and search_string == "":  # no search input, return a list
                strict_return = "all"

            search = {'strict_return': strict_return,
                      'string': search_string}
            response = a.command('searchCourse', search)

            if response is not None:
                if response.count() == 0:
                    response = None

        return render(request, 'main/courses.html',
                      {"navbar": "courses", "results": response, "user": user, "name": name, 'search': search_string,
                       "course": course, 'course_obj': course_obj, 'edit': edit, 'users': user_list, 'labs': lab_list})


class Labs(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        name = ""
        lab_obj = None
        user = a.get_loggedin(request.session.get("user", ""))
        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)  # get ?edit from url to see if

        response = ""
        search_string = ""
        lab_number_id = request.GET.get("id", "")  # grab the id of the lab

        # grab a list of TAs
        search = {'strict_return': 'role',
                  'string': "ta"}
        user_list = a.command('search', search)

        # grab a list of courses
        search = {'strict_return': 'all',
                  'string': ""}
        course_list = a.command('searchCourse', search)

        if lab_number_id != "":
            lab_obj = a.get_lab_object(lab_number_id)  # get the lab associated with the id

        else:
            strict_return = request.POST.get("strictReturn", None)
            search_string = request.POST.get("search_string", "")
            if strict_return is None and search_string == "":  # no search results, get all
                strict_return = "all"

            search = {'strict_return': strict_return,
                      'string': search_string}
            response = a.command('searchLab', search)

            if response.count() == 0:
                response = None

        return render(request, "main/labs.html",
                      {"navbar": "labs", "results": response, "user": user, "name": name, 'search': search_string,
                       'lab_obj': lab_obj, 'edit': edit, 'users': user_list, 'courses': course_list})

    def post(self, request):
        self.init_logged_in(request)

        name = ""
        user = a.get_loggedin(request.session.get("user", ""))
        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)  # get the ?edit to see if the user is editing

        lab_obj = None
        response = ""
        search_string = ""
        lab_number_id = request.GET.get("id", "")

        command_type = request.POST.get("command", False)
        command_string = request.POST.get("commandStr", "")

        # grab a list of TAs
        search = {'strict_return': 'role',
                  'string': "ta"}
        user_list = a.command('search', search)

        # grab a list of courses
        search = {'strict_return': 'all',
                  'string': ""}
        course_list = a.command('searchCourse', search)

        if command_type == 'deleteLab':  # if the user wants to delete the lab
            lab_info = {'lab_id': command_string}
            a.command('deleteLab', lab_info)
            return redirect('/labs/')  # redirect to labs to prevent possible errors

        if lab_number_id != "":
            lab_obj = a.get_lab_object(lab_number_id)

            if lab_obj is not None:
                # grab the lab information from the form
                lab_info = {
                    'lab_id': lab_obj.id,
                    'course': a.get_course_object(request.POST.get("course", "")),
                    'lab_number': request.POST.get("lab_number", ""),
                    'lab_ta': a.get_user_object(request.POST.get("lab_ta", ""))
                }
                response = a.command('editLab', lab_info)

                # refresh the lab information
                lab_obj = a.get_lab_object(lab_number_id)

        else:
            # no lab, display a list
            strict_return = request.POST.get("strictReturn", None)
            search_string = request.POST.get("search_string", "")
            if strict_return is None and search_string == "":  # no search, grab all labs
                strict_return = "all"

            search = {'strict_return': strict_return,
                      'string': search_string}
            response = a.command('searchLab', search)
            if response is not None:
                if response.count() == 0:
                    response = None

        return render(request, "main/labs.html",
                      {"navbar": "labs", "results": response, "user": user, "name": name, 'search': search_string,
                       'lab_obj': lab_obj, 'edit': edit, 'users': user_list, 'courses': course_list})


class Account(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        name_list = {}
        lab_list = None
        course_list = None
        name = ""
        edit = request.GET.get("edit", False)
        user = a.get_loggedin(request.session.get("user", ""))

        if user is not None:
            name = user['name']
            name_list = name.split(' ')

            # grab a list of courses that the user instructs
            search = {'strict_return': 'course_instructor',
                      'string': user['username']}
            course_list = a.command('searchCourse', search)

            if course_list.count() == 0:
                course_list = None

            # grab a list of labs that the user is a TA for
            search = {'strict_return': 'lab_ta',
                      'string': user['username']}
            lab_list = a.command('searchLab', search)

            if lab_list.count() == 0:
                lab_list = None

        response = ""
        return render(request, 'main/account.html',
                      {"navbar": "account", "message": response, "user": user, 'edit': edit, 'name_list': name_list,
                       'name': name, 'labs': lab_list, 'courses': course_list})

    def post(self, request):
        self.init_logged_in(request)

        name_list = {}
        course_list = None
        lab_list = None
        name = ""
        response = ""
        edit = request.GET.get("edit", False)
        user = a.get_loggedin(request.session.get("user", ""))

        if user is not None:
            name = user['name']
            name_list = name.split(' ')

            current_role = user['role']

            # oh no here it is again
            first = request.POST.get("firstname", "")
            last = request.POST.get("lastname", "")
            # why didn't we change this
            if first == "":
                first = name_list[0]
            # why oh why
            if last == "":
                if len(name_list) == 2:
                    last = name_list[1]
                else:
                    last = "Undefined"
            name = first + ' ' + last
            # this was a terrible idea
            if name == " ":
                name = user['name']

            # grab a list of the user's information
            user_info = {
                'name': name,
                'username': user['username'],
                'password': request.POST.get("password", ""),
                'role': current_role,
                'email': request.POST.get("email", ""),
                'phone': request.POST.get("phone", ""),
                'address': request.POST.get("address", "")
            }
            response = a.command('editUser', user_info)

            # grab a list of courses
            search = {'strict_return': 'course_instructor',
                      'string': user['username']}
            course_list = a.command('searchCourse', search)

            if course_list.count() == 0:
                course_list = None

            # grab a list of labs
            search = {'strict_return': 'lab_ta',
                      'string': user['username']}
            lab_list = a.command('searchLab', search)

            if lab_list.count() == 0:
                lab_list = None

        # refresh the user object
        user = a.get_loggedin(request.session.get("user", ""))

        return render(request, 'main/account.html',
                      {"navbar": "account", "message": response, "user": user, 'edit': edit, 'name_list': name_list,
                       'name': name, 'labs': lab_list, 'courses': course_list})
