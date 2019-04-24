class Course:
    def __init__(self, course_name, course_instructor="n/a", course_number="n/a"):
        self.course_code = course_number
        self.course_name = course_name
        self.course_instructor = course_instructor
        self.lab_name = ["n/a"]

    def get_name(self):
        return self.course_name

    def get_type(self):
        return self.course_type

    def edit_course_instructor(self, instructor):
        pass

    def get_instructor(self):
        return self.course_instructor

    def get_number(self):
        return self.course_code

    # adds an empty lab section, further steps needed
    # further steps needed to finish lab assignment from
    # class Lab_section#
    def add_lab(self, lab_name):
        # create an instance of lab
        pass
