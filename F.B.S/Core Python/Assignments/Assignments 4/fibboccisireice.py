num = int(input("Enter the number to give fibbonacci series:- "))
a = -1
b = 1
for i in range(1,num+1):
    c = a + b
    print(c)
    a = b
    b = c
    
