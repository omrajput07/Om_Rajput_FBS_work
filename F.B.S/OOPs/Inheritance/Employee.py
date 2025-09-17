class Employee:
    def __init__(self,id,name,sal):
        self.eid = id
        self.ename = name
        self.esal = sal
    def ShowData(self):
        print("ID        :",self.eid)
        print("Name      :",self.ename)
        print("Salary    :",self.esal)

class SalesManager(Employee):
    def __init__(self,id,name,sal,targate,insentives):
        super().__init__(id,name,sal)
        self.tr = targate
        self.ince = insentives
    def ShowData(self):
        super().ShowData()
        print("Target    :",self.tr)
        print("Insentives:",self.ince)

sm1 = SalesManager(101,"Om",50000,10,12000)
sm1.ShowData()
