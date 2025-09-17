# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. Showproduct

class Product:
    def __init__(self,bid=10050,pname="spare_part",bprice=1500,product_Quality= "best"):
        self.i = bid
        self.n = pname
        self.p = bprice
        self.q = product_Quality

    def showProduct(self):
        print("Product ID         :",self.i)
        print("Product Name       :",self.n)
        print("Product Price      :",self.p)
        print("Product Quality    :",self.q)
    def __del__(self):
        print("This is Destructor")

Product1 = Product(3001,"Chair",450,"Average")
Product1.showProduct()
del Product1
print("---------||---------")
Product2 = Product()
Product2.showProduct()