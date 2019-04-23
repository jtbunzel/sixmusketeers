from Application_Classes.CommandController import CommandController
from Application_Classes.User import *
from Application_Classes.Course import *


class App(object):
    def __init__(self):
        self.command_controller = CommandController()
        self.set_cmd_controller()
        self.loggedin = None
        pass

    def set_cmd_controller(self):
        self.command_controller.set_pointer_to_app(self)

    def command(self, command, table_data):
        response = self.command_controller.parse(command, table_data)
        return response

    def get_loggedin(self, username):
        return self.command_controller.get_user_by_username(username)


    def get_user(self, username):
        return self.command_controller.get_user_by_username(username)


    def set_loggedin(self, new_loggedin):
        self.loggedin = new_loggedin
        pass
