# 9. Write a program to check if entered number is a palindrome or not
def reverce(num , rev = 0):
    if(num == 0):
        return 0
    else:
        return reverce(num // 10,(rev * 10) + num % 10)
def palindrome(num):
    if num == reverce(num):
        return f'The number is palindrome:-{num}'
    return f'The number is not palindrome:-{num}'

n = int(input("Enter the number:- "))
print(palindrome(n))