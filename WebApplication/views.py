from django.shortcuts import render, redirect
from django.views import View
from Application_Classes.App import App
from ApplicationSession import Credentials

# Create your views here.

a = App()


class BaseView(View):
    def __init__(self):
        self.credentials = Credentials.Credentials(a, DEBUG=True)

    def init_logged_in(self, request):
        if "user" in request.session and request.session["user"] != "":
            self.credentials.user = self.credentials.controller.get_loggedin()
        else:
            self.credentials.user = None

    def post_response(self, request, user):
        command_type = request.POST.get("command", False)
        command_input = request.POST.get("commandStr", False)
        response = ""

        if user is not None:
            if command_type is not None:
                if command_type == 'logout':
                    a.command_controller.logout()
                    request.session["user"] = ""
                    user = None
                    self.init_logged_in(request)
                else:
                    if command_input:
                        response = a.command(command_input)
        else:
            if command_type is not None:
                if command_type == 'login':
                    username = request.POST.get('username')
                    password = request.POST.get('password')

                    res = a.command_controller.login(username, password)
                    if res == 'User logged in.':
                        request.session["user"] = request.POST["username"]
                        self.init_logged_in(request)
                        user = self.credentials.user
                    else:
                        response = "Incorrect login"

        return user, response


class Home(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = None
        name = ""
        if self.credentials.user is not None:
            user = self.credentials.user.username
            name = self.credentials.user.name

        return render(request, "main/index.html", {"navbar": "home", "user": user, "name": name})

    def post(self, request):
        self.init_logged_in(request)
        user = self.credentials.user
        name = ""
        if user is not None:
            name = self.credentials.user.name

        user, response = self.post_response(request, user)

        return render(request, 'main/index.html', {"navbar": "home", "message": response, "user": user, "name": name})


class Create(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = None
        name = ""
        if self.credentials.user is not None:
            user = self.credentials.user.username
            name = self.credentials.user.name

        return render(request, "main/create.html", {"navbar": "create", "user": user, "name": name})

    def post(self, request):
        self.init_logged_in(request)
        user = self.credentials.user
        name = self.credentials.user.name

        user, response = self.post_response(request, user)

        return render(request, 'main/create.html', {"navbar": "create", "message": response, "user": user, "name": name})


class Users(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = None
        name = ""
        if self.credentials.user is not None:
            user = self.credentials.user.username
            name = self.credentials.user.name

        return render(request, "main/users.html", {"navbar": "users", "user": user, "name": name})

    def post(self, request):
        self.init_logged_in(request)
        user = self.credentials.user
        name = self.credentials.user.name

        user, response = self.post_response(request, user)

        return render(request, 'main/users.html', {"navbar": "users", "message": response, "user": user, "name": name})


class Courses(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = None
        name = ""
        if self.credentials.user is not None:
            user = self.credentials.user.username
            name = self.credentials.user.name

        return render(request, "main/courses.html", {"navbar": "courses", "user": user, "name": name})

    def post(self, request):
        self.init_logged_in(request)
        user = self.credentials.user
        name = self.credentials.user.name

        user, response = self.post_response(request, user)

        return render(request, 'main/courses.html', {"navbar": "courses", "message": response, "user": user, "name": name})


class Account(BaseView):
    def get(self, request):
        self.init_logged_in(request)

        user = None
        name = ""
        if self.credentials.user is not None:
            user = self.credentials.user.username
            name = self.credentials.user.name

        return render(request, "main/account.html", {"navbar": "account", "user": user, "name": name})

    def post(self, request):
        self.init_logged_in(request)
        user = self.credentials.user
        name = self.credentials.user.name

        user, response = self.post_response(request, user)

        return render(request, 'main/account.html', {"navbar": "account", "message": response, "user": user, "name": name})
