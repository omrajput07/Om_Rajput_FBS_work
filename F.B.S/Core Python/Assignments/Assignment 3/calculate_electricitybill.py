unit = int(input("Enter the meter reading units:- "))
total_bill = 0
if(unit>0):
    if(unit>50):
        if(unit>150):
            if(unit>200):
                pass
            else:
                total_bill = 50 * 0.50
                remaining_unit = unit - 150
                total_bill = total_bill + (remaining_unit * 1.20)
        else:
            total_bill = 50 * 0.50
            remaining_unit = unit - 50
            total_bill = total_bill + (remaining_unit * 0.75)
    else:
        total_bill = unit * 0.50
else:
    print("the input value is Invalid..")

print(total_bill)



   

