##def Add(a,b):
##    return a+b
##if __name__=="__main__":
##    print(Add(10,20))

#print((lambda a,b:a*b)(10,12))

'''normal function'''
##def eo(a):
##    if a%2==0:
##        return "even"
##    else:
##        return "odd"
##print(eo(int(input())))

'''lambda function'''
#print((lambda a:'even' if a%2==0 else 'odd')(int(input())))

'''squares with map'''
##def Square(l):
##    values=[]
##    for i in l:
##        values.append(i*i)
##    return values
##res=Square(list(map(int,input().split())))
##print(res)

''' squares of ele in list in map'''
##l=list(map(int,input().split()))
##print(list(map(lambda l:l**2,l)))

'''even or odd in map'''
##l=list(map(int,input().split()))
##print(list(map(lambda l:'even' if l%2==0 else 'odd',l)))

##l=['a','b','c','d','e']
##res=map(lambda l:l.upper(),l)
##print(set(res))

##prices=[1000,2000,3000,990,800,190]
##res=filter(lambda prices:prices if prices<=1000 else None, prices)
##print(res)

##v=[0,10,2,1,7,12,2]
##print(sorted(v,key=lambda v:v))

##from functools import reduce
##l=[1,2,3,4,5]
##print(reduce(lambda a,b:a+b,l))

##l=['ahalya','amruth','amma','annad','pk']
##for i in l:
##    for j in i:
##        if j[0]=='a':
##            print(i,end='')
##            break
##    print()

##l=['ahalya','amruth','amma','annad','pk']
##li=[]
##for i in l:
##    if i.startswith('a'):
##        li.append(i)
##    else:
##         li.append(None)
##print(li)

##l=['ahalya','amruth','amma','annad','pk']
##final=[i if i.startswith('a') else None for i in l]
##print(final)

'''multiple lists to single list'''
##l=[[1,2],[3,4],[5,6]]
##final=[]
##for i in l:
##    for j in i:
##        final.append(j)
##print(final)

##l=[[1,2],[3,4],[5,6]]
##result=[j for i in l for j in i]
##print(result)

##l=[]
##for i in range(5):
##    for j in range(3):
##        l.append([i,j])
##print(l)
##result=[]
##print(result)

##l=[]
##res=[l for i in range(5) for j in range(3)]
##print(res)
