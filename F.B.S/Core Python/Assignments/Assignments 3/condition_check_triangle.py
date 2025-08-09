#.Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("Enter the side 1:- "))
b = int(input("Enter the side 2:- "))
c = int(input("Enter the side 3:- "))
if((a==b)and(b==c)and(a==c)):
    print("The Triangle is equilateral")
elif((a==b)or(b==c)or(a==c)):
    print("The Triangle is isoscelesl")
else:
    print("The Triangle is scalene")