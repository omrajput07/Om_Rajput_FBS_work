a = int(input("enter value a:- "))
b = int(input("enter value b:- "))
c = int(input("enter value c:- "))
sqrt =((b ** 2) - (4 * a * b * c)) ** 0.5
resl1 = (-b + sqrt) / 2 * a
resl2 = (-b - sqrt) / 2 * a
print(f'quadratic equation:{resl1},{resl2}')