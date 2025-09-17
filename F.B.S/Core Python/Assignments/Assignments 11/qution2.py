# 2. Python Program to Merge Two Lists and Sort it

def merge(li1,li2):
    li_3 = []
    for element in li1:
        li_3.append(element)
    for element in li2:
        li_3.append(element)
    return li_3

    # li_3.sort()

def bubble(mergel):
    sorted_li = []
    for i in range(len(mergel)):
        for j in range(len(mergel)-i):
            if mergel[j] > mergel[j+1]:
                mergel [j] , mergel[j+1] = mergel[j+1] , mergel[j]
                print(mergel)

    return mergel    

li_1 = [1,2,3,4,5,6,7,8,9,10]
li_2 = [10,9,8,6,7,5,4,2,1,3]
mergel = bubble(li_1,li_2)
print(mergel)