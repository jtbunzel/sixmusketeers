from Skeleton_Classes.Instructor import *
from Skeleton_Classes.MOCK_Instructor import *


class TA(Instructor):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.list_labs = []
        self.list_graders = []

    def get_lab_sections(self):
        return self.list_labs

    def add_lab_section(self, section):
        self.list_labs.append([section])
        return self.list_labs

    def remove_lab_section(self, section):
        if self.list_labs.__contains__(section):
            self.list_labs.remove(section)
            return self.list_labs
        else:
            return "Lab to be removed not found"

    def get_grader_courses(self):
        return self.list_graders

    def add_grader_course(self, course):
        self.list_graders.append(course)
        return self.list_graders

    def remove_grader_course(self, course):
        if self.list_graders.__contains__(course):
            self.list_graders.remove(course)
            return self.list_graders
        else:
            return "Grader to be removed not found"

    def __str__(self):
        pass

