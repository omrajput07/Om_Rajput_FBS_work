class Pen:
    def setDAta(self,brand,pen_body_color,ink_color,price):
        self.b = brand
        self.c = pen_body_color
        self.i = ink_color
        self.p = price
        
    def display(self):
        print("Brand     :",self.b)
        print("Body_Color:",self.c)
        print("Ink_Color :",self.i)
        print("Price     :",self.p)
        

obj1 = Pen()
obj1.setDAta("Cello","Gray","Blue",10)
obj1.display()

print("-------------||-------------")

obj2 = Pen()
obj2.setDAta("Writometer","Navy_bleu","GEl",20)
obj2.display()