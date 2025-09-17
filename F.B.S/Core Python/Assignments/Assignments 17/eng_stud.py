from student_main import Student
class eng_student(Student):
    def __init__(self, stud_id=0, stud_nm="", age=0, marks=0, perce=0,Branch="",Internal_marks=0):
        super().__init__(stud_id, stud_nm, age, marks, perce)
        self.branch = Branch
        self.imarks = Internal_marks
