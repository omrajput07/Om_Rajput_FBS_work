n = 5  # height of the pyramid

for i in range(1, n + 1):
    # Print leading spaces
    for s in range(n - i):
        print("  ", end="")

    # Increasing numbers
    for j in range(i):
        print(i + j, end=" ")

    # Decreasing numbers
    for j in range(i - 2, -1, -1):
        print(i + j, end=" ")

    print()