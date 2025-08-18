num = int(input("Enter the number to check armstrong number:- "))
temp = num
sum = 0
while(temp>0):
    d = temp % 10
    temp  //= 10
    sum += d ** 3
if(sum == num):
    print(f"This number is armstrong:- {num}")
else:
    print(f"This number is not armstrong:- {num} ")
