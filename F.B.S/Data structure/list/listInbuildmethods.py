li = [10,20,30,50,60,70]
li.append(40)
print(li)

li = [10,20,30,50,60,70]
li.clear()
print(li)

li = [10,20,30,50,60,70]
new = []
new = li.copy()
print(new)

li = [10,20,30,50,60,70]
li.extend([90,100])
print(li)

li = [10,20,30,50,60,70]
li.extend("om rajput")
print(li)

li = [10,20,30,50,60,70]
li.index(20)
print(li)

li = [10,20,30,50,60,70]
li.insert(0,80)
print(li)

li = [10,20,30,50,60,70] # return the count in list 
print(li.count(30))

li = [10,20,30,50,60,70]
li.pop(1)  # working in index, Remove the index value in list
print(li)

li = [10,20,30,50,60,70]
li.remove(30) # working in value,Remove the value in list
print(li)

li = [20,40,60,70,40,50]
li.sort() #sorting list
print(li)

li = [10,20,30,50,60,70]
li.reverse() #Reverce the list
print(li)

li = [20,40,60,70,40,50]
li.sort(reverse=True)  #Reverce the list in sorted form
print(li)


print("Nested List")

li = [10,20,[30,40],[60,50,80]]
li2= li.copy()
li2[0] = 30
print(li2)