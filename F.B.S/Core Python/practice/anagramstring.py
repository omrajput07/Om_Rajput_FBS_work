def check_anagram(str1,str2):
    if len(str1) != len(str2):
        return f'The string are not anagram'
    
    dict1 = {}
    dict2 = {}
    
    for ch1 , ch2 in zip(str1,str2):
        if ch1 in dict1:
            dict1[ch1] += 1
        else:
            dict1[ch1] = 1
        if ch2 in dict2:
            dict2[ch2] += 1
        else:
            dict2[ch2] = 1
    if dict1 == dict2:
        return(":--------This  is anagram string-------:")
    
    return (":--------The string are not anagram-------:")
    # if len(dict1) != len(dict2):
    #     return f'The string are not anagram'
    # for key in dict1:
    #     if key not in dict2 or dict1[key] != dict2[key]:
    #        return f'The string are not anagram' 
    #return f'this  is anagram string'

str1 = input("Enter the string 1: ")
str2 = input("Enter the string 2: ")
result = check_anagram(str1,str2)
print(result)