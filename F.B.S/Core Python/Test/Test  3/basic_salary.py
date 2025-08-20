salary=int(input("enter salary:"))

while(salary>20000):
    da=(salary/100)*10
    ta=(salary/100)*12
    hra=(salary/100)*15
    print(f"da:{da} ta:{ta} hra:{hra}")
    break
else:
    da=(salary/100)*15
    ta=(salary/100)*18
    hra=(salary/100)*20
    print(f"da:{da} ta:{ta} hra:{hra}")

total_salary=da+ta+hra+salary
print("total_salary",total_salary)
    