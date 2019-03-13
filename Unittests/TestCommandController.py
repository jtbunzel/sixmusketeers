import unittest as bk
from Skeleton_Classes.CommandController import CommandController
from User import *
from Administrator import *
from Course import *
from Instructor import *
from Lab_section import *
from Supervisor import *
from TA import *

class TestCommandController(bk.TestCase):
    def setup(self):
        self.command= CommandController()

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

