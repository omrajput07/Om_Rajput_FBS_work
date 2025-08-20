def sum_of_serice(n):
    if(n == 0):
        return 0
    else:
        return n + sum_of_serice(n - 1)

n = int(input("Enter the number:- ")) 
sum = sum_of_serice(n)
print(sum)