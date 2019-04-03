from Skeleton_Classes.User import *


class Administrator(User):

    def __init__(self, username, password):
        self.username=username
        self.password=password

    def __str__(self):
        pass

    def get_instructor(self):
        return self.instructor

    def create_instructor(self, new_instructor ):
        self.instructor=new_instructor

    def remove_instructor(self, instructor_to_be_removed):
        self.instructor=instructor_to_be_removed

    def edit_instructor(self, instructor_to_be_edit):
        self.instructor=instructor_to_be_edit

    def assign_instructor_to_course(self, instructor_to_be_assign, course):
        pass

    def get_courses(self):
        return self.course

    def create_course(self, new_course):
        self.course=new_course

    def remove_course(self, course_to_be_removed):
        pass

    def get_public_contact_info(self):
        return self.info

    def get_lab_sections(self):
        return ""

    def create_lab_section(self, course, section):
        pass

    def remove_lab_section(self, course, section):
        pass

    def assign_lab_section_TA(self, lab_section, TA_to_be_assign):
        pass
