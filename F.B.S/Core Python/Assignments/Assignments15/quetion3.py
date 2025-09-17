# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowShirt

class Shirt:
    def __init__(self,sid=1002,sname="Tshirt",price=250,size="M",stype='Formal'):
        self.i = sid
        self.n = sname
        self.p = price
        self.s = size
        self.t = stype

    def ShowShirt(self):
        print("Shirt ID         :",self.i)
        print("Shirt Name       :",self.n)
        print("Shirt Price      :",self.p)
        print("Shirt Size       :",self.s)
        print("Shirt type       :",self.t)
    def __del__(self):
        print("This is Destructor")

book1 = Shirt(3001,"Simple",500,"L","Casual")
book1.ShowShirt()
del book1
print("---------||---------")
book2 = Shirt()
book2.ShowShirt()