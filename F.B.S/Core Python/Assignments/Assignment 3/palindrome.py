#.Write a program to check if given 3 digit number is a palindrome or not.
digit = int(input("Enter the Three digit number:- "))
num = digit
d1 = num // 10
num = num % 10

d2 = num // 10
num = num % 10

d3 = num // 10
reverse = d3*100 + d2*10 + d1
print(f'reverse digit : {reverse}')
if(reverse==digit):
    print("this is palindrome number..")
else:
    print("It is not palindrome number..")

#print(d1,d2,d3)