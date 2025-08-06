#5. A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST
product1 = int(input("Enter the first product price:- "))
product2 = int(input("Enter the second product price:- "))
product3 = int(input("Enter the third product price:- "))
product4 = int(input("Enter the fourth product price:- "))
product5 = int(input("Enter the fifth product price:- "))
Total_price = product1 + product2 + product3 + product4 + product5
Gst = Total_price *0.18
Total_price = Total_price + Gst
print(f'Total amount is with :{Total_price}and gst is add 18% {Gst}')