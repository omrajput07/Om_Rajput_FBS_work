# 1. assigning value to parameter/argurment in the function definition.
# 2. flow should be right to left
# 3. Invoking optional parameter concept
def addition(num1,num2,num3=0,num4=0):
    return num1 + num2 + num3 + num4
print(addition(10,20,30,40))
print(addition(10,20))