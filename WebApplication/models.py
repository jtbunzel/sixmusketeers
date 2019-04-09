from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50, default='None')
    last_name = models.CharField(max_length=50, default='None')
    username = models.CharField(max_length=50, default='None')
    password = models.CharField(max_length=50, default='None')
    role = models.CharField(max_length=50, default='None')
    phone = models.CharField(max_length=50, default='None')
    email = models.CharField(max_length=50, default='None')
    address = models.CharField(max_length=50, default='None')


class TA(models.model, User):
    ta = models.CharField(max_length=10)


class Instructor(models.model, User):
    instructor = models.CharField(max_length=10)


class Course(models.Model):
    course_name = models.CharField(max_length=50, default='None')
    course_code = models.CharField(max_length=5)
    course_instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default='None')
    course_tas = models.ManyToManyField(TA, on_delete=models.SET(None), default='None')


class LabSection(models.Model):
    section_number = models.CharField(max_length=5)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
