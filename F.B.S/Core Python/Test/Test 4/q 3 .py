def pattern(n):
     
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i == 1 or i == 6 or j + i == n+1):
                print('*',end=' ')
            else:
                print(" ",end=' ')

        print()
n = int(input("Enter the n:- "))
pattern(n)
#for i in range(1,n+2):
   
