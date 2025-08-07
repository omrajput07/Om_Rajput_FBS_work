# factrorial sum
num = int(input("Enter the number:- "))
temp = num
sum = 0

# seprate digit and stor "D" variable

while(temp>0):
    d = temp % 10
   # print(d)
    temp = temp // 10
    i = 1
    fact = 1
    #geting seprate digit factroial number
    while(i<=d):
        fact *= i
        i += 1
    sum += fact
#print sum are exact equal to num are condition are true
if(sum == num):
    print(f'this is strong number')
else:
    print(f'this is not strong number')

