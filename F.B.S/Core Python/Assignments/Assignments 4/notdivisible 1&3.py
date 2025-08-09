#.WAP to print all integers upto n that aren’t divisible by 2 and 3.

n = int(input("Enter the number :- "))
for num in range(1,n+1):
    if(num %2 != 0 and num %3 != 0):
        print(num)