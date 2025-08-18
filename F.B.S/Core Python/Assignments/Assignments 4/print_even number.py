#.1. WAP to print all even numbers until n.
num = int(input("Enter the given number to check even number:- "))
for n in range(1,num+1):
        if(n%2==0):
            print(f'this is all even numbers:{n}')

