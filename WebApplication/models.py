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


class TA(models.Model):
    ta_username = models.CharField(max_length=50, default='None')


class Instructor(models.Model):
    instructor_username = models.CharField(max_length=50, default='None')


class Course(models.Model):
    course_name = models.CharField(max_length=50, default='None')
    course_code = models.CharField(max_length=5, default='None')
    course_instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=None)
    course_tas = models.ManyToManyField(TA, default=None)


class LabSection(models.Model):
    section_number = models.CharField(max_length=5, default='None')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
