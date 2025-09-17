# Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method

class Student:
    def __init__(self,stud_id=0,stud_nm="",age=0,marks=0,perce=0):
        self.id = stud_id
        self.name = stud_nm
        self.age = age
        self.marks = marks
        self.per = perce
    
    def Accept_percentage(self):
        self.id = int(input("Enter the Id  of student: "))
        self.name = input("Enter the name of the student: ")
        self.age = int(input("Enter the Age of the student: "))
        self.marks = int(input("Enter the Total  Marks of the student: "))
        self.per = self.marks / 500 * 100
        
    def Showdata(self):
        print(self)
    
    
    def calculate_rank(self):
        if self.per >= 90:
            return "A"
        elif self.per >= 85:
            return "B"
        elif self.per >= 80:
            return "C"
        elif 60>self.per >= 70:
            return "D"
        else:
            return "Average"

    def __str__(self):
        return (f"Stu_id    : {self.id}\n"
                f"Name      : {self.name}\n"
                f"Age       : {self.age}\n"
                f"Percentage: {self.per:.2f}\n"
                f"Stud_Rank : {self.calculate_rank()}")
       
        
student1 = Student()
student1.Accept_percentage()
print("------------------||------------------")
student1.Showdata()
student1.calculate_rank()

        
