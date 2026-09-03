##def Gen():
##    yield 1
##    yield 23
##    yield 3
##    yield 100
##res=Gen()
####print(next(res))
####print(next(res))
####for i in range(5):
####    print(next(Gen()))

##for i in range(l):
##    #print(next(result))
##    print(result._next_()) #dunder method

##x=tuple(i for i in range(5))
##print(x)

##emails=['abc@gmail.com','xyz@gmail.com','n@yahoo.com','m@yahoo.com']
##res=tuple(i if i.endswith('@gmail.com') else False for i in emails )
##print(res)

##n=input()
##p={x:n.count(x) for x in n}
##print(p)

##word=input()
##vowels='aeiou'
##p={char:word.count(char) for char in word if char in vowels}
##print(p)

##x=[1,2,3,4,5]
##p={i:x[i]**2 for i in range(len(x))}
##print(p)

##x=[[1,'a'],[2,'b'],[=#res={i[0]:i[1] for i in x}
##print(res)

##students={'lavanya':[80,60,90],'narmada':[99,77,44],'mahalakshmi':[97,55,65]}
##p={i:{'total': sum(students[i])} for i in range(len(students))}
##print(p)

##x=[1,2,3,4]
##for i in range(len(x)):
##    print(i)

##x=[1,2,3,4]
##for ind,v in enumerate(x):
##    print(ind,v)
##
##y=['a','b','c','d','e']
##print(dict(zip(x,y)))
