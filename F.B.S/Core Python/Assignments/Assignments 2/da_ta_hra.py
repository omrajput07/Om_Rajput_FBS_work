salary_employee = int(input("Enter the employee salary:- "))
da = salary_employee * 10/100
ta = salary_employee * 12/100
hra = salary_employee * 15/100

total_salary = salary_employee + da + ta + hra
print(f'total_salary:{total_salary}')