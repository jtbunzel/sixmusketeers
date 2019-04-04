from Skeleton_Classes.User import *

class Supervisor(User):

    def __init__(self, username, password, supervisor):
        self.login.username = username
        self.login.password = password
        self.supervisor_name = supervisor
        self.rank= 1

    def __str__(self):
        self.supervisor_name

    def get_administrator(self):
        return self.administrator

    def create_administrator(self, new_administrator):
        self.create.administrator= new_administrator

    def remove_administrator(self, administrator_to_be_removed):
        self.remove.administrator= administrator_to_be_removed

    def edit_administrator(self, administrator_to_be_edited):
        self.edit.administrator= administrator_to_be_edited

    def get_instructor(self):
        return self.instructor

    def create_instructor(self, new_instructor ):
        self.create.instructor= new_instructor

    def remove_instructor(self, instructor_to_be_removed):
        self.remove.instructor= instructor_to_be_removed

    def edit_instructor(self, instructor_to_be_edit):
        self.edit.instructor= instructor_to_be_edit

    def assign_instructor_to_course(self, instructor_to_be_assign, course):
        self.assign.course= course
        self.assign.instructor= instructor_to_be_assign

    def get_courses(self):
        return self.course

    def create_course(self, new_course):
        self.create.course= new_course

    def remove_course(self, course_to_be_removed):
        self.remove.course= course_to_be_removed

    def get_public_contact_info(self):
        return self.info

    def get_lab_sections(self):
        return self.lab_section

    def create_lab_section(self, course, lab_section):
        self.create.course=course
        self.create.lab_section= lab_section

    def remove_lab_section(self, course, section):
        self.remove.course=course
        self.remove.lab_section=section

    def assign_lab_section_TA(self, course, lab_section, TA_to_be_assign):
        self.assign.course = course
        self.assign.TA = TA_to_be_assign
        self.assign.lab_section=lab_section
