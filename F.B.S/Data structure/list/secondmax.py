li = [10,30,60,40,52,98,45,80]
max = li[0]
smax = 0
tmax = 0
for i in range(1,len(li)):
    if(li[i] > max):
        tmax = smax
        smax = max
        max = li[i]
    elif(li[i]>smax):
        tmax = smax
        smax = li[i]
    elif(li[i]>tmax):
        tmax = li[i]
print(f"first max is:-{max}")
print(f'second max is:- {smax}')
print(f'third max is:- {tmax}')

# sum of alll elements
