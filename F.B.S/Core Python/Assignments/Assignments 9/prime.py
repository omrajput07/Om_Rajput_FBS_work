def prime(n , devisor= None):
    if(n < 2):
        return "this is not prime number"
    if(devisor == None):
        devisor = n-1
    if(devisor == 1):
        return "This is prime number"
    if(n % devisor == 0):
            return "this is not prime number"
    return prime(n, devisor - 1)


n = int(input("Enter the number:- "))
print(prime(n))

    