num = int(input("Enter The number press 1 to perform even odd operation\nand press 2 display employee basic salary:-"))
if(num==1):
    num1 = int(input("Enter the number check even or odd:- "))
    if(num1==0):
        print(f'This number is nutral')
    elif(num1 % 2 == 0):
        print(f'This number is even')
    else:
        print(f'this number is odd')
else:
    salary = int(input("Enter the employee salary:- "))
    if(salary<=5000):
        da =  salary *0.10
        ta = salary *0.20
        hra = salary *0.25
        total_salary = salary + da + ta + hra
        print(f'Total salary of employee:{total_salary}')
    else:
        da = salary *0.15
        ta = salary *0.25
        hra = salary *0.30
        total_salary = salary + da + ta + hra
        print(f'Total salary of employee:{total_salary}')

