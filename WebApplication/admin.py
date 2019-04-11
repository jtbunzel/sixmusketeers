from django.contrib import admin

# Register your models here.
from .models import User, Course, LabSection

admin.site.register(User)

admin.site.register(Course)
admin.site.register(LabSection)