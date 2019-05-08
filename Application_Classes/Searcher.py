from WebApplication.models import User, Course, LabSection
from itertools import chain


class Searcher:
    user = User()


    def get_user_object(self, username):
        if username == "None":
            return None

        user_object = User.objects.get(username=username)
        return user_object

    def get_course_object(self, course_name):
        if course_name == "None":
            return None

        course_object = Course.objects.get(course_name=course_name)
        return course_object

    def searchuser(self, table_data):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"
        specific = table_data['strict_return']
        string_search = table_data['string']

        results = None

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
            elif specific == "all":
                results = User.objects.all()

        else:
            usernames = User.objects.filter(username__contains=string_search)
            names = User.objects.filter(name__contains=string_search)
            roles = User.objects.filter(role__contains=string_search)
            emails = User.objects.filter(email__contains=string_search)
            phones = User.objects.filter(phone__contains=string_search)

            results = (usernames | names | roles | emails | phones).distinct()

        return results

    def clean_query(self, queryname):
        strr = []
        lists = (User.objects.filter(username=queryname).all())
        strr.append("Username: " + lists.get().username + " ")
        strr.append("Full name: " + lists.get().name + " ")
        strr.append("Email: " + lists.get().email + " ")
        strr.append("Address: " + lists.get().address + " ")
        strr.append("Phone: " + lists.get().phone + " ")

        print(strr)
        return strr

    def searchCourse(self, table_data):
        if self.user is None:
            return "Your must be logged in"

        specific = table_data['strict_return']
        string_search = table_data['string']

        results = None

        if specific is not None:
            if specific == "course_name":
                results = Course.objects.filter(course_name__contains=string_search)
            elif specific == 'course_code':
                try:
                    code = int(string_search)
                    results = Course.objects.filter(course_code__contains=code)
                except ValueError:
                    courseCode = ""
            elif specific == 'course_instructor':
                try:
                    instructor = self.get_user_object(string_search)
                except User.DoesNotExist:
                    instructor = None
                results = Course.objects.filter(course_instructor=instructor)
            elif specific == 'all':
                results = Course.objects.all()

        else:
            courseNames = Course.objects.filter(course_name__contains=string_search)
            courseCode = Course.objects.none()
            courseInstructor = User.objects.none()
            try:
                code = int(string_search)
                courseCode = Course.objects.filter(course_code__contains=code)
            except ValueError:
                pass
            try:
                possible_instructors = User.objects.filter(username__contains=string_search)
                for i in possible_instructors:
                    instructor = self.get_user_object(i.username)
                    new_list = Course.objects.filter(course_instructor=instructor)

                    courseInstructor = (courseInstructor | new_list)
            except User.DoesNotExist:
                pass

            results = (courseNames | courseCode | courseInstructor).distinct()

        return results

    def searchLabSection(self, table_data):
        if self.user is None:
            return "Your must be logged in"

        specific = table_data['strict_return']
        string_search = table_data['string']

        results = None

        if specific is not None:
            if specific == "lab_ta":
                try:
                    ta = self.get_user_object(string_search)
                except User.DoesNotExist:
                    ta = None
                results = LabSection.objects.filter(lab_ta=ta)
            elif specific == 'lab_number':
                results = LabSection.objects.filter(lab_number__contains=string_search)
            elif specific == 'course':
                try:
                    course = self.get_course_object(string_search)
                except Course.DoesNotExist:
                    course = None
                results = LabSection.objects.filter(course=course)
            elif specific == 'all':
                results = LabSection.objects.all()

        else:
            labTa = User.objects.none()
            courses = Course.objects.none()
            try:
                possible_ta = User.objects.filter(username__contains=string_search)
                for i in possible_ta:
                    ta = self.get_user_object(i.username)
                    new_list = LabSection.objects.filter(lab_ta=ta)

                    labTa = (ta | new_list)
            except User.DoesNotExist:
                pass

            try:
                possible_course = Course.objects.filter(course_name__contains=string_search)
                for i in possible_course:
                    course = self.get_course_object(i.course_name)
                    new_list = LabSection.objects.filter(course=course)

                    courses = (course | new_list)
            except LabSection.DoesNotExist:
                pass

            labNumber = LabSection.objects.filter(lab_number__contains=string_search)

            results = (labTa | labNumber | courses).distinct()

        return results
