def selection(li):
    size = len(li)
    for i in range(size - 1):
        index = i
        for j in range(i + 1 , len(li)):
            if(li[j] < li[index]):
                index = j
        li[i] , li[index] = li[index] , li[i]
        print(li)
    return li

li = [50,30,40,10,20]
print("befor sorting list",li)
li = selection(li)
print(f'after sorting list',li)


#. i = position
#. j = compare the number
#. index = 