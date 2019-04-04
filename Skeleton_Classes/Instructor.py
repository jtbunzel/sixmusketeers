from typing import List, Any

# import Skeleton_Classes
from Skeleton_Classes.MOCK_user import *  # mock because testing classes is independent
from Skeleton_Classes.User import *
from Skeleton_Classes.Course import *



class Instructor(User):

    def __init__(self, username, password):
        """
        :type username: string
        :type password: string
        """
        self.username=username
        self.password=password
        self.courses: List[Course]=[]

    def get_courses(self):
        str_courses=""
        for i in self.courses:
            str_courses+=i
            str_courses+="\n"
        return str_courses

    def add_course(self, new_course=None):
        self.courses.append(new_course)

    def remove_course(self, course_to_be_removed):
        if self.courses.__contains__(course_to_be_removed):
            self.courses.remove(course_to_be_removed)
        else:
            return ("no course to remove")

    def get_public_contact_info(self):
        if self.username is not None:
            return self.get_full_name() + '\n' + self.get_email() + '\n' + self.get_phone_number()
        else:
            return None
