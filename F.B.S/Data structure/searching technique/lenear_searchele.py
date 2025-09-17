def search(li,search):
    for i in range(len(li)):
        if((li[i]) == search):
            print(i)
            return i
            
    return -1

li = [ 10, 30 , 40, 50 ,70 ,90]
searchele = int(input("Enter the element for search:- "))
res = search(li , searchele)
if(res != -1):
    print(f"{searchele}:Element is found in list: {res}.")
else:
    print(f"{searchele}:Element is not found in list.")
    
