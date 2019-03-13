import unittest as bk
from  CommandController import*
from User import *
from Administrator import *
from Course import *
from Instructor import *
from Lab_section import *
from Supervisor import *
from TA import *

class TestCommandController(bk.TestCase):
    def setup(self):
        self.command= CommandController(self, Course)
        self.command.User('wheelerg', '1234')
        self.command.set_full_name('Grant Wheeler')
        self.command.set_address('3200 N. Cramer St. Milwaukee, WI 53211')
        self.command.user.set_email('wheelerg@uwm.edu')
        self.command.set_phone_number('4148857236')
        self.command.supervisor = Supervisor('hunterg', 'passwerd')
        self.command.supervisor.set_full_name('Hunter Green')
        self.command.supervisor.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.command.supervisor.set_email('hunterg@uwm.edu')
        self.Command.supervisor.set_phone_number('414-569-8784')
        self.admin = Administrator('hunterg', 'passwerd')
        self.command.admin.set_full_name('Hunter Green')
        self.command.admin.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.commanad.admin.set_email('hunterg@uwm.edu')
        self.command.admin.set_phone_number('414-569-8784')


    def test_parse(self):

    def test_login(self):

    def test_create(self):

    def test_notify(self):

    def test_assing(self):

    def test_logout(self):

    def test_edit(self):

    def test_access(self):

    def test_delete(self):

    def test_assignments(self):

    def test_verify(self):

if __name__ == '__main__':
    unittest.main()

