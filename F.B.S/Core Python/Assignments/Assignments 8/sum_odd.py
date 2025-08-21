# 4. Sum of all odd numbers between 1 to n

def sum_odd(n):
    for i in range(1,n+1,2):
        sum = 0
        sum += i
    return f"this is odd numbers:{sum}"
        
n = int(input("Enter the number:- "))
print(sum_odd(n))