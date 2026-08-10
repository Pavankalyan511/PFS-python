''' salary prog using  conditional statements, for loop'''
##user_data={'ravi':50000,'teja':70000,'ajay':90000}
##highest=None
##lowest=None
##total=0
##no_of_emp=0
##for i,j in user_data.items():
##    if (highest is None) or (highest<j):
##        highest=j
##    if (lowest is None)or lowest> j:
##        lowest=j
##    total=total+j
##    no_of_emp=no_of_emp+1
##average=total//no_of_emp
##print(f"highest salary:{highest} lowest salary:{lowest} average:{average}")

'''cricket score prog'''
##x=int(input())
##over=list(map(int,input().split()))
##boundaries=0
##dot=0
##total=0
##for i in over:
##    total=total+i
##    if i>4:
##        boundaries+=1
##    if i==0:
##        dot+=1
##print(f"total:{total} Boundaries:{boundaries} Dot balls:{dot}")

''' seperating mail domains'''
##l=['abc@gmail.com','admin@gmail.com']
##for i in l:
##    print(i.split('@')[1])

##x=int(input())
##l1=list(map(str,input().split()))    
##for i in l1:
##    print(i.split('@')[1])

'''Atm pin blocks'''
##max_attempts=3
##pin="1234"
##attempts=0
##while attempts<max_attempts:
##    user_input=input('Enter pin:')
##    if user_input==pin:
##        print("Access Granted")
##        break
##    else:
##        attempts+=1
##        print(f'''Invalid pin num,no.of attempts left:{max_attempts-attempts}''')
##else:
##    print("card blocked")

'''number guessing'''
##Num=25
##attempts=0
##while Num!=0:
##    x=int(input('Guess the num:'))
##    if x==Num:
##        print('Correct')
##        break
##    elif x>Num:
##        attempts+=1
##        print("Wrong num,too high")
##    else:
##        attempts+=1
##        print('Wrong num,too low')
    
x='python'
##lifes=3
##while lifes>0:
##    y=input().lower()
##    if y==x:
##        print('win')
##        print(f'no.of lifes remaining:{lifes-1}')
##        break
##    else:
##        lifes-=1
##        print('try again')
##        print('no.of lifes remaining:',lifes)
##else:
##    print('you lost')
              
