#.WAP to calculate selling price of book based on cost price and discount.
cost_price = int(input("Enter the cost_price "))
selling_price = cost_price + (10 // 100) * cost_price
print(f'selling_price{selling_price}')
discount = selling_price -(5 // 100) * cost_price
print(f'discount_price:{discount}')