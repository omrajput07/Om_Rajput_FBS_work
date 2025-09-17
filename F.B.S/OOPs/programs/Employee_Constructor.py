class Employee:
    def __init__(self,id,name,sal,dept):
        self.eid = id
        self.ename = name
        self.esal = sal
        self.dept = dept
    
    def total_salary(self):
        ta = self.esal * 7 // 100
        hra = self.esal * 10 // 100
        pf = self.esal  * 12 // 100
        total_sal = (self.esal + ta + hra - pf)
        print("Id of the Employee    :",self.eid)
        print("Name of Employe       :",self.ename)
        print("Salary of Employe     :",total_sal)
        print("Department of Employee:",self.dept)
         
        return total_sal
    def __del__(self):
        print("This is destructor")

e1 = Employee(101,"Om",45000,"Software_Devloper")
e1.total_salary()
print("-----------||-----------")
e2 = Employee(102,"Sarvesh",55000,"Data Engineear")
e2.total_salary()

# final_detail = ()


# __init__ That is constructor that are call automatically ok.