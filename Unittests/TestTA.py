import unittest


class testTa(unittest.Testcase):
    def setup(self):
        self.TA = TA('John', 'Doe')
        self.TA.add_lab_section('801', 'John', 'Doe')

    def test_constructor(self):
        pass

    def get_lab_sections(self):
        pass

    def add_lab_section(self, course, section):
        pass

    def remove_lab_section(self, course, section):
        pass

    def get_grader_courses(self):
        pass

    def add_grader_course(self, course):
        pass

    def remove_grader_course(self, course):
        pass

    def test_view_public_info(self):
        result = a.access(self)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
