n = int(input("Enter the number range to check in prime number:-"))
count = 0
num = 2
while(count<n):
    for i in range(2,num//2+1):
        if(num % i==0):
            break
    else:
        print(f'{num}')
        count += 1
    num += 1
