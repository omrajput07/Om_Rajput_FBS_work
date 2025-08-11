#.Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to  
# re-enter the credentials. Let him try 3 times. After that program to terminate.

#id == 'admin' and password == 1234
for attempt in range(1,4):
    print("This is your attemp no",attempt, "remember after 3 attempts your password will be lock")
    id = (input("Enter the user id:- "))
    password = int(input("Enter the password:- "))
    
    if(id == 'admin' and password == 1234):
        print(f'id password is correct \n login successfully..')
        break
    else:
        password = ("Enter correct password")
    if(attempt == 3):
        password =input("You have completed all 3 attempts")
        
