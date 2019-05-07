from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from WebApplication.models import User
from django.test import TestCase

cmd = SuperUserCommandController()


class TestAdminSuperCommandController(TestCase):

    # database testing for create
#    def test_User_can_create(self):
#        with self.assertRaises(Exception):
#            User.objects.get(username="boyland123").username
#        userInfo = {
#            'data_type': "user",
#            'username': "boyland123",
#            'name': "boyland123",
#            'password': "password",
#            'user_type': "TA".upper(),
#            'email': "email@uwm.edu",
#            'phone': "phone",
#            'address': "address"
#        }
#        str = cmd.create("instructor", userInfo)
#        self.assertEqual(User.objects.get(username="boyland123").username
#                         , 'boyland123')
#        self.assertEqual(User.objects.get(username="boyland123").password
#                         , 'password')
#        self.assertTrue(User.objects.get(username="boyland123").password
#                        is not 'passwordddd')
#        self.assertTrue(User.objects.get(username="boyland123").username
#                        is not 'boy land')
#        self.assertTrue(User.objects.get(username="boyland123").role
#                        is not 'instructor')
#        self.assertEqual(User.objects.get(username="boyland123").role
#                         , 'TA')
#        self.assertTrue(User.objects.get(username="boyland123").address
#                        is not 'not address ')
#        self.assertEqual(User.objects.get(username="boyland123").address
#                         , 'address')
#        self.assertEqual(User.objects.get(username="boyland123").email
#                         , 'email@uwm.edu')
#        self.assertTrue(User.objects.get(username="boyland123").email
#                        is not 'address ')

    def test_delete_user(self):
        cmd = SuperUserCommandController()
        userInfo = {
            'data_type': "User",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'role': "TA".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "1234 fake st."
        }
        cmd.create("User", userInfo)
        action = cmd.deleteUser("johnDoe")
        result = (userInfo['username'] + " deleted successfully.")
        self.assertEqual(result, action)

    def test_delete_supervisor(self):
        cmd = SuperUserCommandController()
        userInfo = {
            'data_type': "User",
            'username': "admin123",
            'name': "jojo",
            'password': "password",
            'role': "SUPERVISOR".upper(),
            'email': "MojoJojo@yahoo.com",
            'phone': "4142247777",
            'address': "777 fake st."
        }
        a123 = cmd.create("User", userInfo)
        print(a123)

        action = cmd.deleteUser("admin123")
        result = (userInfo['username'] + " is a Supervisor and cannot be deleted.")
        self.assertEqual(result, action)

    def test_showAll(self):
        cmd = SuperUserCommandController()
        userInfo = {
            'data_type': "User",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'role': "TA".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "1234 fake st."
        }
        userInfo2 = {
            'data_type': "User",
            'username': "HarryPotter",
            'name': "Harry",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "HarryPotter@yahoo.com",
            'phone': "4142245326",
            'address': "123 fake st."
        }
        cmd.create("User", userInfo)
        cmd.create("User", userInfo2)
        result = cmd.showAll()
        newResult = "johnDoe john TA 4142240088 johnDoe123@yahoo.com 1234 fake st.\nHarryPotter Harry INSTRUCTOR 4142245326 HarryPotter@yahoo.com 123 fake st.\n"
        self.assertEqual(result, newResult)

    def test_showAll_empty_database(self):
        cmd = SuperUserCommandController()
        result = cmd.showAll()
        newResult = ""
        self.assertEqual(result, newResult)

    def test_create_course(self):
        cmd = SuperUserCommandController()

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

        cmd.create("User", userInfo)
        user1 = User.objects.get(username__iexact="HarryPotter")

        courseInfo = {
            'data_type': "Course",
            'course_name': "Intro to CS",
            'course_code': "007",
            'course_instructor': user1
        }

        action = cmd.create("Course", courseInfo)
        result = "Intro to CS created as 007."
        self.assertEqual(result,action)

    def test_create_course_already_exists(self):
        cmd = SuperUserCommandController()

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

        cmd.create("User", userInfo)
        user1 = User.objects.get(username__iexact="HarryPotter")

        courseInfo = {
            'data_type': "Course",
            'course_name': "Intro to CS",
            'course_code': "007",
            'course_instructor': user1
        }
        cmd.create("Course", courseInfo)
        courseInfo2 = {
            'data_type': "Course",
            'course_name': "Intro to CS",
            'course_code': "111",
            'course_instructor': user1
        }

        action = cmd.create("Course", courseInfo2)
        result = "Course is already in use!"
        self.assertEqual(result, action)
