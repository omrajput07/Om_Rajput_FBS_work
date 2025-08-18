num_of_stud = int (input("Enter the number of sudents:- "))
total_percentage = 0
for stud in range (1 , num_of_stud+1):
    print(f"student number:{stud}")
    sub1 = int(input("Enter the marks science:- "))
    sub2 = int(input("Enter the marks math:- "))
    sub3 = int(input("Enter the marks python:- "))
    sub4 = int(input("Enter the marks Marathi:- "))
    sub5 = int(input("Enter the marks English:- "))
    total_marks = sub1 +sub2 + sub3 + sub4 + sub5
    percentage = total_marks/500*100
    print(f"student :{stud}:percentage is:={percentage}")
    
    total_percentage += percentage  # Add to total

average = total_percentage/num_of_stud
print(f'The average percentage of  students:{average}')


