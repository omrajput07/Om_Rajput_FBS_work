#.WAP to check if given number is Perfect Number.
n = int(input("Enter the number check the perfect or not:- "))
sum = 0
for num in range(1,n):
    if(n%num==0):
        sum += num
if(sum == n):
    print(f'this is perfect number:- {num}')
else:
    print(f'This not perfect number:- {num}')