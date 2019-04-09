from django.shortcuts import render
from django.views import View
import hashlib

class Home(View):
    def get(self, request):
        return render(request, 'main/index.html')

    def post(self, request):
        return render(request, 'main/index.html')


class Command(View):
    def get(self, request):
        return render(request, 'main/commandLine.html')

    def post(self, request):
        return render(request, 'main/commandLine.html')