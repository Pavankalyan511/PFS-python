''' nums'''
##for i in range(0,4):
##    for j in range(0,4):
##        print((i,j),end='')
##    print()

'''*'S square pattern'''
##for i in range(0,4):
##    for j in range(0,4):
##        print("* ",end='')
##    print()

##for i in range(5):
##    print("* "*5)

'''Right angle Triangle'''
##for i in range(5):
##    i+=1
##    print("* "*i)

##for i in range(5):
##    for j in range(i+1):
##        print("*",end=' ')
##    print()

'''inverted right angle triangle'''
##for i in range(5,0,-1):
##    for j in range(i):
##        print("*",end='')
##    print()

##for i in range(5,0,-1):
##    print("*"*i)

'''Reversed right angle triangle'''
##n=5
##for i in range(1,n+1):
##    print(' '*((n-i)*2)+"* "*i)

##for i in range(1,6):
##    print(' '*(6-i)+"*"*i)

##n=5
##for i in range(1,n+1):
##    for j in range(i,i+1):
##        print(' '*(n-j)+"*"*i)
##    
    
'''triangle'''
##n=5
##for i in range(1,n+1):
##    print(' '*(n-i)+"* "*i)

##n=int(input())
##for i in range(1,n+1):
##    print(' '*(n-i)+'*'*((2*i)-1))


##n=5
##for i in range(1,n):
##    print(' '*(n-i-1)+'* '*i)

'''inverted triangle'''
##n=5
##for i in range(n,0,-1):
##    print(' '*(n-i)+'* '*i)

##n=int(input())
##for i in range(n,0,-1):
##    print(' '*(n-i)+'*'*((2*i)-1))

'''rhombus'''
##n=5
##for i in range(1,n):
##    print(' '*(n-i)+'* '*i)
##for i in range(n,0,-1):
##    print(' '*(n-i)+'* '*i)

##n=int(input())
##for i in range(1,n):
##    print(' '*(n-i)+'*'*((2*i)-1))
##for j in range(n,0,-1):
##    print(' '*(n-j)+'*'*((2*j)-1))

'''Butterfly'''
##m=int(input())
##for i in range(1,m+1):
##    for j in range(1,m+1):
##        if j==1 or i==j or j==(m+1)-i or j==m:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()

'''Numbers'''
##num=1           
##n=int(input())
##for i in range(1,n):
##    for j in range(i):
##        print(num,end="")
##        num+=1
##    print()

##n=int(input())
##for i in range(0,n):
##    i+=1
##    print(f"{i}"*i)

##num=1           
##n=int(input())
##for i in range(1,n):
##    print(num,end=' ')
##    num+=1
##    for j in range(i+1):


##        print(num,end=' ')
##    print()


'''Hollow Square'''
##n=int(input())
##for i in range(1,n+1):
##    if i==1 or i==n:
##        print("* "*n)
##    else:
##        print("* "+"  "*(n-2)+"*")

##n=int(input())
##for i in range(n):
##    for j in range(n):
##        if i==0 or i==n-1 or j==0 or j==n-1:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()

'''I'''
##n=int(input())
##for i in range(n):
##    for j in range(n):
##        if i==0 or i==n-1  or j==n//2:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()

'''J'''
##n=int(input())
##for i in range(n):
##    for j in range(n):
##        if i==0:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()

'''even indexed odd values'''
n=[1,0,2,0,3,4,5]
##for i in range(len(n)):
##    if i%2==0 and n[i]%2!=0:
##        print(n[i])

'''even indexed even values'''
##for i in range(len(n)):
##    if i%2==0 and n[i]%2==0:
##        print(n[i])


'''dict'''
##d={'a':60,'b':70,'c':45,'d':49}
##for key,value in d.items():
##    if value>=60:
##        print(key)

d={}
for i in range(5):
    name=input()
    phnum=int(input())
    d[name]=phnum
    print(d)
    
