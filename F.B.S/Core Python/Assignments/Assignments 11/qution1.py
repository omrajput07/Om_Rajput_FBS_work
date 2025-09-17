# 1. Python Program to Put Even and Odd elements of a List into two Different Lists

def even_odd(li):
    even = []
    odd = []
    for element in li:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    return even,odd

li = [1,2,3,4,5,6,7,8,9,10]
eve,odd = even_odd(li)
print("The list is even:",eve)
print("The list is odd:",odd)