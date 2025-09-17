class Laptop:
    def setDAta(self,brand,color,processor,price,generation):
        self.b = brand
        self.c = color
        self.p = processor
        self.r = price
        self.g = generation
    def display(self):
        print("Brand     :",self.b)
        print("Color     :",self.c)
        print("Processor :",self.p)
        print("Price     :",self.r)
        print("Generation:",self.g)

obj1 = Laptop()
obj1.setDAta("Samsung","Gray","i7",67000,'13th')
obj1.display()

print("-------------||-------------")

obj2 = Laptop()
obj2.setDAta("Acer","Golden","i5",57000,'12th')
obj2.display()