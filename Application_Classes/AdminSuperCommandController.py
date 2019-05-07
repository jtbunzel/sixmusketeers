from WebApplication.models import User, Course, LabSection
from django.core.exceptions import ObjectDoesNotExist


class SuperUserCommandController:
    user = User()

    def deleteUser(self, targetUser):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

        user_obj = User.objects.get(username__iexact=targetUser)
        user_object = User.objects.get(username__iexact=targetUser).role

        user_to_str = str(user_object).upper()
        args = "SUPERVISOR".upper()
        response = "Delete User Malfunction"
        if user_to_str == args:
            response = targetUser + " is a Supervisor and cannot be deleted."
        else:
            user_obj.delete()
            response = targetUser + " deleted successfully."
        return response

    #   #Display public info for all users in database.
    def showAll(self):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

        #        #For each user
        #        #Print all userInfo
        userInfo = ""
        for user in User.objects.all():
            if user.name == "":
                return ""
            else:
                userInfo += (user.username + " " + user.name + " " + user.role + " " + user.phone + " " + user.email + " " + user.address + "\n")
        return userInfo

    def create(self, create_type, credential_array):
        print(credential_array)

        if create_type == "User":
            if credential_array['username'] == "" or credential_array['password'] == "":
                return "Fields are missing or empty."

            user1 = User()
            user1.name = credential_array['name']
            user1.username = credential_array['username']
            user1.password = credential_array['password']
            user1.role = credential_array['role']
            user1.email = credential_array['email']
            user1.phone = credential_array['phone']
            user1.address = credential_array['address']

            if User.objects.filter(username=user1.username).exists():
                return "Username is already in use!"
            else:
                user1.save()
                return user1.username + " created as " + user1.role + "."
        if create_type == "Course":
            course = Course()
            course.course_name = credential_array["course_name"]
            course.course_code = credential_array["course_code"]
            print(credential_array["course_instructor"])
            if credential_array["course_instructor"] is not None:
                course.course_instructor = credential_array["course_instructor"]

            if Course.objects.filter(course_name=course.course_name).exists():
                return "Course is already in use!"
            else:
                course.save()

            return course.course_name + " created as " + course.course_code + "."

        elif create_type == "Lab":
            lab = LabSection()
            if credential_array["lab_ta"] is not None:
                lab.lab_ta = credential_array["lab_ta"]
            lab.lab_number = credential_array["lab_number"]
            if credential_array["course_name"] is not None:
                lab.course = credential_array["course_name"]

            if LabSection.objects.filter(lab_number=lab.lab_number).exists():
                return "Lab Section has already been created!"
            else:
                lab.save()

            return " Lab section " + lab.lab_number + " created for " + lab.course.course_name + "."