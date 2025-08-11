num = int(input("Enter the number to check armstrong number:- "))
temp = num
for i in range(1,num+1):
    d = temp % 10
    temp // 10
    count += d
    print(count,d)
