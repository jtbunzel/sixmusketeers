from Skeleton_Classes.User import *


class Supervisor(User):

    def __init__(self, username, password):
        pass

    def __str__(self):
        pass

    def get_administrator(self):
        return " "

    def create_administrator(self, new_administrator):
        pass

    def remove_administrator(self, administrator_to_be_removed):
        pass

    def edit_administrator(self, administrator_to_be_edited):
        pass

    def get_instructor(self):
        return ""

    def create_instructor(self, new_instructor ):
        pass

    def remove_instructor(self, instructor_to_be_removed):
        pass

    def edit_instructor(self, instructor_to_be_edit):
        pass

    def assign_instructor_to_course(self, instructor_to_be_assign, course):
        pass

    def get_courses(self):
        return " "

    def create_course(self, new_course):
        pass

    def remove_course(self, course_to_be_removed):
        pass

    def get_public_contact_info(self):
        return " "

    def get_lab_sections(self):
        return " "

    def create_lab_section(self, course, section):
        pass

    def remove_lab_section(self, course, section):
        pass

    def assign_lab_section_TA(self, lab_section, TA_to_be_assign):
        pass