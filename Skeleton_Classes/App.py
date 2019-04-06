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
            user1 = User()
            user1 = self.command_controller.assign(data)
            return user1

        elif self.command_controller.parse(a) == 'delete':
            user1 = User()
            user1 = self.command_controller.delete(data)
            return user1

        elif self.command_controller.parse(a) == 'edit':
            user1 = User()
            user1 = self.command_controller.edit(data)
            return user1

        elif self.command_controller.parse(a) == 'notify':
            user1 = User()
            user1 = self.command_controller.notify(data)
            return user1


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
