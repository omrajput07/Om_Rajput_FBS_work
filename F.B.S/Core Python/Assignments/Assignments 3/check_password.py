user_id = (input("Enter the user_name:- "))
password = int(input("Enter the password:- "))
if(user_id=='admin') and (password==1234):
    print(f"login succefully..")
else:
    print(f"invalid id password..")