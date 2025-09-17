class Shoes:
    def setDAta(self,brand,color,size,price):
        self.b = brand
        self.c = color
        self.p = price
        self.s = size
    def display(self):
        print("Brand:",self.b)
        print("Color:",self.c)
        print("Price:",self.p)
        print("Size :",self.s)

obj1 = Shoes()
obj1.setDAta("Campus","Navay_blue",10,2575)
obj1.display()

print("-------------||-------------")

obj2 = Shoes()
obj2.setDAta("Puma","White",10,2500,)
obj2.display()