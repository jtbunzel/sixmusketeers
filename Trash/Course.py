class Course:
    course_name = ""
    course_instructor = None
    course_code = None
    lab_sections = []
    assigned_TA = None
    assigned_Grader = None

    def __init__(self, course_name, course_instructor, course_code):
        self.course_name = course_name
        self.course_instructor = course_instructor
        self.course_code = course_code
        self.lab_sections = []
        self.assigned_TA = None
        self.assigned_Grader = None

    def get_name(self):
        return self.course_name

    def set_name(self, new_course_name):
        self.course_name = new_course_name

    def get_instructor(self):
        return self.course_instructor

    def set_instructor(self, new_course_instructor):
        self.course_instructor = new_course_instructor

    def get_course_code(self):
        return self.course_code

    def set_course_code(self, new_course_code):
        self.course_code = new_course_code

    def get_lab_sections(self):
        return self.lab_sections

    def set_lab_section(self, new_lab_section):
        self.lab_sections.append(new_lab_section)

    def get_assigned_TA(self):
        return self.assigned_TA

    def set_assigned_TA(self, new_TA):
        self.assigned_TA = new_TA

    def get_graders(self):
        return self.assigned_Grader

    def set_graders(self, new_grader):
        self.assigned_Grader = new_grader
