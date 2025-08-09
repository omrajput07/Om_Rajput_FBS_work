#3. WAP to print sum of series upto n.
num = int(input("Enter the number range to check sum of the number:- "))
sum = 0
for i in range(1,num+1):
    sum += i
print(f'the number:{num}:sum is:{sum}')