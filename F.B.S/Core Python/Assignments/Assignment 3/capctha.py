#.Write a program to prompt user to enter userid and password. After verifying captcha.
import random
user_id = (input("Enter the user_name:- "))
password = int(input("Enter the password:- "))
generate_captcha = random.randint(1111, 9999)
print(f'generate_captcha:{generate_captcha}')
captcha = int(input("enter the captcha:- "))
if(user_id=='admin') and (password==1234) and (generate_captcha==captcha):
    print(f"login succefully..\n..welcome your account...")
else:
    print(f"invalid id , password or captcha..")
