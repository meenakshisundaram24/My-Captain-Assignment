def fibo():
    a=0
    b=1
    print(a,",",b,end=" , ")
    while(True):
        c=a+b
        a=b
        b=c
        print(c,end=" , ")
        
print("The Fibonacci series \n")
fibo()
