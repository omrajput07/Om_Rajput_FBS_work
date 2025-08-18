num=int(input("Enter number :"))
i=1
sum=0

while(i<=num):
    fact=1
    j=1
    while(j<=i):
        fact=fact*j
        j=j+1
    sum=sum+fact
    i+=1

print("sum of factrorial from 1 to", num ,"is :" ,sum)


