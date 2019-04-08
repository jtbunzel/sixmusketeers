from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    full_name = models.CharField(max_length=40)
    address = models.CharField(max_length=60)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=30)
    rank = models.IntegerField()


class Instructor(User):
    pass


class TA(User):
    pass


class Supervisor(User):
    pass


class Administrator(User):
    pass


class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=60)
    course_instructor = models.ForeignKey(Instructor, on_delete=models.SET(None))
    course_TAs = models.ManyToManyField(TA)

class LabSection(models.Model):
    section_number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_TA = models.ForeignKey(TA, on_delete=models.SET(None))
