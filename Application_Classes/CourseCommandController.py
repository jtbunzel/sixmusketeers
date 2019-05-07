from WebApplication.models import User, Course
from django.core.exceptions import ObjectDoesNotExist


class CourseCommandController:
    user = User()

    def editCourse(self, course_name, newInfo):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"
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
        currentCourse = Course()
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"
        try:
            currentCourse = Course.objects.get(course_name__iexact=course_name)
        except ObjectDoesNotExist:
            return "Course could not be found or does not exist."

        currentCourse.delete()

        return "Course has been deleted."


