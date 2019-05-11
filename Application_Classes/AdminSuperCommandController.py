from WebApplication.models import User, Course, LabSection


class SuperUserCommandController:
    def deleteUser(self, targetUser):
        user_obj = User.objects.get(username=targetUser)
        user_object = User.objects.get(username=targetUser).role

        user_to_str = str(user_object).upper()  # big letters
        response = ""

        # check if the user is a supervisor
        if user_to_str != "SUPERVISOR":
            user_obj.delete()
        else:
            response = "User is a supervisor and cannot be deleted"

        return response

    def create(self, create_type, credential_array):
        # creation type is  user
        if create_type == "User":
            # username and password are required
            if credential_array['username'] == "" or credential_array['password'] == "":
                return "Fields are missing or empty."

            user = User()
            user.name = credential_array['name']
            user.username = credential_array['username']
            user.password = credential_array['password']
            user.role = credential_array['role']
            user.email = credential_array['email']
            user.phone = credential_array['phone']
            user.address = credential_array['address']

            if User.objects.filter(username=user.username).exists():
                return "Username is already in use!"
            else:
                user.save()

            # style return
            if user.role:
                response = "User " + user.username + " created as " + user.role + "."
            else:
                response = "User " + user.username + " created."

            return response

        # creation type is a course
        if create_type == "Course":
            course = Course()
            course.course_name = credential_array["course_name"]
            course.course_code = credential_array["course_code"]

            # set an instructor if there was one selected
            if credential_array["course_instructor"] is not None:
                course.course_instructor = credential_array["course_instructor"]

            # check for existing course
            if Course.objects.filter(course_name=course.course_name).exists():
                return "Course is already exists!"
            else:
                course.save()

            # style return
            if course.course_code:
                response = "Course " + course.course_name + " created with code " + course.course_code + "."
            else:
                response = "Course " + course.course_name + " created."

            return response

        # creation type is a lab
        elif create_type == "Lab":
            lab = LabSection()

            # if there is a ta selected, use it
            if credential_array["lab_ta"] is not None:
                lab.lab_ta = credential_array["lab_ta"]

            lab.lab_number = credential_array["lab_number"]

            # if there is a course selected, use it
            if credential_array["course_name"] is not None:
                lab.course = credential_array["course_name"]

            lab.save()

            # style return
            if lab.course:
                response = "Lab section " + lab.lab_number + " created for " + lab.course.course_name + "."
            else:
                response = "Lab section " + lab.lab_number + " created."

            return response
