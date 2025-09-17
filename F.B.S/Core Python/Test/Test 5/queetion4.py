numbers = [1,2,1,2,3,1,3,4,5,4,2,5]
check_count = {}
for num in numbers:
    if num in check_count:
        check_count[num] += 1
    else:
        check_count[num] = 1
print("The frequency of number: ",check_count)