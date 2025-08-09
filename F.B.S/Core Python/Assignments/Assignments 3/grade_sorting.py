#.Input 5 subject marks from user and display grade(eg.First class,Second class ..)
m1 = int(input("Enter the mark of English:- "))
m2 = int(input("Enter the mark of Marathi:- "))
m3 = int(input("Enter the mark of Hindi:- "))
m4 = int(input("Enter the mark of Science:- "))
m5 = int(input("Enter the mark of python:- "))
total_marks = m1 + m2 + m3 + m4 + m5
percentage = total_marks/500*100
if(percentage==35):
    print("pass")
elif(percentage>=95):
        print("Grade:-A+\nYour Briliant........")
elif(percentage>=90):
        print("Grade:-A")
elif(percentage>=80):
        print("Grade:-B")
elif(percentage>=70):
        print("Grade:-C")
elif(percentage>=50):
        print("Grade:-D")
else:
    print("fail")
#print(f'{percentage}%')