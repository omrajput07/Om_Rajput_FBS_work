principal_amount = int(input("Enter principal amount:- "))
rate_of_intrest = int (input("Enter rate of intrest:-(%) "))
time_of_years = int (input("Enter of time in annual year:- "))
p = principal_amount
r = rate_of_intrest
t = time_of_years

compound_intrest = p * (1 + r/100) ** t
print(f'compound_intrest:{compound_intrest}')