from Application_Classes.UserCommandController import UserCommandController
from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from django.test import TestCase

cmd = UserCommandController()
scmd = SuperUserCommandController()


class TestUserCommandController(TestCase):

    def test_edit_user(self):
        scmd = SuperUserCommandController()
        userInfo = {
            'data_type': "User",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "777 fake st."
        }
        scmd.create("User", userInfo)

        newInfo = {
            'data_type': "User",
            'username': "Mojojojo",
            'name': "Mojo",
            'password': "pass",
            'role': "Instructor".upper(),
            'email': "Mojo@yahoo.com",
            'phone': "4147771111",
            'address': "777 real st."
        }

        action = cmd.editUser("johnDoe", newInfo)
        result = "User information has been successfully updated"

        self.assertEqual(result, action)

    def test_edit_user_DNE(self):
        scmd = SuperUserCommandController()

        userInfo = {
            'data_type': "User",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "777 fake st."
        }
        scmd.create("User", userInfo)

        newInfo = {
            'data_type': "User",
            'username': "Mojojojo",
            'name': "Mojo",
            'password': "pass",
            'role': "Instructor".upper(),
            'email': "Mojo@yahoo.com",
            'phone': "4147771111",
            'address': "777 real st."
        }

        action = cmd.editUser("Mojojojo", newInfo)
        result = 'No user under this name'

        self.assertEqual(result, action)

    def test_showUser(self):

        scmd = SuperUserCommandController()
        userInfo = {
            'data_type': "User",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "777 fake st."
        }
        scmd.create("User", userInfo)

        action = cmd.showUser("johnDoe")
        result = "Username: " + "johnDoe" + "Name: " + "john" + "Role: " + "INSTRUCTOR" + "Phone Number: " + "4142240088" + "Email: " + "johnDoe123@yahoo.com" + "Address: " + "777 fake st."
        self.assertEqual(result, action)

    def test_showUser_DNE(self):

        scmd = SuperUserCommandController()
        userInfo = {
            'data_type': "User",
            'username': "johnDoe",
            'name': "john",
            'password': "password",
            'role': "Instructor".upper(),
            'email': "johnDoe123@yahoo.com",
            'phone': "4142240088",
            'address': "777 fake st."
        }
        scmd.create("User", userInfo)

        action = cmd.showUser("Mojojojo")
        result = "User could not be found."
        self.assertEqual(result, action)