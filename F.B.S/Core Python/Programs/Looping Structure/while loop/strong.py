num = int(input("Enter the number:- "))
temp = num
sum = 0
while(temp>0):
    d = temp % 10
   # print(d)
    temp = temp // 10
    i = 1
    fact =1
    while(i<=d):
        fact *= i
        i += 1
    sum += fact
    print(fact)
if(sum == num):
    print(f'this is strong number')
else:
    print(f'this is not strong number')

