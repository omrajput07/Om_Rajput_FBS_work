def reverce(n,rev=0):
    if(n == 0):
        return rev 
    return reverce(n // 10 , rev * 10 + n % 10)
def palindrome(num):
    if num ==  reverce(num):
        return f"The number is palindrome:-{num}"
    else:
        return f"The number is not palindrome:-{num}"

n = int(input("Enter the number:- "))
print(palindrome(n))