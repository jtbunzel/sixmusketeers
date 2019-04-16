from django.test import TestCase
from WebApplication.AdminSuperCommandController import SuperUserCommandController

class TestAdminSuperCommandController(TestCase):
    cmd = SuperUserCommandController()

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

