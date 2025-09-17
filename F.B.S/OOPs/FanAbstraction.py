class Fan:
    def setData(self,brand,color,price):
        self.b = brand
        self.c = color
        self.p = price
    def display(self):
        print("Brand:",self.b)
        print("Color:",self.c)
        print("Price:",self.p)
obj1 = Fan()
obj1.setData("Godrej","White",2500)
obj1.display()

print("---------------||---------------")

obj2 = Fan()
obj2.setData("Bajaj","Black",2250)
obj2.display()