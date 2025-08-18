n = 5

for i in range(1, n + 1):
   
    for space in range(n - i):
        print("  ", end="")

    
    for num in range(1, 2 * i):
        print(num, end=" ")

    print()