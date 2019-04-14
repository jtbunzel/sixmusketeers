import unittest
from WebApplication.Parser import *


class TestParser(unittest):

    def setUp(self):
        parser = Parser()

    def test_call_correct_command(self):
        parser.parse('createUser rock')
        self.assertEquals('createUser', parser.last_command_called)

        parser.parse('logout')
        self.assertEqual('logout', parser.last_command_called)

        parser.parse('editUser username newUsername')
        self.assertEquals('createUser', parser.last_command_called)

    def test_correct_parameters(self):
        parser.parse('createUser rock')
        self.assertEqual(['rock'], parser.last_parameter_passed)

        parser.parse('editUser username rocker')
        self.assertEqual(['username', 'rocker'], self.last_parameter_passed)

    def test_incorrect_command_name(self):
        with self.assertException():
            parser.parse('loogout')

        with self.assertException():
            parser.parse('ediyuser username rocker')

