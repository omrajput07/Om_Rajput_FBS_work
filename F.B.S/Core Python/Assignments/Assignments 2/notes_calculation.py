notes = int(input("Enter number for calculates notes"))
amount = notes

two_thousands = amount // 2000
amount = amount % 2000

five_hundred = amount // 500
amount = amount % 500

two_hundred = amount // 200
amount = amount % 200

one_hundres = amount // 100
amount = amount % 100

fifty_rupee = amount // 50
amount = amount % 50

twenty_rupee = amount // 20
amount = amount % 20

ten_rupee = amount // 10
amount = amount % 10

notes = two_thousands + five_hundred + two_hundred + one_hundres + fifty_rupee + twenty_rupee + ten_rupee
print(f'total_notes:{notes}')

