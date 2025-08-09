num = int(input("Enter the number to check prime:- "))
for i in range(2,num//2+1):
    
    if(num%i==0):
        print(f'This is not prime number:{num}')
        break
else:
    print(f'This is the prime number:{num}')