verify_stud = (input("your are a student say 'yes' or 'no':- "))
price = int(input("Enter the product price:-"))
if(verify_stud == 'yes'):
    if(price > 500):
        discount_price = price *0.20
        price = price - discount_price
        print(f'Total price is :{price}')
    else:
        discount_price = price *0.10
        price = price - discount_price
        print(f'Total price is :{price}')
else:
    if(price>600):
         discount_price = price *0.15
         price = price - discount_price
         print(f'Total price is :{price}')
    else:
        print(f"not discount aplly:{price}")