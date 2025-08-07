num = int(input("Enter the number to get seprate and sum:- "))
temp = num
sum = 0
while(temp>0):
    d = temp % 10
    print(d)
    temp //= 10
    sum += d
    print(sum)
    