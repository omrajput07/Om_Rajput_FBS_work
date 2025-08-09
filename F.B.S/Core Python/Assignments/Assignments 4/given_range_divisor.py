#.print all numbers in a range divisible by a given number.
n  = int(input("Enter the number range:- "))
devisor = int(input("Enter the devisor:- "))
for num in range(1,n+1):
    if(num % devisor == 0):
        print(f'your range is divisible numbers:{num}')