def fibbo(n , a , b):
    if(n > 0):
        c = a + b
        print(c)
        fibbo(n - 1, b , c)

num = int(input("Enter the number:- "))
a = -1
b = 1
fibbo(num , a, b)