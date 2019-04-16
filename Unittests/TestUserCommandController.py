from django.test import TestCase
from WebApplication.models import User
from WebApplication.UserCommandController import UserCommandController

class TestAdminSuperCommandController(TestCase):

    def setUp(self):
        user = User()
        pass

    def test_edit_user(self):
        pass

    def test_showUser(self):
        user = UserCommandController()
        action = user.showUser(self)
        result = "First name = " + "Rock" + "\n" + "Last name = " + "gomez" + "\n" + "Address = " + "Milwaukee" + "\n" + "Phone = " + "4148563625" + "\n" + "Email = " + "rock@uwm.edu" + "\n"
        self.assertEqual(action,result)
