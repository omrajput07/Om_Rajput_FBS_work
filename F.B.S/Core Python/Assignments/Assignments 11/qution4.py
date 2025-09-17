# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort.


def bubble(li):
    for i in range(1,len(li)):
        for j in range(len(li) - i):
            if(li[j] > li[j + 1]):
                li[j] , li[j +1 ] = li[j + 1] , li[j]
    return li

li = [100,40,10,50,30,20,80,60,70,90]
print("List after sorting:",li)
res = bubble(li)
print("----------------------------------||----------------------------------")
print("List before sorting:",li)
            