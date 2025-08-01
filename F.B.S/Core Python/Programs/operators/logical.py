# 1. (and):- 'True = True'  :- True
        #    'False = False':- False
        #    'False = True' :- False
        #    'True = False ':- False   

a = True
b = False

print(a and a)
print(a and b)
print(b and b)
print(b and b)

# 2.(or):-   'True = True'  :- True
        #    'False = False':- False
        #    'False = True' :- True
        #    'True = False ':- True 
print(a or a)
print(a or b)
print(b or b)
print(b or a)

# 3.(Not):- 'False' :- True 
        #   'True ' :- False
print(not(a))
print(not(b))