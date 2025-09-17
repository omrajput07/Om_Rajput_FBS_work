class Charger:
    def setDAta(self,brand,color,price,Capacity):
        self.b = brand
        self.c = color
        self.p = price
        self.v = Capacity
    def display(self):
        print("Brand     :",self.b)
        print("Color     :",self.c)
        print("Price     :",self.p)
        print("Voltage   :",self.v)

obj1 = Charger()
obj1.setDAta("Samsung","White",2250,'25w')
obj1.display()

print("-------------||-------------")

obj2 = Charger()
obj2.setDAta("Realme","Red",1250,'65w')
obj2.display()