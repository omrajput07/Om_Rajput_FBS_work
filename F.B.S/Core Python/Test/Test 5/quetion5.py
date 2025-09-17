list1 = [1,2,3,7,8,9]
list2 = [1,2,3,4,5,6]

union_list = list1.copy()

for items in list2:
    if items not in union_list:
        union_list.append(items)
        union_list.sort()

print("The union list is",union_list)