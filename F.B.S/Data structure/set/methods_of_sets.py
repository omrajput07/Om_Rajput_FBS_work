s1 = {10,20,30,40}
s2 = {30,40,50,60}
s4 = {10,20}


#methods 

s1.add(50)
# s1.clear()
# s3 = s1.copy()
# print(s1.difference(s2))
# s1.difference_update(s2) # that method are workin to original 
# s1.discard(30) # that are dilate the value in original
# print(s1.intersection(s2)) # return comman value
print(s1.issubset(s4))  # check the s1 element are both same and return true or false
print(s4.issubset(s1))  #check  the element are both same and return true or false
print(s1.issuperset(s4)) # s1 in all s4 element are present tu return true or not same retun false
s1.pop()  #this method are working in original and delate random element
print(s1)
s1.remove(10) #this method are woring the original and delate the present element or not present element return error
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
s1.update({90,100})
print(s1.union(s2))