def evenOdd(num):
    if(num == 0):
        return f'{num} is neutral'
    elif(num % 2 == 0):
        return f'{num} num is even'
    else:
        return f'{num}num is odd'
    
def possitiveNegative(num):
    if(num == 0):
        return f'{num} num is neutal'
    elif(num<0):
        return f'{num} num is negative'
    else:
        return f'{num} num is positive'

def checkprime(num):
    for i in range(2,(num // 2)+1):
      if(num % i == 0):
            return False
    else:
        return True

def perfect(num):
    sum = 0
    for i in range(1,num):
        if(num % i == 0):
            sum += i
        elif(sum == num):
            return f'{num}:This is perfect number'
        else:
            return f'{num}:The number is not perfect'
        
ch = 0 

while(ch != '8'):
    print('''Please select choice from below:
          1. Check even odd
          2. check positive negative
          3. Check prime number
          4. Check perfect number
          5. Check strong number
          6. Check factorial number
          7. Check armstrong number
          8. Exit''')
    ch = input("Enter your choice:- ")
    if(ch == '1'):
        num = int(input("Enter the number:- "))
        res = evenOdd(num)
        print(res)
    elif(ch == '2'):
        num = int(input("Enter the number:- "))
        res = possitiveNegative(num)
        print(res)
    elif(ch == '3'):
        num = int(input("Enter the number:- "))
        res = checkprime(num)
        if(res):
            print(f'{num}is a prime number')
        else:
            print(f'{num}is not prime number')
    elif(ch == '4'):
        num = int(input("Enter the number:- "))
        res = perfect(num)
        print(res)
    elif(ch == '5'):
        pass
    elif(ch == '6'):
        pass
    elif(ch == '7'):
        pass
    elif(ch == '8'):
        print("Thank you")
    else:
        print("Invalid choice")





#perfect number
#armstrong number
#strong number
#palindrome number