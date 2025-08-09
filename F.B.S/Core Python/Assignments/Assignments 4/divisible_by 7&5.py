#. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
n = int(input("Enter the number:- "))
for num in range(1,n+1):
    if(num%5==0 and num%7==0):
        print(num)