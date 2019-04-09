from django.shortcuts import render
from django.views import View
from Skeleton_Classes import App

# Create your views here.

class Home(View):
  def get(self,request):
    return render(request, 'main/index.html')

  def post(self,request):
    yourInstance = App()
    commandInput = request.POST["command"]

    if commandInput:
      response = yourInstance.command(commandInput)
    else:
      response = ""
    return render(request, 'main/index.html',{"message":response})