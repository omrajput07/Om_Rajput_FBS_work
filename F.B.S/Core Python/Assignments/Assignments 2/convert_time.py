#Convert the time entered in hh,min and sec into seconds.
#user_time = int(input("Enter the Time:- "))
#hours = user_time // 60
#minute = user_time % 60
#second = user_time // 60
#print(f'hours:{hours} , minute:{minute} , second:{second}')

hours = int(input("enter the hours:- "))
minute = int(input("enter the minute:- "))
second = int(input("enter the seconds:- "))
total_seconds = hours * 3600 + minute * 60 + second
print("total_seconds",(total_seconds))