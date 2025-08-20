# 1. Mentioned double asterisk(**)symbol before parameter in fuction definition
# 2. stored data into a dictionary format
# 3. pass multiple values with key(attribute)
# 4. use for loop on dic.items()to iterate key and values
def emp (**detail):
    for i , j in detail.items():
        print(i,':',j)
    print("-------------#$#---------------")
emp(id=101,name="Om",sal= 1005,dept="devloper")
emp(id=102,name="xyz",sal= 1006,dept="wonder")