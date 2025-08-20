# 1. variable length / number of argurment
# 2 .Mentioneed asterisk (*) symbol before parameter in function defination
# 3. we can pass multiple values in function call
# 4. store in tuple format
# 5. we're going to iterate values using for loop

def add(*data):
    sum = 0
    for ele in data:
        sum += ele
    print(sum)

add(10,20)
add(20,30,10,50,15,658)

str = 'Hellow word'
for i in str:
    print(i,end= ' ')