#1. find maximum number:

def max(li):
    max = li[0]
    for i in range(1 , len(li)):
        if(li[i]>max):
                max = li[i]
    return f'maximum number is:- {max}'
        
#2. find minimum number:

def min(li):
    max = li[0]
    for i in range(1 , len(li)):
        if(li[i]<max):
                max = li[i]
    return f'maximum number is:- {max}'

#3. Reverce index list:

def reverce(li):
    new = []
    for i in range(len(li)-1,-1,-1):
        new.append(li[i])
    return new

#4. Find Second max & Third max number

def second_max(li):
     max = li[0]
     second = 0
     third = 0
     for i in range (1,len(li)):
          if(li[i] > max):
               third = second
               second = max
               max = (li[i])
          elif(li[i] > second):
               second = max
               second = (li[i])
          elif(li[i] > third):
               third = (li[i])
     print( f'maximum number is:- {max}')
     print (f'second max in list:- {second}')
     return f'third max in list:- {third}'               
          
#5. Print list Removing even number

def reduce_even(li):
    new_list = []
    for i in range(0,len(li)):
        if(li[i] % 2 != 0):
            new_list.append (li[i])
    return f'The list is without even number:- {new_list}'
            
#6. find the element in list

def find_element(li,user):
    for i in range(len(li)):
        if(li[i] == user):
            return f'{user} The element are present in list'
    return f'{user} The element are not present in list'

#7. Remove duplicate for list

def remove_duplicate(li):
    unique = []
    for item in li:
        if item not in unique:
            unique.append(item)
    return unique

# 8. Create new list of the cube elements cube

def cube_list(li):
    new_li = []
    for element in li:
        new_li.append(element * element * element)
    return new_li
    
# 9. Copy existing list to new list

def copy_new_list(li):
    new_list = []
    for element in li:
        new_list.append(element)
    return new_list

# 10.Even or Odd elements print in seprate list.

def even_odd(li):
    even = []
    odd = []
    for elements in li:
        if elements % 2 == 0:
            even.append(elements)
        else:
            odd.append(elements)
    return even , odd

# 11.Remove the element in the list.

def remove_element(li,removable):
    update_list = []
    for element in li:
        if element != removable:
            update_list.append(element)
    return update_list

# 12.Print only m and n divisible elements.

def m_and_n_devisible(li,m,n):
    new_list = []
    for element in li:
        if element % m == 0 and element % n == 0:
            new_list.append(element)
    return new_list

# 13.List element cube and squre.

def cube_an_squre(li):
    cube_list = []
    squre_list = []
    for element in li:
        cube_list.append(element**3)
        squre_list.append(element**2)
    return cube_list , squre_list

#--------------------------------------------------------------------------------------------#

ch = 0
while(ch != '14'):
    print('''Enter your choice Below :
        1. find maximum number.
        2. find minimum number.
        3. Reverce index list.
        4. Find Second max & Third max number.
        5. Print list Removing even number.
        6. find the element in list.
        7. Remove duplicate for list.
        8. Create new list.
        9. Copy existing list to new list.
        10.Even or Odd elements print in seprate list.
        11.Remove the element in the list.
        12.Print only m and n divisible elements.
        13.List element cube and squre.
        14. Exit''')
    ch = input("Enter Your choice:- ")
#---------------------------------------------------------------------------------------------#

#1. find maximum number:

    if(ch == '1'):
        li = [10,20,30,40,50,60,70]
        print(max(li))
    

#2. find minimum number:
    
    elif(ch == '2'):
         li = [10,20,30,40,50,60,70]
         print(min(li))

#3. Reverce index list:
    
    elif(ch == '3'):
        li = [10,20,30,40,50,60,70]
        print(reverce(li))

#4. Find Second max & Third max number

    elif(ch == '4'):
        li = [10,20,30,40,50,60,70]
        print(second_max(li))
    
#5. Print list Removing even number
    
    elif(ch == '5'):
        li = [1,2,3,4,5,6,7,8,9,10]
        print(reduce_even(li))
    
#6. find the element in list    
    
    elif(ch == '6'):
        li = [1,2,3,4,5,6,7,8,9,10]
        user = int(input("Enter element to find in list:- "))
        print(find_element(li,user))
    
#7. Remove duplicate for list

    elif(ch == '7'):
         li = [1,2,3,4,4,4,5,6,7,8,9,10]
         print(remove_duplicate(li))
            
# 8. Create new list of the cube elements cube

    elif(ch == '8'):
         li = [2,3,4]
         new_list = cube_list(li)
         print(new_list)
             
# 9. Copy existing list to new list

    elif(ch == '9'):
        li = [1,2,3,4,4,4,5,6,7,8,9,10]   
        new_list = copy_new_list(li)
        print(new_list) 
    
# 10.Even or Odd elements print in seprate list.

    elif(ch == '10'):
        li = [1,2,3,4,5,6,7,8,9,10]
        even ,odd = even_odd(li)
        print("The even list is:",even)
        print("The odd list is:",odd)
# 11.Remove the element in the list.

    elif(ch == '11'):
        li = [1,2,3,4,5,6,7,8,9,10]
        print(li)
        delate_element = int(input("Enter the removable element: "))
        print("After  updated list",remove_element(li,delate_element))

# 12.Print only m and n divisible elements.

    elif(ch == '12'):
        li = [12,20,15,14,6,18]
        m = 2
        n = 3
        result = m_and_n_devisible(li,m,n)
        print("Only m and n divisible number are print:",result)

# 13.List element cube and squre.

    elif(ch == '13'):
        li = [12,20,15,14,6,18]
        cube_lis,squre_list = cube_an_squre(li)
        print("The cubes is in our list",cube_lis)
        print("The Squer is in our list",squre_list)
# 14. Exit.

    elif(ch == '14'):
        print("Thankyou")

# 15. Invalid_choice.

    else:
        print("Invalid Choice........")