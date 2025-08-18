k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=' ')
        k += 1
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
        #k += 1
    print()