from WebApplication.models import User, Course
from django.core.exceptions import ObjectDoesNotExist


class CourseCommandController:
    # edits the course with the new information
    def editCourse(self, course_name, newInfo):
        try:
            obj = Course.objects.get(course_name__iexact=course_name)
            # makes changes
            for key, value in newInfo.items():
                if value is not "":
                    setattr(obj, key, value)
            obj.save()
        # no matching course object
        except Course.DoesNotExist:
            return 'No course under this name'

        return "Course information has been successfully updated"

    # removes the course from the database
    def deleteCourse(self, course_name):
        try:
            current_course = Course.objects.get(course_name=course_name)
        except ObjectDoesNotExist:
            return "Course could not be found or does not exist."

        current_course.delete()

        return "Course has been deleted."


