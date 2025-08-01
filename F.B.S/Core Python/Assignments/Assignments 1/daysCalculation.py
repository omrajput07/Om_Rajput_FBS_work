days = int(input("Enter the days: "))
years = days // 365
days = days % 365
weeks = days // 7
days = days % 7
print(f'{years} years {weeks} weeks {days} days.')


user_days = int(input("Enter the number of days: "))

years = user_days // 365
remaining_days = user_days % 365

weeks = remaining_days // 7
days = remaining_days % 7

print(f"{years} years, {weeks} weeks, and {days} days.")