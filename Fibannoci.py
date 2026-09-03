##def Fib(n):
##    a,b=0,1
##    for i in range(n+1):
##        print(a,end=' ')
##        a,b=b,a+b
##Fib(int(input()))

##def Fib(n):
##    a,b=0,1
##    i=0
##    while i<n:
##        print(a,end=' ')
##        a,b=b,a+b
##        i+=1
##Fib(int(input()))

##def Fib(a,b,n):
##    if n==0:
##        return
##    else:
##        print(a,end=' ')
##        Fib(b,a+b,n-1)
##Fib(0,1,5)

##def num(n):
##    if n<0:
##        return
##    else:
##        print(n)
##        num(n-1)
##num(int(input()))

'''Factorial using recursion'''
##F=1
##def fact(n):
##    global F
##    if n==0:
##        return
##    else:
##        F*=n
##        fact(n-1)
##fact(int(input()))
##print(F)
        
def Fib(n):
    if n==0:
        return 0
    elif n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
for i in range(
