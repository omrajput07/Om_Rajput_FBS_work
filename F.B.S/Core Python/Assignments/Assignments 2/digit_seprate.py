num = int(input("Enter three digit numbers:- "))
temp = num              #store the num of temp variable [152]
d1 = temp % 10          #temp is 152 % 10 = 2 is remainder and remaining amount store in temp 
temp = temp // 10       #temp is 150 // 10 = 15 is qutiont remeaning store in temp

d2 = temp % 10          #temp is 15 % 10 = 5 is remainder and remaining amount store in temp
temp = temp // 10       #temp is 15 // 10 = 1 is qutiont remeaning store in temp

d3 = temp % 10          #temp is 1 % 10 = 1 is remainder and remaining amount store in temp
temp = temp // 10       #temp is 1 // 10 = 0 is qutiont remeaning store in temp

print(f'D1:{d1},D2:{d2},D3:{d3}')