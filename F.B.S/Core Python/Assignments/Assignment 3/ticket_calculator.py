#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

ticket_amount = float(input("Enter ticket amount for persons:- "))

age1 = int(input("Enter age of person 1:- "))
age2 = int(input("Enter age of person 2:- "))
age3 = int(input("Enter age of person 3:- "))
age4 = int(input("Enter age of person 4:- "))
age5 = int(input("Enter age of person 5:- "))

# for person 1
if(age1<=12):
    discount_amt = ticket_amount * 0.3
    amt1 = ticket_amount - discount_amt
elif(age1>=59):
    discount_amt = ticket_amount * 0.5
    amt1 = ticket_amount - discount_amt
else:
    amt1 = ticket_amount
 
# for person 2
if(age2<=12):
    discount_amt = ticket_amount * 0.3
    amt2 = ticket_amount - discount_amt
elif(age2>=59):
    discount_amt = ticket_amount * 0.5
    amt1 = ticket_amount - discount_amt
else:
    amt2 = ticket_amount

# for person 3
if(age3<=12):
    discount_amt = ticket_amount * 0.3
    amt3 = ticket_amount - discount_amt
elif(age3>=59):
    discount_amt = ticket_amount * 0.5
    amt3 = ticket_amount - discount_amt
else:
    amt3 = ticket_amount

# for person 4
if(age4<=12):
    discount_amt = ticket_amount * 0.3
    amt4 = ticket_amount - discount_amt
elif(age4>=59):
    discount_amt = ticket_amount * 0.5
    amt4 = ticket_amount - discount_amt
else:
    amt4 = ticket_amount

# for person 5
if(age5<=12):
    discount_amt = ticket_amount * 0.3
    amt5 = ticket_amount - discount_amt
elif(age5>=59):
    discount_amt = ticket_amount * 0.5
    amt5 = ticket_amount - discount_amt
else:
    amt5 = ticket_amount
    


total_amt = amt1 + amt2 + amt3 + amt4 + amt5
print(f'The total ticket amount is:-{total_amt}')
