from django.shortcuts import render
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

        instructors = a.command('get_instructors', None)

        return render(request, "main/create.html",
                      {"navbar": "create", "user": user, "name": name, "type": create_type, 'instructors': instructors})

    def post(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        response = ""
        current_role = str(user['role'])
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
                response = a.command('create', userInfo)
        return render(request, 'main/create.html',
                      {"navbar": "create", "message": response, "user": user, "name": name})


class Users(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            name = user['name']

        return render(request, "main/users.html", {"navbar": "users", "user": user, "name": name})

    def post(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            name = user['name']
        search_criteria = request.POST.get("search_criteria", "")
        search_string = request.POST.get("search_string", "")
        search = {'criteria': search_criteria,
                  'string': search_string}
        response = a.command('search', search)
        # user, response = self.post_response(request, user)
        # response = search_criteria + search_string
        return render(request, 'main/users.html', {"navbar": "users", "message": response, "user": user, "name": name})


class Courses(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = ""
        if user is not None:
            name = user['name']

        return render(request, "main/courses.html", {"navbar": "courses", "user": user, "name": name})

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
        if user is not None:
            name = user['name']
            name_list = name.split(' ')

        edit = request.GET.get("edit", False)

        response = ""
        return render(request, 'main/account.html',
                      {"navbar": "account", "message": response, "user": user, 'edit': edit, 'name': name_list})

    def post(self, request):
        self.init_logged_in(request)

        user = a.get_loggedin(request.session.get("user", ""))
        name = "",
        if user is not None:
            name = user['name']

        # user, response = self.post_response(request, user)
        user_name = request.POST.get("username", "")
        user_first = request.POST.get("firstname", "")
        response = ""
        print(user_first)
        print(user_name)
        return render(request, 'main/account.html',
                      {"navbar": "account", "message": response, "user": user, "name": name, "user_name": user_name,
                       "user_first": user_first})
