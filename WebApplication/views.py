from django.shortcuts import render, redirect
from django.views import View
from Skeleton_Classes.App import App

# Create your views here.

a = App()

class Home(View):
    def get(self,request):
        return render(request, 'main/index.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        res = a.command_controller.login(username, password)
        if res == 'User logged in.':
            return redirect('/command')
        else:
            return redirect('/')


class CommandView(View):
    def get(self, request):
        return render(request, 'main/commandLine.html')

    def post(self, request):
        commandInput = request.POST["command"]

        if commandInput:
            response = a.command(commandInput)
        else:
            response = ""
        return render(request, 'main/commandLine.html',{"message":response})