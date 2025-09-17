def bubble(li):
    for i in range(1,len(li)):
        for j in range(len(li) - i):
            if(li[j] > li[j + 1]):
                li[j] , li[j +1] = li[j+1] , li[j]
                print(f'{j}:-{li}')
    
    return li

li = [60,50,40,30,20,10]
print("Before sorting list:- ",li)
li = (bubble(li))
print("After sorting list in bubble sort:- ",li)