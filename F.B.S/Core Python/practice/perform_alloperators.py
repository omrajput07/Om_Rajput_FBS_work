num1 = int(input("Enter the number 1:- "))
num2 = int(input("Enter the number 2:- "))
operator = input("Choose an operation (+, -, *, /, %): ")
if(operator == '+'):
    result =num1 + num2
    print(f'result is:{result}')
elif(operator == '-'):
    result =num1 - num2
    print(f'result is:{result}')
elif(operator == '*'):
    result =num1 * num2
    print(f'result is:{result}')
elif(operator == '%'):
    if(operator != 0):
        result =num1 % num2
        print(f'result is:{result}') 
    else:
        print("Error: modulus by zero is not allowed.")
else:
    print("Invalid operator! Please choose from +, -, *, /, %.")
