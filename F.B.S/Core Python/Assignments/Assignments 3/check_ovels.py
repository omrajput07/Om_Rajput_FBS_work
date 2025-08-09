#.Write a program to input any alphabet and check whether it is vowel or consonant.
character = (input("Enter the one character:- "))
vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
if(character in vowel):
    print("This character are owel")
else:
    print("this character are consonant")