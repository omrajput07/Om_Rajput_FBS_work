# 1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    def __init__(self,bid,bname,bprice,bAthour="APJ"):
        self.i = bid
        self.n = bname
        self.p = bprice
        self.a = bAthour

    def showbook(self):
        print("Book ID         :",self.i)
        print("Book Name       :",self.n)
        print("Book Price      :",self.p)
        print("Book Author Name:",self.a)
    def __del__(self):
        print("This is Destructor")

book1 = Book(3001,"Python",450,"Xyz")
book1.showbook()
del book1
print("---------||---------")
book2 = Book(3002,"Java",255)
book2.showbook()