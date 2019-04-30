from WebApplication.models import User
from WebApplication.models import LabSection
from itertools import chain


class Searcher:
    user = User

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

    def searchLabSection(self, table_data):
       #check if user is logged in
        if self.user is None:
            return "You must be logged in"
        specific = table_data['strict_return']
        string_search = table_data['string']

        results = None

        if specific is not None:

           if specific == "lab_tas":
               results= LabSection.objects.filter(lab_ta_contains=string_search)
           elif specific == "lab_number":
               results= LabSection.objects.filter(lab_number_contains=string_search)
           elif specific == "course":
               results= LabSection.objects.filter(course_contains=string_search)

        else:
           lab_tas =  LabSection.objects.filter(lab_ta_contains=string_search)
           lab_number = LabSection.objects.filter(lab_number_contains=string_search)
           course = LabSection.objects.filter(course_contains=string_search)

           results=(lab_tas | lab_number | course)

        return results



