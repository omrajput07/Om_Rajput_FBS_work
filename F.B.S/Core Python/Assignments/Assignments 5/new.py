userid = "admin"
password = "1234"
i = 1
input_userid = input("Please enter user id:- ")
input_password = input("please enter password:- ")

while i <= 3:
    if (input_password  == password):
        print("password is correct")
        break
    else:
        input_password = input("Enter password correctly") 
    i += 1

#if input_userid==userid and input_password==password:
#    print("user id and password is correct successful login")
