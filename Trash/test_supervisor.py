import unittest
import app.py

class TestApp(unittest.TestCase):
    def test_create_course(self):
        # Assume the user is logged in
        # Assume the user is a supervisor or an administrator
        # Assume the course name doesn't exist already

        a = app()
        result = a.command("create course name")
        self.assertEqual("course name created", result)

    def test_create__account(self):
        # Assume the user is logged in
        # Assume the user is a supervisor or an administrator
        # Assume the username doesn't exist already

        a = app()
        result = a.command("create account username password")
        self.assertEqual("account username created", result)

    def test_delete__account(self):
        # Assume the user is logged in
        # Assume the user is a supervisor or an administrator
        # Assume the username exists
        # Assume the account is not a supervisor
        # Assume if the user is an administrator, that the account is not a supervisor or an administrator
        # Assume the username can be the user's username

        a = app()
        result = a.command("delete username")
        self.assertEqual("account deleted", result)

    def test_edit__account(self):
        # Assume the user is logged in
        # Assume the user is a supervisor or an administrator
        # Assume the account exists
        # Assume the account is not a supervisor
        # Assume if the user is an administrator, that the account is not a supervisor or an administrator
        # Assume the account can be the user's account

        a = app()
        result = a.command("edit username criteria")
        self.assertEqual("username criteria edited", result)

    def test_send_email(self):
        # Assume the user is logged in
        # Assume the user is a supervisor, an administrator, or an instructor
        # Assume if the user is an instructor, they can only send to TAs
        # Assume the message is not blank
        # Assume the accounts exist
        # Assume the account's email exists

        a = app()
        result = a.command("send users message")
        self.assertEqual("message sent to user", result)

    def test_access_data(self):
        # Assume the user is logged in
        # Assume the user is a supervisor, an administrator
        # Assume the data exists

        a = app()
        result = a.command("access data")
        self.assertEqual("data accessed", result)

    def test_assign_instructor(self):
        # Assume the user is logged in
        # Assume the user is a supervisor
        # Assume the account exists
        # Assume the account is an instructor
        # Assume the course exists

        a = app()
        result = a.command("assign username course")
        self.assertEqual("username assigned to course", result)

    def test_assign_ta(self):
        # Assume the user is logged in
        # Assume the user is a supervisor
        # Assume the ta username exists
        # Assume the username is a TA
        # Assume the course exists

        a = app()
        result = a.command("assign username course")
        self.assertEqual("username assigned to course", result)

    def test_assign_ta_to__lab(self):
        # Assume the user is logged in
        # Assume the user is a supervisor or an instructor
        # Assume the TA account exists
        # Assume the account is a TA
        # Assume the course exists

        a = app()
        result = a.command("assign username course lab")
        self.assertEqual("username assigned to course lab", result)