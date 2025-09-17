D = [2000,500,200,100,50,20,10,5,2,1]

amount = int(input("Enter the amount: "))

note_count = {}

for note in D:
    if amount >= note:
        count = amount // note
        note_count[note] = count
        amount = amount % note

print("Denominations needed:")

for note in D:
    if note in note_count:
        print(f"{note} x {note_count[note]}")

# def notes(li):
#     sum_list = []
#     for ele in range(len(li)):
#         sum_list.append(ele)
#     return sum_list

# D = [2000,500,200,100,50,20,10,5]
# result = notes(li)
# print(result)
