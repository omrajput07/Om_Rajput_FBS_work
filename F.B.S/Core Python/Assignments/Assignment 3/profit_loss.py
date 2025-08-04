#.Write a program to calculate profit or loss.

amount1 = int(input("Enter the cost price:- "))
amount2 = int(input("Enter the selling price:- "))
final_amount = amount1 + amount2
if(amount1<=amount2):
    profit_amount = amount2 - amount1
    total = profit_amount + amount1
    print(f'total amount is: {total},profit amount is:-{profit_amount}')
else:
    lose_amount = amount1 - amount2
    print(f'the lose is:-{lose_amount} ')