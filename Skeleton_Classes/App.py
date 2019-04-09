from Skeleton_Classes.CommandController import CommandController
from Skeleton_Classes.User import *
from Skeleton_Classes.Course import *


class App(object):
    def __init__(self):
        self.command_controller = CommandController()
        self.set_cmd_controller()
        self.loggedin = None
        pass

    def set_cmd_controller(self):
        self.command_controller.set_pointer_to_app(self)

    def command(self, a):
        response = self.command_controller.parse(a)
        return response

    def get_loggedin(self):
        return self.loggedin
        pass

    def set_loggedin(self, new_loggedin):
        self.loggedin = new_loggedin
        pass
