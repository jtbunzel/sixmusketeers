from .models import User, Course
from django.core.exceptions import ObjectDoesNotExist


class UserCommandController:
    user = User()

    def editCourse(self, course_name, course_instructor, course_code):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

#        #Check for Supervisor or Admin role
        if self.user.rank < 2:
            return "You do not have permission to use this command"

#        Check if course exists
#        if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist.
        try:
            currentCourse = Course.objects.filter(course_name=course_name)
        except ObjectDoesNotExist:
            print("Course could not be found or does not exist.")

#       #If Course Name not blank edit Course Name
        if course_name != '':
            currentCourse.course_name = course_name

#       #If Course Code not blank edit Course Code
        if course_code != '':
            currentCourse.course_code = course_code

#       #If Course Instructor not blank edit Course Instructor
        if course_instructor != '':
            currentCourse.course_instructor = course_instructor

        currentCourse.save()

        return "Course has been edited."
