from django.test import TestCase
from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from Application_Classes.CourseCommandController import CourseCommandController
from WebApplication.models import User


class TestCourseCommandController(TestCase):

    def test_edit_course_name(self):
        scmd = SuperUserCommandController()
        cmd = CourseCommandController()

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

        course1 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "111",
            'course_instructor': user1
        }
        scmd.create("Course", course1)

        course2 = {
            'data_type': "Course",
            'course_name': "Intro to Calculus",
            'course_code': "111",
            'course_instructor': user1
        }

        action = cmd.editCourse(course1['course_name'], course2)
        result = "Course information has been successfully updated"
        self.assertEqual(result, action)

    def test_edit_course_code(self):
        scmd = SuperUserCommandController()
        cmd = CourseCommandController()

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


        course1 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "111",
            'course_instructor': user1
        }
        scmd.create("Course", course1)

        course2 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "0001",
            'course_instructor': user1
        }

        action = cmd.editCourse(course1['course_name'], course2)
        result = "Course information has been successfully updated"
        self.assertEqual(result, action)

    def test_edit_course_Instructor(self):
        scmd = SuperUserCommandController()
        cmd = CourseCommandController()

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

        course1 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "111",
            'course_instructor': user1
        }
        scmd.create("Course", course1)

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
        scmd.create("User", userInfo2)

        user2 = User.objects.get(username__iexact="johnDoe")

        course2 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "111",
            'course_instructor': user2
        }

        scmd.create("Course", course2)

        action = cmd.editCourse(course1['course_name'], course2)
        result = "Course information has been successfully updated"
        self.assertEqual(result, action)

    def test_edit_course_DNE(self):
        scmd = SuperUserCommandController()
        cmd = CourseCommandController()

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

        course1 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "111",
            'course_instructor': user1
        }
        scmd.create("Course", course1)

        course2 = {
            'data_type': "Course",
            'course_name': "Intro to Calculus",
            'course_code': "111",
            'course_instructor': user1
        }

        action = cmd.editCourse("Intro to", course2)
        result = 'No course under this name'
        self.assertEqual(result, action)


    def test_delete_course(self):
        scmd = SuperUserCommandController()
        cmd = CourseCommandController()

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

        course1 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "111",
            'course_instructor': user1
        }
        scmd.create("Course", course1)

        action = cmd.deleteCourse("Intro to Comp Sci")
        result = "Course has been deleted."
        self.assertEqual(result, action)

    def test_delete_course_DNE(self):
        scmd = SuperUserCommandController()
        cmd = CourseCommandController()

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

        course1 = {
            'data_type': "Course",
            'course_name': "Intro to Comp Sci",
            'course_code': "111",
            'course_instructor': user1
        }
        scmd.create("Course", course1)

        action = cmd.deleteCourse("Intro to Computer Science")
        result = "Course could not be found or does not exist."
        self.assertEqual(result, action)