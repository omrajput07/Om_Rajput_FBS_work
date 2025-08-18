
person = int(input("Enter the count of passengers:- "))
ticket_amount = int(input("Enter the ticket amount:- "))
final_amt = 0
for i in range(1,person+1):
    age = int(input(f"Enter the age off passenger{i}:- "))
    if(age<=12):

        discount_amt = ticket_amount  * 0.3
        total =   ticket_amount - discount_amt
    elif(age>=59):
        discount_amt = ticket_amount * 0.5
        total = ticket_amount - discount_amt
    else:
         total = ticket_amount
    final_amt += total
print(final_amt)
