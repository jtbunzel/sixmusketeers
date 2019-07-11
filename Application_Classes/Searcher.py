from WebApplication.models import User, Course, LabSection
from itertools import chain


class Searcher:
    # gets the user object from username
    def get_user_object(self, username):
        if username == "None":
            return None

        user_object = User.objects.get(username=username)
        return user_object

    # get the course object from name
    def get_course_object(self, course_name):
        if course_name == "None":
            return None

        course_object = Course.objects.get(course_name=course_name)
        return course_object

    # search for users
    def searchuser(self, table_data):
        # key variables
        specific = table_data['strict_return']
        string_search = table_data['string']

        results = None

        # if the user wishes to search for a specific variable
        if specific is not None:
            if specific == "username":
                results = User.objects.filter(username__contains=string_search)
            elif specific == "name":
                results = User.objects.filter(name__contains=string_search)
            elif specific == "role":
                results = User.objects.filter(role__contains=string_search)
            elif specific == "email":
                results = User.objects.filter(email__contains=string_search)
            elif specific == "phone":
                results = User.objects.filter(phone__contains=string_search)
            elif specific == "all":  # get list of all users
                results = User.objects.all()

        else:
            # search all variables for the search string
            usernames = User.objects.filter(username__contains=string_search)
            names = User.objects.filter(name__contains=string_search)
            roles = User.objects.filter(role__contains=string_search)
            emails = User.objects.filter(email__contains=string_search)
            phones = User.objects.filter(phone__contains=string_search)

            # combine results
            results = (usernames | names | roles | emails | phones).distinct()

        return results


    def searchCourse(self, table_data):
        specific = table_data['strict_return']
        string_search = table_data['string']

        results = None

        # if the user wishes to search for a specific variable
        if specific is not None:
            if specific == "course_name":
                results = Course.objects.filter(course_name__contains=string_search)
            elif specific == 'course_code':
                # course code is integer
                try:
                    code = int(string_search)
                    results = Course.objects.filter(course_code__contains=code)
                except ValueError:
                    pass
            elif specific == 'course_instructor':
                # instructor must be a user object, grab matching one.
                try:
                    instructor = self.get_user_object(string_search)
                except User.DoesNotExist:
                    instructor = None

                results = Course.objects.filter(course_instructor=instructor)
            elif specific == 'all':  # return all courses
                results = Course.objects.all()

        else:
            course_names = Course.objects.filter(course_name__contains=string_search)
            course_code = Course.objects.none()
            course_instructor = User.objects.none()

            # course code is an integer
            try:
                code = int(string_search)
                course_code = Course.objects.filter(course_code__contains=code)
            except ValueError:
                pass
                # course instructor is an user object, grab possible results
            try:
                possible_instructors = User.objects.filter(username__contains=string_search)
                for i in possible_instructors:
                    instructor = self.get_user_object(i.username)
                    new_list = Course.objects.filter(course_instructor=instructor)

                    # combine list of all instructors
                    course_instructor = (course_instructor | new_list)
            except User.DoesNotExist:
                pass

            # combine lists of all results
            results = (course_names | course_code | course_instructor).distinct()

        return results


    def searchLabSection(self, table_data):
        specific = table_data['strict_return']
        string_search = table_data['string']

        results = None

        # if the user wishes to search for a specific variable
        if specific is not None:
            if specific == "lab_ta":
                # lab ta is an user object
                try:
                    ta = self.get_user_object(string_search)
                except User.DoesNotExist:
                    ta = None
                results = LabSection.objects.filter(lab_ta=ta)
            elif specific == 'lab_number':
                results = LabSection.objects.filter(lab_number__contains=string_search)
            elif specific == 'course':
                # course is a course object
                try:
                    course = self.get_course_object(string_search)
                except Course.DoesNotExist:
                    course = None
                results = LabSection.objects.filter(course=course)
            elif specific == 'all':
                results = LabSection.objects.all()  # return all labs

        else:
            lab_ta = User.objects.none()
            courses = Course.objects.none()
            try:
                possible_ta = User.objects.filter(username__contains=string_search)
                # grab all possible TAs
                for i in possible_ta:
                    ta = self.get_user_object(i.username)
                    new_list = LabSection.objects.filter(lab_ta=ta)

                    lab_ta = (lab_ta | new_list)
            except User.DoesNotExist:
                pass

            try:
                possible_course = Course.objects.filter(course_name__contains=string_search)
                # grab all possible courses
                for i in possible_course:
                    course = self.get_course_object(i.course_name)
                    new_list = LabSection.objects.filter(course=course)

                    courses = (courses | new_list)
            except LabSection.DoesNotExist:
                pass

            lab_number = LabSection.objects.filter(lab_number__contains=string_search)

            # combine lists of all results
            results = (lab_ta | lab_number | courses).distinct()

        return results
