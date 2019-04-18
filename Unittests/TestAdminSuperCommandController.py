from django.test import TestCase
from WebApplication.AdminSuperCommandController import SuperUserCommandController
from WebApplication.models import User
from django.test import TestCase

cmd = SuperUserCommandController()


class TestAdminSuperCommandController(TestCase):

    def setUp(self):
        pass

    def test_create_user(self):
        pass

    def test_delete_user(self):
        cmd = SuperUserCommandController()
        cmd.createUser(johnDoe, TA)
        action = cmd.deleteUser(johnDoe)
        result = "User successfully deleted."
        self.assertEqual(result, action)

    def test_showAll(self):
        cmd = SuperUserCommandController()
        cmd.createUser(johnDoe, TA)
        cmd.createUser(HarryPotter, Instructor)
        result = cmd.showAll()
        #       #When it works replace default fields with ''
        newResult = "'johnDoe' 'last' 'phone' 'address' 'email' 'TA' \n 'HarryPotter'  'last' 'phone' 'address' 'email' 'Instructor'"
        self.assertEqual(result, newResult)
    # database testing for create
    def test_User_can_create(self):
        with self.assertRaises(Exception):
            User.objects.get(username="boyland123").username
        credentials_array = ["boyland123", "password"]
        str = cmd.create("instructor", credentials_array)
        self.assertEqual(User.objects.get(username="boyland123").username
                         , 'boyland123')
        self.assertEqual(User.objects.get(username="boyland123").password
                         , 'password')
        self.assertTrue(User.objects.get(username="boyland123").password
                        is not 'passwordddd')
        self.assertTrue(User.objects.get(username="boyland123").username
                        is not 'boy land')
