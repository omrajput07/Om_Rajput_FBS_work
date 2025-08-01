number = int(input("Enter the the number:- "))
if(number == 0):
    print(f'number is neutral:{number}')
elif(number % 2 == 0):
    print(f'number is even:{number}')
else:
    print(f'number is odd:{number}')