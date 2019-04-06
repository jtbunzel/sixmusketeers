from django.contrib import admin

# Register your models here.
from WebApplication.models import User, Course

admin.site.register(User)
admin.site.register(Course)