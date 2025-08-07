num = int(input("Enter the number to check factorial:- "))
i = 1
fact = 1
while(i<=num):
    fact *= i
    i += 1
print(f'factorial of number:{num},fact is:{fact}')