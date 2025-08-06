num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print(f"Number 1 is greatest: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Number 2 is greatest: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"Number 3 is greatest: {num3}")
else:
    print("There is a tie between two or more numbers.")