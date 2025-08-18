n = 5  # number of rows

for i in range(1, n + 1):           # rows
    for j in range(1, i + 1):       # columns
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()