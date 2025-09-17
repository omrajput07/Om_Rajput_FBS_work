# 1. Even odd number

def evenOdd(num):
    if(num == 0):
        return f'{num} is neutral'
    elif(num % 2 == 0):
        return f'{num} num is even'
    else:
        return f'{num}num is odd'

# 2. positive negative number
    
def possitiveNegative(num):
    if(num == 0):
        return f'{num} num is neutal'
    elif(num<0):
        return f'{num} num is negative'
    else:
        return f'{num} num is positive'

# 3. prime number

def checkprime(num):
    for i in range(2,(num // 2)+1):
      if(num % i == 0):
            return False
    else:
        return 
    
# 4. perfect number    

def perfect(num):
    sum = 0
    for i in range(1,num):
        if(num % i == 0):
            sum += i
        elif(sum == num):
            return f'{num}:This is perfect number'
        else:
            return f'{num}:The number is not perfect'

# 5. Palindrome number

def reverce(n , rev=0):
    if n == 0:
        return 0
    else:
        return reverce( n//10 , rev * 10 + n % 10)
    
def palindrome(n):
    if n == reverce(n):
        return f'The number is palindrome:- {n}'
    else:
        return f'The number is not palindrome:-{n}'   
    
# 6. factorial number

def fact(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i   
    return fac

# 7. armstrong number

def armstrong(n,sum = 0):
    temp = n
    digit = len(str(temp))
    for i in range(1,n+1):
        d = temp % 10
        sum += (d ** digit)
        temp = temp // 10
    if(n == sum):
        return f'This is armstrong number:- {n}'
    return f'This number is not armstrong:- {n}'
    
# 8. strong number

def strong(n):
    sum = 0
    for digite in str(n):
        sum += fact(int(digite))
    return sum
def checkstrong(n):
    if n == strong(n):
        return f'This number is strong:-{n}'
    return f'This number is not strong'
#-----------------------------------------------------------------------------------------#        
ch = 0 

while(ch != '9'):
    print('''Please select choice from below:
          1. Check even odd
          2. check positive negative
          3. Check prime number
          4. Check perfect number
          5. Check palindrome number
          6. Check factorial number
          7. Check armstrong number
          8. Check strong number
          9. Exit''')
    ch = input("Enter your choice:- ")

# 1. Even odd number

    if(ch == '1'):
        num = int(input("Enter the number:- "))
        res = evenOdd(num)
        print(res)

# 2. positive negative number    
    
    elif(ch == '2'):
        num = int(input("Enter the number:- "))
        res = possitiveNegative(num)
        print(res)

# 3. prime number

    elif(ch == '3'):
        num = int(input("Enter the number:- "))
        res = checkprime(num)
        if(res):
            print(f'{num}is a prime number')
        else:
            print(f'{num}is not prime number')

# 4. perfect number

    elif(ch == '4'):
        num = int(input("Enter the number:- "))
        res = perfect(num)
        print(res)

# 5. palindrome number

    elif(ch == '5'):
        num = int(input("Enter the number:- "))
        print(palindrome(num))

# 6. factorial number

    elif(ch == '6'):
        num = int(input("Enter the number:- "))
        print(fact(num))

# 7. armstrong number

    elif(ch == '7'):
        num = int(input("Enter the number:- "))
        print(armstrong(num))

# 8. strong number
    elif(ch == '8'):
        num = int(input("Enter the number:- "))
        print(checkstrong(num))

# 9. Exit the block of code

    elif(ch == '9'):
        print("Thank you")
    else:
        print("Invalid choice")






