from django.test import TestCase
from Application_Classes.CourseCommandController import CourseCommandController


class TestCourseCommandController(TestCase):
    cmd = CourseCommandController()

    def setUp(self):
        pass

    def test_create_course(self):
        cmd = CourseCommandController()
        action = cmd.createCourse("Intro to Comp Sci", "007", "Jojo")
        result = "Successfully created a new Course"
        self.assertEqual(result, action)

    def test_edit_course(self):
        cmd = CourseCommandController()
        cmd.createCourse("Intro to Comp Sci", "007", "Jojo")
        action = cmd.editCourse("Intro to Comp Security", "008", "Billy")
        result = "Course has been edited."
        self.assertEqual(result, action)

    def test_delete_course(self):
        cmd = CourseCommandController()
        cmd.createCourse("Intro to Comp Sci", "007", "Jojo")
        action = cmd.deleteCourse("007")
        result = "Course has been deleted."
        self.assertEqual(result, action)