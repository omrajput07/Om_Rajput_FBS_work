def perfect(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if n == sum:
        return f'this number is perfect: {n}'
    else:
        return f'this number is not perfect:-{n}'
n = int(input("Enter the number:- "))
res = perfect(n)
print(res)