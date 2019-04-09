from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50, default='None')
    last_name = models.CharField(max_length=50, default='None')
    username = models.CharField(max_length=50, default='None')
    password = models.CharField(max_length=50, default='None')
    role = models.CharField(max_length=50, default='None')
    phone = models.CharField(max_length=50, default='None')
    email = models.CharField(max_length=50, default='None')
    address = models.CharField(max_length=50, default='None')

class Course(models.Model):
    course_name = models.CharField(max_length=50, default='None')
    course_code = models.CharField(max_length=5)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, default='None')
    grader_ta = models.ForeignKey(User, on_delete=models.SET(None) default='None')

class Lab(models.Model):
    section_number = models.CharField(max_length=5)
    course = models.ForeignKey(Course, on_delete=models.CASCADE())
