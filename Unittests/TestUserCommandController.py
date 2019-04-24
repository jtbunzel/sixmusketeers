from Application_Classes.UserCommandController import UserCommandController
from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from WebApplication.models import User
from django.test import TestCase

cmd = UserCommandController()
scmd = SuperUserCommandController()


class TestUserCommandController(TestCase):

    def test_edit_user(self):
        scmd = SuperUserCommandController()
        userInfo = {
            'data_type': "user",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'user_type': "Instructor".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "777 fake st."
        }
        scmd.create("Instructor", userInfo)

        newInfo = {
            'data_type': "user",
            'username': "Mojojojo",
            'name': "Mojo",
            'password': "pass",
            'user_type': "Instructor".upper(),
            'email': "Mojo@yahoo.com",
            'phone': "4147771111",
            'address': "777 real st."
        }

        action = cmd.editUser("johnDoe", newInfo)
        result = "User information has been successfully updated"

#        show = scmd.showAll()
#        print(show)
        self.assertEqual(result, action)

    def test_showUser(self):
        user = UserCommandController()
        action = user.showUser()
        result = "Name = " + "Rock" + "\n" + "Address = " + "Milwaukee" + "\n" + "Phone = " + "4148563625" + "\n" + "Email = " + "rock@uwm.edu" + "\n"
        self.assertEqual(action,result)
