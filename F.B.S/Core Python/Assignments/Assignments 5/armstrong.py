num=int(input("Enter number "))
temp=num
sum=0

while(temp>0):
    d=temp % 10
    temp=temp // 10
    sum=sum+d**4

if(sum==num):
    print("amstrong number")
else:
    print("not armstrom")