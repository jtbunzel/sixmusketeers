from django.test import TestCase
from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from Application_Classes.LabSectionCommandController import LabSectionCommandController
from WebApplication.models import User, Course


class TestLabSectionCommandController(TestCase):


    def test_delete_lab(self):
        scmd = SuperUserCommandController()
        lcmd = LabSectionCommandController

        userInfo = {
            'data_type': "User",
            'username': "HarryPotter",
            'name': "Harry",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "HarryPotter@yahoo.com",
            'phone': "4142245326",
            'address': "123 fake st."
        }

        scmd.create("User", userInfo)
        user1 = User.objects.get(username__iexact="HarryPotter")

        courseInfo = {
            'data_type': "Course",
            'course_name': "Intro to CS",
            'course_code': "007",
            'course_instructor': user1
        }

        scmd.create("Course", courseInfo)
        course1 = Course.objects.get(course_name__iexact="Intro to CS")

        labInfo = {
            'data_type': "LabSection",
            'lab_ta': user1,
            'lab_number': "007",
            'course_name': course1
        }
        lab1 = scmd.create("Lab", labInfo)


        action = lcmd.deleteLabSection(lab1['lab_number'])

        result = "Lab Section has been deleted."
        self.assertEqual(result, action)

    def test_delete_lab_DNE(self):
        scmd = SuperUserCommandController()
        lcmd = LabSectionCommandController

        userInfo = {
            'data_type': "User",
            'username': "HarryPotter",
            'name': "Harry",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "HarryPotter@yahoo.com",
            'phone': "4142245326",
            'address': "123 fake st."
        }

        scmd.create("User", userInfo)
        user1 = User.objects.get(username__iexact="HarryPotter")

        courseInfo = {
            'data_type': "Course",
            'course_name': "Intro to CS",
            'course_code': "007",
            'course_instructor': user1
        }

        scmd.create("Course", courseInfo)
        course1 = Course.objects.get(course_name__iexact="Intro to CS")

        labInfo = {
            'data_type': "LabSection",
            'lab_ta': user1,
            'lab_number': "007",
            'course_name': course1
        }
        lab1 = scmd.create("Lab", labInfo)


        action = lcmd.deleteLabSection(lab1['lab_number'])
        result = "Failed to delete, Lab Section does not exist!"
        self.assertEqual(result, action)

    def test_edit_lab_Instructor(self):
        scmd = SuperUserCommandController()
        lcmd = LabSectionCommandController()

        userInfo = {
            'data_type': "User",
            'username': "HarryPotter",
            'name': "Harry",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "HarryPotter@yahoo.com",
            'phone': "4142245326",
            'address': "123 fake st."
        }

        scmd.create("User", userInfo)
        user1 = User.objects.get(username__iexact="HarryPotter")

        courseInfo = {
            'data_type': "Course",
            'course_name': "Intro to CS",
            'course_code': "007",
            'course_instructor': user1
        }

        scmd.create("Course", courseInfo)
        course1 = Course.objects.get(course_name__iexact="Intro to CS")

        labInfo = {
            'data_type': "LabSection",
            'lab_ta': user1,
            'lab_number': "007",
            'course_name': course1
        }
        scmd.create("LabSection", labInfo)

        userInfo2 = {
            'data_type': "User",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "1234 fake st."
        }
        user2 = scmd.create("User", userInfo2)

        labInfo2 = {
            'data_type': "LabSection",
            'lab_ta': user2,
            'lab_number': "008",
            'course_name': course1
        }
        scmd.create("LabSection", labInfo2)

        action = lcmd.editLabSection(labInfo['lab_number'], labInfo2)

        result = "Lab Section information has been successfully updated"
        self.assertEqual(result, action)

    def test_edit_lab_Number(self):
        scmd = SuperUserCommandController()
        lcmd = LabSectionCommandController()

        userInfo = {
            'data_type': "User",
            'username': "HarryPotter",
            'name': "Harry",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "HarryPotter@yahoo.com",
            'phone': "4142245326",
            'address': "123 fake st."
        }

        scmd.create("User", userInfo)
        user1 = User.objects.get(username__iexact="HarryPotter")

        courseInfo = {
            'data_type': "Course",
            'course_name': "Intro to CS",
            'course_code': "007",
            'course_instructor': user1
        }

        scmd.create("Course", courseInfo)
        course1 = Course.objects.get(course_name__iexact="Intro to CS")

        labInfo = {
            'data_type': "LabSection",
            'lab_ta': user1,
            'lab_number': "007",
            'course_name': course1
        }
        scmd.create("LabSection", labInfo)

        labInfo2 = {
            'data_type': "LabSection",
            'lab_ta': user1,
            'lab_number': "777",
            'course_name': course1
        }
        scmd.create("LabSection", labInfo2)

        action = lcmd.editLabSection(labInfo['lab_number'], labInfo2)

        result = "Lab Section information has been successfully updated"
        self.assertEqual(result, action)

    def test_edit_lab_course(self):
        scmd = SuperUserCommandController()
        lcmd = LabSectionCommandController()

        userInfo = {
            'data_type': "User",
            'username': "HarryPotter",
            'name': "Harry",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "HarryPotter@yahoo.com",
            'phone': "4142245326",
            'address': "123 fake st."
        }

        scmd.create("User", userInfo)
        user1 = User.objects.get(username__iexact="HarryPotter")

        courseInfo = {
            'data_type': "Course",
            'course_name': "Intro to CS",
            'course_code': "007",
            'course_instructor': user1
        }

        scmd.create("Course", courseInfo)
        course1 = Course.objects.get(course_name__iexact="Intro to CS")

        labInfo = {
            'data_type': "LabSection",
            'lab_ta': user1,
            'lab_number': "007",
            'course_name': course1
        }
        scmd.create("LabSection", labInfo)

        course2 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "111",
            'course_instructor': user1
        }

        scmd.create("Course", course2)

        labInfo2 = {
            'data_type': "LabSection",
            'lab_ta': user1,
            'lab_number': "008",
            'course_name': course2
        }
        scmd.create("LabSection", labInfo2)

        action = lcmd.editLabSection(labInfo['lab_number'], labInfo2)

        result = "Lab Section information has been successfully updated"
        self.assertEqual(result, action)
