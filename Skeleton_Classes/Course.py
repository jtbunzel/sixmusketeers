from Skeleton_Classes.LabSection import *


class Course:
    def __init__(self, course_name, course_instructor="n/a", course_number="n/a"):
        self.course_name = course_name
        self.course_instructor = course_instructor
        self.course_code = course_number
        self.lab_sections = ["n/a"]
        self.list_assigned_TA = []
        self.list_graders = []

    def get_name(self):
        return self.course_name

    def set_name(self, new_course_name):
        self.course_name = new_course_name

    def get_instructor(self):
        return self.course_instructor

    def set_instructor(self, new_course_instructor):
        self.course_instructor = new_course_instructor

    def get_course_code(self):
        return self.course_code

    def set_course_code(self, new_course_code):
        self.course_code = new_course_code

    def get_lab_sections(self):
        return self.lab_sections

    def set_lab_section(self, new_lab_section):
        self.lab_sections.append(new_lab_section)

    def get_assigned_TA(self):
        return self.list_assigned_TA

    def set_assigned_TA(self, new_TA):
        self.list_assigned_TA.append(new_TA)

    def get_graders(self):
        return self.get_graders()

    def set_graders(self, new_grader):
        self.list_graders.append(new_grader)
