#.A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
#for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
#length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
#cost of fencing the field.

radius = int(input("Enter the radius:- "))
length = int(input("Enter the length:- "))
breadth =int(input("Enter the breadth:- "))
times_of_fencing = int(input("Enter the Which times of fencing:- "))
rate  = int(input("Enter the rate of fencing per meter:- "))
radius  = radius * 3.14
length = length * 2
perimeter = radius + length + breadth
total_perimeter = perimeter * times_of_fencing 
cost = total_perimeter * rate
print(f'Total perimeter of the: {perimeter},Total cost of fencing is: {cost}')
