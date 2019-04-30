from django.db import models


class User(models.Model):
    ROLE_CHOICES = (
        ("SUPERVISOR", "Supervisor"),
        ("ADMINISTRATOR", "Administrator"),
        ("INSTRUCTOR", "Instructor"),
        ("TA", "TA"),
    )

    name = models.CharField(max_length=50, default='')
    username = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    role = models.CharField(max_length=13, choices=ROLE_CHOICES, default='1')
    phone = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')


class Course(models.Model):
    course_name = models.CharField(max_length=50, default='')
    course_code = models.CharField(max_length=5, default='')
    course_instructor = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    course_time = models.CharField(max_length=50, default='')
    course_tas = models.ManyToManyField(User, related_name="course_tas_user", default=None)


class LabSection(models.Model):
    lab_ta = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    lab_number = models.CharField(max_length=5, default='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    lab_time = models.CharField(max_length=50, default='')
