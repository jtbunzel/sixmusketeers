from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from WebApplication.models import User
from django.test import TestCase

cmd = SuperUserCommandController()


class TestAdminSuperCommandController(TestCase):

    # database testing for create
    def test_User_can_create(self):
        with self.assertRaises(Exception):
            User.objects.get(username="boyland123").username
        userInfo = {
            'data_type': "user",
            'username': "boyland123",
            'name': "boyland123",
            'password': "password",
            'user_type': "TA".upper(),
            'email': "email@uwm.edu",
            'phone': "phone",
            'address': "address"
        }
        str = cmd.create("instructor", userInfo)
        self.assertEqual(User.objects.get(username="boyland123").username
                         , 'boyland123')
        self.assertEqual(User.objects.get(username="boyland123").password
                         , 'password')
        self.assertTrue(User.objects.get(username="boyland123").password
                        is not 'passwordddd')
        self.assertTrue(User.objects.get(username="boyland123").username
                        is not 'boy land')
        self.assertTrue(User.objects.get(username="boyland123").role
                        is not 'instructor')
        self.assertEqual(User.objects.get(username="boyland123").role
                         , 'TA')
        self.assertTrue(User.objects.get(username="boyland123").address
                        is not 'not address ')
        self.assertEqual(User.objects.get(username="boyland123").address
                         , 'address')
        self.assertEqual(User.objects.get(username="boyland123").email
                         , 'email@uwm.edu')
        self.assertTrue(User.objects.get(username="boyland123").email
                        is not 'address ')

    def test_delete_user(self):
        cmd = SuperUserCommandController()
        userInfo = {
            'data_type': "user",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'user_type': "TA".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "1234 fake st."
        }
        cmd.create("TA", userInfo)
        action = cmd.deleteUser("johnDoe")
        result = "User successfully deleted."
        self.assertEqual(result, action)

    def test_delete_admin(self):
        cmd = SuperUserCommandController()
        userInfo = {
            'data_type': "user",
            'username': "admin",
            'name': "jojo",
            'password': "password",
            'user_type': "SUPERVISOR".upper(),
            'email': "MojoJojo@yahoo.com",
            'phone': "4142247777",
            'address': "777 fake st."
        }
        cmd.create("SUPERVISOR", userInfo)
        action = cmd.deleteUser("admin")
        result = "Can not delete Admin account"
        self.assertEqual(result, action)

    def test_showAll(self):
        cmd = SuperUserCommandController()
        userInfo = {
            'data_type': "user",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'user_type': "TA".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "1234 fake st."
        }
        userInfo2 = {
            'data_type': "user",
            'username': "HarryPotter",
            'name': "Harry",
            'password': "password",
            'user_type': "Instructor".upper(),
            'email': "HarryPotter@yahoo.com",
            'phone': "4142245326",
            'address': "123 fake st."
        }
        cmd.create("TA", userInfo)
        cmd.create("Instructor", userInfo2)
        result = cmd.showAll()
        newResult = "johnDoe john TA 4142240088 johnDoe123@yahoo.com 1234 fake st.\nHarryPotter Harry INSTRUCTOR 4142245326 HarryPotter@yahoo.com 123 fake st.\n"
        self.assertEqual(result, newResult)
