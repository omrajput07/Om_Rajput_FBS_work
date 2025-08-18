a = input("Enter the a value:- ")
b = input("Enter the b value:- ")
for i in range(1,6):
    for j in range(1,6):
        if(j%2==0):
            print(a,end=' ')
        else:
            print(b,end=' ')
    print()