price = int(input("Enter the price"))
if(price>5000):
    if(price>7000):
        if(price>10000):
            if(price>15000):
                discount = price *0.18
                final_price = price - discount
                print(f'final_price is:{final_price}')
            else:
                discount = price *0.18
                final_price = price - discount
                print(f'final_price is:{final_price}')
        else:
            discount = price *0.15
            final_price = price - discount
            print(f'final_price is:{final_price}')

    else:
        discount = price *0.12
        final_price = price - discount
        print(f'final_price is:{final_price}')

else:
    discount = price *0.10
    final_price = price - discount
    print(f'final_price is:{final_price}')
