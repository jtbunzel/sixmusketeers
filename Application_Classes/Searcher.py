from WebApplication.models import User, Course, LabSection
from itertools import chain


class Searcher:
    user = User

    def get_user_object(self, username):
        print("object: " + username)
        if username == "None":
            return None

        user_object = User.objects.get(username__iexact=username)
        return user_object

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
                    results = Course.objects.filter(course_code=code)
                except ValueError:
                    courseCode = ""
            elif specific == 'course_intructor':
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
            courseInstructor = Course.objects.none()
            try:
                code = int(string_search)
                courseCode = Course.objects.filter(course_code=code)
            except ValueError:
                pass
            try:
                instructor = self.get_user_object(string_search)
                courseInstructor = Course.objects.filter(course_instructor=instructor)
            except User.DoesNotExist:
                pass

            results = (courseNames | courseCode | courseInstructor).distinct()

        return results