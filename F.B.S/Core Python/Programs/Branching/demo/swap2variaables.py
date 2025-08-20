
x = 10 # 10 store in x
y = 20 # 20 store in y
x = x + y # x is add in y  [20 + 10 = 30] x = 30
y = x - y # y is x - y  [30 - 20 = 10]    y = 10
x = x - y # x is x - y  [30 - 10 = 20]    x = 20
print(f'After swapping x:{x},y:{y}') # print [x and y]

x = 10 # 10 store in x                  
y = 20 # 20 store in y
z = x # x is store in z
x = y # y is store in x
y = z # z is store in y
print(f'After swapping x:{x},y:{y}') # print [x and y]

# the python trick are x,y = y,x
