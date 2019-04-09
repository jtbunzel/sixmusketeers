from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='password')
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class TA(User):
    ta_field = models.CharField(max_length=50)


class Instructor(User):
    instructor_field = models.CharField(max_length=50)


class Course(models.Model):
    course_name = models.CharField(max_length=50, default='None')
    course_code = models.CharField(max_length=5, default='None')
    course_instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course_tas = models.ManyToManyField(TA, default=None)


class LabSection(models.Model):
    section_number = models.CharField(max_length=5, default='None')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
