from django.shortcuts import render
from django.views import View
from Skeleton_Classes.App import*


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'sixmusketeers\base.html')

    def post(self, request):
        yourInstance = App()
        commandInput = request.POST["command"]
        if commandInput:
            response = yourInstance.command(commandInput)
        else:
            response = ""
        return render(request, 'sixmusketeers\base.html', {"message": response})
