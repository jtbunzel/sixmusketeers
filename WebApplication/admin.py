from django.contrib import admin

# Register your models here.
from .models import User, Course, TA, Instructor, LabSection

admin.site.register(User)
admin.site.register(Instructor)
admin.site.register(TA)

admin.site.register(Course)
admin.site.register(LabSection)