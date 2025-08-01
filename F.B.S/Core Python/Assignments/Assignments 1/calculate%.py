science = int(input("Enter the marks this subject: "))
math = int(input("Enter the marks this subject: "))
python = int(input("Enter the marks this subject: "))
java = int(input("Enter the marks of this subject: "))
english = int(input("Enter the marks of this subject: "))

gain_marks  = science + math + python + java + english
percentage = (gain_marks / 500) * 100
print(f'percentage is {percentage}%.')