'''2. Write a program to calculate the sum of following series
where n is input by user.
1/1! + 2/2! + 3/3! + 4/4! + ... N/N!'''


num=int(input("Enter number :"))
i=1
sum=0

while(i<=num):
    fact=1
    j=1
    while(j<=i):
        fact=fact*j
        j=j+1
    sum = sum + (i / fact)
    i+=1
    

print(sum)