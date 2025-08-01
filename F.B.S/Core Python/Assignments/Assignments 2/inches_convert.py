#- 1 foot = 12 inches
#- 1 inch = 2.54 centimeters
#- 100 centimeters = 1 meter
foot = float(input("Enter the distance in foot:- "))
inches = float(input("Enter the inches:- "))
total_inches = foot * 12 + inches
centimiter = total_inches * 2.54
meter = centimiter / 100
print(f'centimiter in distance:{centimiter} , meter in distance:{meter}')