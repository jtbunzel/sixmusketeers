from Skeleton_Classes.User import *


class Administrator(User):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.Administrator= Administrator
        self.rank = 2



    def __str__(self):
        self.Administrator

    def get_instructor(self):
        return self.instructor

    def create_instructor(self, new_instructor ):
        self.CommandController.create().instructor=new_instructor

    def remove_instructor(self, instructor_to_be_removed):
        self.CommandController.delete().instructor=instructor_to_be_removed

    def edit_instructor(self, instructor_to_be_edit):
        self.CommandController.edit().instructor=instructor_to_be_edit

    def assign_instructor_to_course(self, instructor_to_be_assign, course):
        self.CommandController.assign().instructor= instructor_to_be_assign
        self.CommandController.assign().course= course

    def get_courses(self):
        return self.course

    def create_course(self, new_course):
        self.CommandController.create().course=new_course

    def remove_course(self, course_to_be_removed):
        self.CommandController.delete().course= course_to_be_removed

    def get_public_contact_info(self):
        return self.info

    def get_lab_sections(self):
        return self.lab_section

    def create_lab_section(self, course, lab_section):
        self.CommandController.create().course= course
        self.CommandController.create().lab_section= lab_section

    def remove_lab_section(self, course, lab_section):
        self.course = course
        course.CommandController.delete()._lab_section= lab_section

    def assign_lab_section_TA(self, course, lab_section, TA_to_be_assign):
        self.CommandController.assign().course= course
        self.CommandController.assign().lab_section= lab_section
        self.CommandController.assign().TA= TA_to_be_assign
