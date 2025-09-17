from person import Person
class Student(Person):
    def __init__(self, nm, age, add, roll, branch):
        super().__init__(nm, age, add)
        self.roll = roll
        self.branch = branch
    def Showdata(self):
        super().Showdata()
        print(f'Roll   :{self.roll}\nBranch :{self.branch}')

num_of_student = int(input("Enter the number of student: "))
for i in range(num_of_student):
    print("Number of student:",i+1)
    nm = input("Enter the Name: ")
    age = int(input("Enter the student age: "))
    add = input("Enter the address: ")
    roll = int(input("Enter the roll number: "))
    branch = input("Enter the course Name: ")
    stud1 = Student(nm, age, add, roll, branch)
    stud1.Showdata()
    print("------------------||------------------")
    
    # stud2 = Student("Sarvesh",22,"Shirpur",49,"MCA")
    # stud2.Showdata()
        