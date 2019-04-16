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
        action = user.showUser()

        pass
