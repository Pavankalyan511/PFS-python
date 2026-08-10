##l1=["abc@gmail.com","xy@gmail.com","pq@gmail.com"]
##print("1.Register\n 2.Withdraw\n 3.Deposit")
##x=int(input())
##amount=10000
##if x==1:
##    email=input()
##    email.endswith("@gmail.com")
##    l1.append(email)
##    print("Successfully registered")
##    print("l1")
##elif x==2:
##    withdraw=int(input())
##    #amount-=withdraw
##    #print("sucess")
##    if withdraw>amount:
##        print(" Not Possible")
##    elif withdraw%100==0:
##        amount-=withdraw
##        print(amount)
##    
##        
##

##x=int(input("Enter distance(km):"))
##if x>1 and x<=5:
##    cost=x*5
##    print(cost)
##elif x>=6 and x<=12:
##    cost=25+(x-6)*6
##    print(cost)
##elif x>=13 and x<=20:
##    cost=25+42+(x-12)*10
##    print(cost)
##elif x>=21 and x<=30:
##    cost=25+42+80+(x-20)*12
##    print(cost)
##elif x>30:
##    print("ride not possible")


##coupon=["first","second","third"]
##x=int(input("Enter distance(km):"))
##if x>1 and x<=5:
##    cost=x*5
##    print(cost)
##elif x>=6 and x<=12:
##    cost=25+(x-6)*6
##    print(cost)
##elif x>=13 and x<=20:
##    cost=25+42+(x-12)*10
##    print(cost)
##elif x>=21 and x<=30:
##    cost=25+42+80+(x-20)*12
##    print(cost)
##elif x>30:
##    print("ride not possible")
##if x<=30:
##    offer=input().lower()
##    if offer in coupon:
##        if offer=="first":
##            cost=cost-(15/100)*cost
##            print(cost)
##        elif offer=="second":
##            cost=cost-(10/100)*cost
##        else:
##            cost=cost-(5/100)*cost
##            

##x=input()
##college=input("college:").lower()
##if college=="yes":
##    block=input("block:").lower()
##    if block=="yes":
##        floor=input("floor:").lower()
##        if floor=="yes":
##            classroom=input("classroom:").lower()
##            if classroom=="yes":
##                print("He is in classs")
##            else:
##                print("he is in the floor")
##        else:
##            print("he is in the block")
##    else:
##        print("he is in the college")
##else:
##    print("Not in the College")


##a=int(input())
##b=int(input())
##c=int(input())
##if a!=b and b!=c:
##    if a>b and a>c:
##        print("greatest:",a)
##    elif b>a and b>c:
##        print("greatest:",b)
##    else:
##        print("greatest:",c)


''' Dictionary concept '''
''' creating dictionary '''
##employee_details={511:"pavan",512:"kalyan",513:"rocky"}
##print(employee_details[511])

##rapido_booking={1:"bike",2:"auto",3:"car"}
##print(rapido_booking[1])

##rapido_booking={1:"bike",2:"auto",3:"car"}
##print(rapido_booking[5])

##rapido_booking={1:"bike",2:"auto",3:"car"}
##print(rapido_booking.get(5))

''' updating dictionary'''
##rapido_booking={1:"bike",2:"auto",3:"car"}
##rapido_booking[2]="autos"
##print(rapido_booking)

##rapido_booking={1:"bike",2:"auto",3:"car"}
##rapido_booking[4]="minibike"
##print(rapido_booking)

##rapido_booking={1: 'bike', 2: 'auto', 3: 'car'}
##rapido_booking.update({4:'minibike'})
##print(rapido_booking)

##rapido_booking={1: 'bike', 2: 'auto', 3: 'car', 4: 'minibike'}
##rapido_booking.update({5:'miniauto',6:'minicar'})
##print(rapido_booking)

''' defining multiple key's for a single value'''
##student_details={('Tel',101):20, ('hin',101):25,('tel',102):34}
##print(student_details[('hin',101)])

''' defining multiple values to a single key'''
##student_details={101:[20,50],102:[50,60]}
##print(student_details[102])

##student_data={'101':'sam','102':'ram'}
##print(student_data['102'])
##print(student_data.get('102'))
##print(student_data['105'])
##print(student_data.get('105'))

##student_data={'101':'sam','102':'ram'}
##student_data['101']='sam kumar'
##student_data.update({'102':'rama sama'})
##student_data.update({'103':'ali baba'})
##print(student_data)

''' .setdefault()'''
##student_data={'ram':45,'sam':89}
##student_data.setdefault('kali',90)
##student_data.setdefault('ram',90)
##print(student_data)

##d={'101':{'name':'sam','salary': 30000, 'role': 'python developer'}, '102':{'name':'ram','salary':50000,'role':'java developer'}}
##print(d)
###d.popitem()
###d.pop('101')
##d.clear()
##print(d)

''' view methods'''
##d={'name':'sam','marks':30}
##print(d.keys())
##print(d.values())
##print(d.items())
##print(d)
##d2=d.copy()#shallow copy- wont change the value or keys of original when update done in the copy 
##print(d2)
##d2['name']='sam kumar'
##print(d2)
##print(d)

##d={1:1,2:4,3:9,4:16}
##print(d.fromkeys([5,6,7]))
##print(d.fromkeys([5,6,7],25))

''' control statements- loops'''
##l=[1,2,3,3,5,6,7,8,9,10]
##for i in l:
##    print(i)

##data={'101':{'name':'sam','salary':20000},'102':{'name':'ram','salary':50000}}
##for i in data:
##    print(i)
##    print(data[i]['name'])
##    print(data[i]['salary'])
##

''' for loop in set'''
##s={2,4,5,6,3,1,7,9}
##for i in s:
##   print(i)

##s={"good","work","keep","it","up"}
##for i in s:
##    print(i)

'''for loop in list'''
##l=[1,2,3,4,5,6,7,8,9,10]
##for i in l:
##    if i%2==0:
##        print(i)
##

##s=[1,3,45,2,45,67,34]
##num=45
##count=0
##for i in s:
##    if i==num:
##        count+=1
##print(count)

##for i in range(0,5,2):
##    print(i)

##for i in range(4,1,-1):
##    print(i)

##Num=int(input())
##attempts=0
##for i in range(1,4):
##    guessed_num=int(input('Enter a num:'))
##    if Num==guessed_num:
##        print('lucky')
##        attempts+=1
##        break
##    else:
##        print('unlucky')
##        attempts+=1
##print("Your attempts are completed")

#print even numbers between 1 to 100
#print sum of 1 to 20 numbers
#print reverse of 1 to 50 numbers

##for i in range(1,101):
##    if i%2==0:
##        print(i)

##sum=0
##for i in range(1,21):
##    sum+=i
##print(sum)

##for i in range(50,0,-1):
##    print(i)



