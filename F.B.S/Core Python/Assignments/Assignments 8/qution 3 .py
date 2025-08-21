# 1. Write a program to calculate area of rectangle
# 2. Write a program to calculate area of circle
# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n
# 4. Sum of all odd numbers between 1 to n
# 5. Sum of all prime numbers between 1 to n
# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms
# 7. Write a program to find sum of digits of a number.
# 8. Write a program find reverse of a number
# 9. Write a program to check if entered number is a palindrome or
# not.
# 10. Write a program to check if entered year is a leap year or not.
# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.


def sum_ofSerise(n):
    sum = 0
    for i in range( 1 , n + 1 ):
        sum += i
    return sum
def fact_sum(n):
    fact = 1
    sum = 0
    for i in range(1,n+1):
        fact*=i
        sum += fact
    return sum
def exponential(n):
         sum = 0 
         for i in range(1,n+1):
               sum += i ** i
         return sum

n = int (input("Enter the number:- "))
print(exponential(n))
              

n = int (input("Enter the number:- "))
print(fact_sum(n))

n = int (input("Enter the number:- "))
print(sum_ofSerise(n))