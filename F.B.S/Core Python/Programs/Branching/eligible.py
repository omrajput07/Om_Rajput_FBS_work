#male = 21
#female = 18
gender = (input("Enter the gender:- "))
age = int(input("Enter the gender:- "))
if((gender == 'Male' and age >= 21) or (gender == 'Female' and age >= 18)):
    print(f'eligible for marrieage')
else:
    print('Not Eligible for marriage')


