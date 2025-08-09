#WAP to check if a given number is prime number or not.
n = int (input("Enter the number to check prime or not:- "))
for num in range(2,n//2+1):
    if(n%num==0):
        print(f'This is not prime number:-{num}')
        break
else:
     print(f'This is prime number:- {num}')
