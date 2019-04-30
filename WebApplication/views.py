from django.shortcuts import render, redirect
from django.views import View
from Application_Classes.App import App

# Create your views here.

a = App()


class BaseView(View):
    def init_logged_in(self, request):
        username = request.session.get("user", "")
        if "user" in request.session and username != "":
            print("logged in: " + username)
            request.session["user"] = username
        else:
            print("no session")
            return False

    def post_response(self, request, user):
        command_type = request.POST.get("command", False)
        command_input = request.POST.get("commandStr", False)
        response = ""
        print(command_type)
        print(command_input)
        if user is not None:
            if command_type is not False:
                if command_type == 'logout':
                    request.session["user"] = ""
                else:
                    if command_input:
                        response = a.command(command_input)
        else:
            if command_type is not False:
                if command_type == 'login':
                    username = request.POST.get('username', '')
                    password = request.POST.get('password', '')

                    res = a.command_controller.login(username, password)
                    print(res)
                    if res:
                        print("log in")
                        request.session["user"] = username
                    else:
                        response = "Incorrect login"

        user = a.get_loggedin(request.session.get("user", ""))
        return user, response


class Home(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            print(user)
            name = user['name']

        return render(request, "main/index.html", {"navbar": "home", "user": user, "name": name})

    def post(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            name = user['name']
        else:
            print("no user")

        user, response = self.post_response(request, user)

        print(user)

        return render(request, 'main/index.html', {"navbar": "home", "message": response, "user": user, "name": name})


class Create(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            name = user['name']

        create_type = request.GET.get("type", "")

        user_list = None
        course_list = None
        if create_type == 'course':
            search = {'strict_return': 'role',
                      'string': "instructor"}
            user_list = a.command('search', search)
        elif create_type == 'lab':
            search = {'strict_return': 'role',
                      'string': "ta"}
            user_list = a.command('search', search)

        return render(request, "main/create.html",
                      {"navbar": "create", "user": user, "name": name, "type": create_type, 'users': user_list})

    def post(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        response = ""
        current_role = str(user['role'])

        create_type = request.GET.get("type", "")

        if create_type == 'user':
            if user is not None:
                if current_role is not "ADMINISTRATOR" and current_role != "SUPERVISOR":
                    response = current_role + " type cannot create"
                else:
                    name = user['name']
                    userInfo = {
                        'data_type': "user",
                        'name': request.POST.get("firstname", "") + " " + request.POST.get("lastname", ""),
                        'username': request.POST.get("username", ""),
                        'password': request.POST.get("password", ""),
                        'user_type': request.POST.get("usertype", "").upper(),
                        'email': request.POST.get("email", ""),
                        'phone': request.POST.get("phone", ""),
                        'address': request.POST.get("address", "")
                    }
                    # Used to check when inside the page
                    # print("Inside create User")
                    response = a.command('create', userInfo)

        elif create_type == 'course':
            courseInfo = {
                'course_name': request.POST["course_name"],
                'course_code': request.POST["course_code"],
                #            'course_instructor': request.POST["course_instructor"]
            }
            # Used to check when inside the page
            # print("Inside create course")
            response = a.command('createCourse', courseInfo)

        elif create_type == 'lab':
            labInfo = {
                #                'lab_tas': request.POST["lab_tas"],
                'lab_number': request.POST["lab_number"],
                #                'course': request.POST["course"]
            }
            # Used to check when inside the page`
            # print("Inside create lab section")
            response = a.command('createLabSection', labInfo)

        return render(request, 'main/create.html',
                      {"navbar": "create", "message": response, "user": user, "type": create_type, "name": name})


class Users(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        user_name_list = {}
        name = ""
        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)

        response = ""
        user_profile = a.get_user(request.GET.get("user", ""))
        search_string = ""

        if user_profile is not None:
            if user_profile['username'] == user['username']:
                return redirect('/account/')

            user_name = user_profile["name"]
            user_name_list = user_name.split(' ')
        else:
            strict_return = request.POST.get("strictReturn", None)
            search_string = request.POST.get("search_string", "")
            if strict_return is None and search_string == "":
                strict_return = "all"

            search = {'strict_return': strict_return,
                      'string': search_string}
            response = a.command('search', search)
            if response.count() == 0:
                response = None

        return render(request, "main/users.html",
                      {"navbar": "users", "results": response, "user": user, "name": name, 'search': search_string,
                       "user_profile": user_profile, 'user_profile_name': user_name_list, 'edit': edit})

    def post(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)

        response = ""
        user_profile = a.get_user(request.GET.get("user", ""))
        search_string = ""
        user_name_list = {}

        command_type = request.POST.get("command", False)
        command_string = request.POST.get("commandStr", "")

        if command_type == 'deleteAccount':
            userInfo = {'username': command_string}
            a.command('deleteAccount', userInfo)
            return redirect('/users/')

        if user_profile is not None:
            if user_profile['username'] == user['username']:
                return redirect('/account/')

            user_name = user_profile["name"]
            user_name_list = user_name.split(' ')

            # Super complicated code because some reason we thought having one name field was easier
            first = request.POST.get("firstname", "")
            last = request.POST.get("lastname", "")
            if first == "":
                first = user_name_list[0]
            if last == "":
                if len(user_name_list) == 2:
                    last = user_name_list[1]
                else:
                    last = "Undefined"
            user_name = first + ' ' + last
            if user_name == " ":
                user_name = user_profile['name']

            userInfo = {
                'name': user_name,
                'username': user_profile['username'],
                'password': request.POST.get("password", ""),
                'role': request.POST.get("role", ""),
                'email': request.POST.get("email", ""),
                'phone': request.POST.get("phone", ""),
                'address': request.POST.get("address", "")
            }
            response = a.command('editUser', userInfo)

            user_profile = a.get_user(request.GET.get("user", ""))

        else:
            strict_return = request.POST.get("strictReturn", None)
            search_string = request.POST.get("search_string", "")
            if strict_return is None and search_string == "":
                strict_return = "all"

            search = {'strict_return': strict_return,
                      'string': search_string}
            response = a.command('search', search)
            if response.count() == 0:
                response = None

        # user, response = self.post_response(request, user)
        # response = search_criteria + search_string
        return render(request, 'main/users.html',
                      {"navbar": "users", "results": response, "user": user, "name": name, 'search': search_string,
                       "user_profile": user_profile, 'user_profile_name': user_name_list, 'edit': edit})


class Courses(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            name = user['name']

        edit = request.GET.get("edit", False)

        return render(request, "main/courses.html", {"navbar": "courses", "user": user, "name": name, "edit": edit})

    def post(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            name = user['name']

        user, response = self.post_response(request, user)

        return render(request, 'main/courses.html',
                      {"navbar": "courses", "message": response, "user": user, "name": name})


class Account(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name_list = {}
        name = ""
        if user is not None:
            name = user['name']
            name_list = name.split(' ')

        edit = request.GET.get("edit", False)

        response = ""
        return render(request, 'main/account.html',
                      {"navbar": "account", "message": response, "user": user, 'edit': edit, 'name_list': name_list,
                       'name': name})

    def post(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name_list = {}
        name = ""
        response = ""
        if user is not None:
            name = user['name']
            name_list = name.split(' ')

            current_role = user['role']

            # Super complicated code because some reason we thought having one name field was easier
            first = request.POST.get("firstname", "")
            last = request.POST.get("lastname", "")
            if first == "":
                first = name_list[0]
            if last == "":
                if len(name_list) == 2:
                    last = name_list[1]
                else:
                    last = "Undefined"
            name = first + ' ' + last
            if name == " ":
                name = user['name']

            userInfo = {
                'name': name,
                'username': user['username'],
                'password': request.POST.get("password", ""),
                'role': current_role,
                'email': request.POST.get("email", ""),
                'phone': request.POST.get("phone", ""),
                'address': request.POST.get("address", "")
            }
            response = a.command('editUser', userInfo)

        edit = request.GET.get("edit", False)
        user = a.get_loggedin(request.session.get("user", ""))

        return render(request, 'main/account.html',
                      {"navbar": "account", "message": response, "user": user, 'edit': edit, 'name_list': name_list,
                       'name': name})
