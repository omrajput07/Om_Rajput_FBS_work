# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace_string(str):
    rep = ''
    for char in str:
        if char == 'a':
            rep+= '$'
        else:
            rep += char
    return rep


str = input("Enter the string:- ")
print(replace_string(str))
