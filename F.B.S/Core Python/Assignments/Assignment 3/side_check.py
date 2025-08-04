a = int(input("Enter the side 1:- "))
b = int(input("Enter the side 2:- "))
c = int(input("Enter the side 3:- "))
if((a+b>c)and(b+c>a)and(a+c>b)):
    print('triangle is valid:')
else:
    print('triangle is invalid:')