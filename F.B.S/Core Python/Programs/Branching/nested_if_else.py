num = int(input("Enter the number:- "))
if(num > 0):
    if(num > 50):
        if(num > 100):
            if(num > 150):
                if(num > 200):
                    print("The number is greater than 200")
                else:
                    print("the number is greate than 150 but less than 200")
            else:
                print("Number is greater than 100 but less than 150")
        else:
            print("Number is greater than 50 but less than 100")
    else:
        print("Number is greater than 0 but less than 50")
else:
    print("Number is less than or 0")