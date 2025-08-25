p = int(input("Enter principal amount:- "))
r = int (input("Enter rate of intrest:-(%) "))
t = int (input("Enter of time in annual year:- "))
compound_intrest = p * (1 + r/100) ** t
rate_of_intres = compound_intrest - p
print(f'Total amount is with intrest:{compound_intrest}:intrest of the amount:- {rate_of_intres}')