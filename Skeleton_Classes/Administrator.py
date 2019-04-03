from Skeleton_Classes.User import *


class Administrator(User):

    def __init__(self, username, password, Administrator, instructor, course,
                 lab_section, edit, create, assign, remove):
        self.username = username
        self.password = password
        self.Administrator= Administrator
        self.instructor = instructor
        self.course = course
        self.lab_section = lab_section
        self.create = create
        self.assign = assign
        self.edit = edit
        self.remove = remove



    def __str__(self):
        self.Administrator

    def get_instructor(self):
        return self.instructor

    def create_instructor(self, new_instructor ):
        self.create.instructor=new_instructor

    def remove_instructor(self, instructor_to_be_removed):
        self.remove.instructor=instructor_to_be_removed

    def edit_instructor(self, instructor_to_be_edit):
        self.edit.instructor=instructor_to_be_edit

    def assign_instructor_to_course(self, instructor_to_be_assign, course):
        self.assign.instructor= instructor_to_be_assign
        self.assign.course= course

    def get_courses(self):
        return self.course

    def create_course(self, new_course):
        self.create.course=new_course

    def remove_course(self, course_to_be_removed):
        self.remove.course= course_to_be_removed

    def get_public_contact_info(self):
        return self.info

    def get_lab_sections(self):
        return self.lab_section

    def create_lab_section(self, course, lab_section):
        self.create.course= course
        self.create.lab_section= lab_section

    def remove_lab_section(self, course, lab_section):
        self.remove.couse.lab_section= lab_section

    def assign_lab_section_TA(self, course, lab_section, TA_to_be_assign):
        self.assign.course= course
        self.assign.lab_section= lab_section
        self.assign.TA= TA_to_be_assign
