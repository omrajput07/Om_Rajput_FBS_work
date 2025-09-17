class Car:
    
    def setdata(self,brand,model,color,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
    
    def showdata(self):
        data = f'Brand:{self.brand}\nModel:{self.model}\nColor:{self.color}\nPrice:{self.price}'
        return data
    
    def start(self):
        print("Car Started:")
    
    def stop(self):
        print("Car Stopped:")

c1 = Car()
c1.setdata("TATA","SAFARI","RED",3000000)
print(c1.showdata())
c1.start()
c1.stop()
print("---------------||------------------")
c2 = Car()
c2.setdata("TATA","NEXON","WHITE",2000000)
print(c2.showdata())
c2.start()
c2.stop()