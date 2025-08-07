num = int(input("Enter the  number to seprate single digit:- "))
temp = num
while(temp>0):
    d = temp % 10
    print(d)
    temp = temp // 10

    