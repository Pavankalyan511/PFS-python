'''defining working of function'''
'''Void functions'''#will print value not return the value
##def Greet(name):
##    print(f"Hello {name} take some break")
##Greet(input())
##Greet(input())

'''user input()'''
##def Greet(name):
##    print(f"Hello {name} take some break")
##Greet(name=input())
##Greet(name=input())

'''positionl argument'''    #'It should follow the positional order'
##def Details(name,marks):
##    print(name)
##    print(marks)
##Details("PK",511)     '''User input()= Details(input(),int(input())'''

'''keyword argument'''
##def Details(name,marks):
##    print(name)
##    print(marks)
##Details(marks=511,name="PK")

'''Default argument'''
##def Details(name, marks,place=Vijawada):
##    print(name)
##    print(marks)
##    print(place)
##Details("Kalyan babu",511)  #'''Here place will be taken by default as the given place value'''
##print()
##Details(marks=511,name="Rocky",place="Bezawada")  #user input()= Details(marks=int(input()),name=input(),place=input())
    

##def Login(name,password):
##    print(name)
##    print(password)
##def Register(name,email,password):
##    print(name)
##    print(email)
##    print(password)
##while True:
##    print("1.Login \n 2.Register")
##    n=int(input("Choose Option"))
##    name_user="Pavan"
##    password_user="pkr"
##    if n==1:
##        name=input('enter name:')
##        if name==name_user:
##            password=input('enter password:')
##            if password==password_user:
##                print("welcome")
##            else:
##                print("wrong pass")
##        else:
##            print("no user name")
##            break
##        Login(name,password)
##        break
##    else:
##        name=input("Enter your name:")
##        email=input("Enter your email")
##        password=input("Set your password")
##        Register(name,email,password)
##        break

'''* argument'''
##def Total(*args):          # we have to use this when we want to take n no.of items/data
##    print(args)
##    print(sum(args))
##Total(10,20,30,12,10,1,1,2)

'''Non void Function'''
##def Total(*args):
##    return args,sum(args)
##values,sum=Total(10,20,30,12,10,1,1,2)
##print(values)
###print(sum)
##print(values[0:4])


##def Order(table,*items):
##    print(f"table:{table}")
##    print(f"items:{items}")
##table=int(input())
##i=tuple(input().split())
##Order(table,i)

def Online(**kwargs):
    print(kwargs)
Online(pizza=1,onions=2,sauce=3)

