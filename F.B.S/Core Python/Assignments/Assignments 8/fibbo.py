def fibbo(n, a , b):
    if(n > 0):
        c = a + b
        print (c)
        fibbo(n-1,b,c)

n = int(input("Entert the number:- "))
a = 1
b = 0
fibbo(n,a,b)