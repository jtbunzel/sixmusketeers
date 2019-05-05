from WebApplication.models import User, Course
from django.core.exceptions import ObjectDoesNotExist


class CourseCommandController:
    user = User()

    def editCourse(self, course_name, newInfo):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

#        try:
#            currentCourse = Course.objects.get(course_name__iexact=course_name)
#        except ObjectDoesNotExist:
#            print("Course could not be found or does not exist.")

#        currentCourse.course_name = newInfo['course_name']
#        currentCourse.course_code = newInfo['course_code']
#        currentCourse.course_instructor = newInfo['course_instructor']

#        currentCourse.save()

#        return "Course has been edited."
        try:
            obj = Course.objects.get(course_name__iexact=course_name)
            for key, value in newInfo.items():
                if value is not "":
                    setattr(obj, key, value)
            obj.save()
        except Course.DoesNotExist:
            return 'No course under this name'

        return "Course information has been successfully updated"


    def deleteCourse(self, course_name):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

#        #Check for Supervisor or Admin role  **Editing out for testing purposes**
#        if self.user.rank < 2:
#            return "You do not have permission to use this command"

#        Check if course exists
#        if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist.
        try:
            currentCourse = Course.objects.filter(course_name__iexact=course_name)
        except ObjectDoesNotExist:
            print("Course could not be found or does not exist.")

        currentCourse.delete()

        return "Course has been deleted."


