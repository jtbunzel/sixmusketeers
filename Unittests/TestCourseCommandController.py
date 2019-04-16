from django.test import TestCase
from WebApplication.CourseCommandController import CourseCommandController


class TestCourseCommandController(TestCase):
    cmd = CourseCommandController()

    def setUp(self):
        pass

    def test_create_course(self):
        cmd = CourseCommandController()
        action = cmd.createCourse("Intro to Comp Sci", "Jojo", "007")
        result = "Successfully created a new Course"
        self.assertEqual(result, action)

    def test_edit_course(self):
        cmd = CourseCommandController()
        cmd.createCourse("Intro to Comp Sci", "Jojo", "007")
        action = cmd.editCourse("001", "Intro to Comp Security", "Billy", "008")
        result = "Course has been edited."
        self.assertEqual(result, action)

    def test_delete_course(self):
        cmd = CourseCommandController()
        cmd.createCourse("Intro to Comp Sci", "Jojo", "007")
        action = cmd.deleteCourse("007")
        result = "Course has been deleted."
        self.assertEqual(result, action)