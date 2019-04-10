from django.shortcuts import render, redirect
from django.views import View
from Skeleton_Classes.App import App
from ApplicationSession import Credentials

# Create your views here.

a = App()

class Home(View):
    def __init__(self):
        self.credentials = Credentials.Credentials(a, DEBUG=True)

    def init_logged_in(self, request):
        if "user" in request.session and request.session["user"] != "":
            self.credentials.user = self.credentials.controller.get_loggedin()
        else:
            self.credentials.user = None

    def get(self, request):
        self.init_logged_in(request)

        user = None
        if self.credentials.user is not None:
            user = self.credentials.user.username

        return render(request, "main/index.html", {"user": user})

    def post(self, request):
        self.init_logged_in(request)
        user = self.credentials.user

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
                    response = "Logged out"
                else:
                    response = a.command(command_input)
        else:
            if command_type is not None:
                if command_type == 'login':
                    username = request.POST.get('username')
                    password = request.POST.get('password')

                    res = a.command_controller.login(username, password)
                    if res == 'User logged in.':
                        response = "Logged in"
                        request.session["user"] = request.POST["username"]
                        self.init_logged_in(request)
                        user = self.credentials.user
                    else:
                        response = "Incorrect login"

        return render(request, 'main/index.html', {"message": response, "user": user})

