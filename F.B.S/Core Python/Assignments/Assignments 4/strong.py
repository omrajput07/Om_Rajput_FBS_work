#.WAP to check if given number Strong Number.
n =  int(input("Enter the num number to check strong:- "))
temp = n
fact_sum = 0

while(temp>0):
    d = temp % 10
    #print(d)
    temp //= 10
    fact = 1
    for i in range(1,d+1):
        fact *= i
    fact_sum += fact
#print(fact_sum)
if(n==fact_sum):
    print(f'{fact_sum}:=The number is stong')
else:
    print(f'{fact_sum}:=The number is not strong')