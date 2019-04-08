from Skeleton_Classes.CommandController import CommandController
from Skeleton_Classes.User import *
from Skeleton_Classes.Course import *


class App(object):
    def __init__(self):
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
            if data[0] == "user":
                user1 = User()
                create_type = data[0] # course/User
                data.remove(data[0])  # remove role
                user1 = self.command_controller.create(data, create_type)
                return "created "+ user1.get_username()
            elif data[0] == "course":
                course = Course()
                create_type = data[0]
                data.remove(data[0])# syntax for this array is: "coursename code instruc #oflabs a_TA
                course = self.command_controller.create(data, create_type)
                return "created "+course.get_course_name()

            elif data[0] == "labSection":
                labSection = LabSection()
                create_type = data[0]
                data.remove(data[0])
                labSection = self.command_controller.create(data, create_type)
                return labSection

        elif command == 'assign':
            if data[0] == "user":
                user1 = User()
                assign_type = data[0]
                # data.remove(data[0])# remove role
                user1 = self.command_controller.create(data, assign_type)
                return user1

            elif data[0] == "labSection":
                labSection = LabSection()
                assign_type = data[0]
                # data.remove(data[0])
                labSection = self.command_controller.create(data, assign_type)
                return labSection

            elif data[0] == "course":
                course = Course()
                assign_type = data[0]
                # data.remove(data[0])
                course = self.command_controller.create(data, assign_type)
                return course

        elif command == 'delete':
            if data[0] == "user":
                user1 = User()
                delete_type = data[0]
                # data.remove(data[0])# remove role
                user1 = self.command_controller.create(data, delete_type)
                return user1

            elif data[0] == "labSection":
                labSection = LabSection()
                delete_type = data[0]
                # data.remove(data[0])
                labSection = self.command_controller.create(data, delete_type)
                return labSection

            elif data[0] == "course":
                course = Course()
                delete_type = data[0]
                # data.remove(data[0])
                course = self.command_controller.create(data, delete_type)
                return course
        elif command == 'edit':
            if data[0] == "user":
                user1 = User()
                assign_type = data[0]
                # data.remove(data[0])# remove role
                user1 = self.command_controller.create(data, edit_type)
                return user1

            elif data[0] == "labSection":
                labSection = LabSection()
                edit_type = data[0]
                # data.remove(data[0])
                labSection = self.command_controller.create(data, edit_type)
                return labSection

            elif data[0] == "course":
                course = Course()
                edit_type = data[0]
                # data.remove(data[0])
                course = self.command_controller.create(data, edit_type)
                return course

        elif command == 'notify':
            if data[0] == "user":
                user1 = User()
                access_type = data[0]
                # data.remove(data[0])# remove role
                user1 = self.command_controller.create(data, access_type)
                return user1

            elif data[0] == "labSection":
                labSection = LabSection()
                access_type = data[0]
                # data.remove(data[0])
                labSection = self.command_controller.create(data, access_type)
                return labSection

            elif data[0] == "course":
                course = Course()
                access_type = data[0]
                # data.remove(data[0])
                course = self.command_controller.create(data, access_type)
                return course

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
