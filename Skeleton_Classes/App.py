from Skeleton_Classes.CommandController import CommandController
from Skeleton_Classes.User import *

class App(object):
    def __init__(self):
        # self.command_controller = CommandController()
        # self.command_controller.set_pointer_to_app(self)
        pass

    def set_cmd_controller(self):
        self.command_controller = CommandController()
        self.command_controller.set_pointer_to_app(self)

    def command(self, a):
        command = self.command_controller.parse(a)
        print(command)  # test your command
        data = []
        data = a.split()
        print(data)
        data.remove(command)
        print(data)
        if command == 'create':
            user1 = User()
            user1 = self.command_controller.create(data)
            return user1
        elif self.command_controller.parse(a) == 'assign':
            self.assign

        elif self.command_controller.parse(a) == 'delete':
            self.delete

        elif self.command_controller.parse(a) == 'edit':
            self.edit

        elif self.command_controller.parse(a) == 'notify':
            self.notiy




    def respond_to_prompt(self, a):
        pass


    def edit(accountDetails, newDetails):
        pass


    def assignments(courses):
        pass


    def access(self):
        pass


    def get_loggedin(self):
        pass


    def set_loggedin(self, user):
        pass
