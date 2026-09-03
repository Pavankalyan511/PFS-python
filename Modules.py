##import sys
##
##print(sys.platform)
##
##print(sys.getsizeof(12345.67890))
####print(sys.executable)
####print(sys.exit())
##print(sys.argv)
##print(sys.api_version)
##print(sys.version)

##import random
##print(random.randint(1,10))
##print(random.random())
##print(random.randrange(1,10,2))
##
##name=['a','b','c']
##print(random.choice(name))
##print(random.choices(name,k=2))
##print(random.sample(name,k=2))
##
##random.shuffle(name)
##print(name)
##random.seed()

##import random
##u=0
##m=0
##for i in range(3):
##    k=random.randint(1,10)
##    print(k)
##    p=int(input())
##    if p==k:
##        u+=1
##    else:
##        m+=1
##print("user score:",u)
##print("machine score:",m)

##import random
##otp=''
##for i in range(4):
##    otp+=str(random.randint(1,9))
##print(otp)

##import random
##otp=''
##for i in range(4):
##    otp+=str(random.randint(1,9))
##for j in range(4):
##    otp+=chr(random.randint(ord('A'),ord('Z')+1))
##print(otp)

##import random
##otp=[]
##x=['a','b','c','d','e','f']
##for i in range(4):
##    otp.append(str(random.randint(1,9)))
##for i in range(4):
##    otp.append(random.choice(x))
##random.shuffle(otp)
##print(''.join(otp))

##import random
##otp=0
##for i in range(3):
##    o=random.randint(1000,9999)
##    print(o)
##    g=int(input())
##    if otp<=3:
##        if o==g:
##            otp+=1
##            print('correct')
##            break
##        else:
##            otp+=1
##            print('wrong')
##    else:
##        print('you have failed all attempts try again later')

'''datetime'''
##from datetime import datetime
##print(datetime(2026,8,19,12,59,00))
##just=datetime.now()
##print(just.hour)
##print(just.minute)
##print(just.year)

##from datetime import datetime
##just=datetime.now()
##print(just)
##print(just.strftime('%y/%m/%d'))
##print(just.strftime('%Y--%B--%D'))
##print(just.strftime('%d--%b--%Y'))

##from datetime import date
##help(date)
##just=date.today()
##print(just.year)
##print(just.strftime('%D'))



##from datetime import time
##time='11-44-23'
##print(time.strptime(time,'%H/%m/%d'))


