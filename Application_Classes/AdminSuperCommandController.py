from WebApplication.models import *
from django.core.exceptions import ObjectDoesNotExist


class SuperUserCommandController:
    user = User

    def deleteUser(self, targetUser):
        # Check for user logged in
        print('\ndeleting ' + targetUser)
        if self.user is None:
            return "You must be logged in"

        user_object = User.objects.filter(username__iexact=targetUser)
        role = user_object.get(username__iexact=targetUser).role.upper()
        print("\n")
        print(role)
        if role != "supervisor".upper():
            user_object.delete()
            response = targetUser + " deleted successfully."
            return response
        else:
            response = targetUser + " is a Supervisor and cannot be deleted."
            return response

    #   #Display public info for all users in database.
    def showAll(self):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

        #        #Check for Supervisor or Admin role
        #        if self.user.rank < 2:
        #            return "You do not have permission to use this command"

        #        If no entries in database return "Database is Empty"
        databaseCount = User.objects.count()
        if databaseCount < 0:
            return "Database is Empty"

        #        #For each user
        #        #Print all userInfo
        userInfo = ""
        for user in User.objects.all():
            userInfo += (
                    user.username + " " + user.name + " " + user.role + " " + user.phone + " " + user.email + " " + user.address + "\n")
        return userInfo

    def create(self, create_type, credential_array):
        types = ["TA", "Instructor", "Administrator"]
        if types.__contains__(create_type):
            if credential_array['username'] == "" or credential_array['password'] == "":
                return "Fields are missing or empty."
                print(credential_array)
                user1 = User()
                user1.name = credential_array['name']
                user1.username = credential_array['username']
                user1.password = credential_array['password']
                user1.role = credential_array['user_type']
                user1.email = credential_array['email']
                user1.phone = credential_array['phone']
                user1.address = credential_array['address']
                if User.objects.filter(username=user1.username).exists():
                    return "Username is already in use!"
                else:
                    user1.save()
                    return user1.username + " created as " + user1.role + "."
        elif create_type is "course":
            course1 = Course()
            course1.course_code = credential_array['course_code']
            if User.objects.filter(username=credential_array['course_instructor']).exists():
                course1.course_instructor = User.objects.filter(username=credential_array['course_instructor'])
            else:
                user_temp = User()
                user_temp.save()
                course1.course_instructor = user_temp
            course1.course_name = credential_array['course_name']
            print(credential_array)
            if Course.objects.filter(course_name=course1.course_name).exists() or Course.objects.filter(
                    course_code=course1.course_code).exists():
                return "course already exists!"
            else:
                course1.save()
                return course1.course_name + " created as " + course1.course_code + " , and assigned to" + str(
                    course1.course_instructor)
