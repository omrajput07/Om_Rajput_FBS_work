class Area_of_Rectangle:
    def SetData(self,area,height,breath):
        # self.a = area
        self.l = height
        self.b = breath

    def Display(self):
        print("Length of Rectangle :",self.l)
        print("Breadth of Rectangle:",self.b)

    def area_of_rectangle(self):
        area = self.l * self.b
        return area


area = Area_of_Rectangle()
height = int(input("Enter the height:"))
breath = int(input("Enter the height:"))
area.Set_Data(height,breath)
print("Area of Rectangle",Area_of_Rectangle(area,height,breath))

    

