def binarysearch(li,search):
    beg = 0
    end = len(li)-1
    while(beg<=end):
        mid = (beg + end) // 2
        if(search == li[mid]):
            return mid
        elif(search > li[mid]):
            return mid + 1
        elif(search < li[mid]):
             return mid -1
    else:
        return -1

li = [ 10,20,30,40,50,60]
searchele = int(input("Enter the element for search:- "))
res = binarysearch(li , searchele)
if(res != -1):
    print(f'{searchele} is element found index:- {res}.')
else:
    print(f'{searchele} The element are not found in index.')