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