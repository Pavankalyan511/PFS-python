


##class phone():
##    ringtone='bham bham bhol'
##lava=phone()
##print(lava.ringtone)
##
##fan=phone()
##print(fan.ringtone)
##fan.ringtone='chal chalo chalooo'
##print(fan.ringtone)
##
##print(lava)
##print(fan)

##class phone():
##    ringtone='bham bham bhool'
##
##    def notification(self):
##        print(self.ringtone)
##obj=phone()
##obj.ringtone='trin trin'
##obj.notification()
##
##obj1=phone()
##obj1.notification()

##class atm():
##    ring='krrrrrrrrrrrrrrrr'
##    def notification(self):
##        print(self.ring)
##obj=atm()
##obj.ring='kir kir kir kir'
##obj.notification()

##class bank():
##    balance=500000000
##    def check(self):
##        print(self.balance)
##obj=bank()
##obj.check()

##class bank:
##    balance=999
##
##    def check(self):
##        print(self.balance)
##
##    def Deposit(This, amount):
##        This.balance+=amount
##
##ac1=bank()
##print(ac1.check())
##ac1.Deposit(199)
##ac1.check()
##
##ac2=bank()
##ac2.Deposit(456)
##ac2.check()

##class Student():
##    def __init__(self,n,m):
##        self.name=n
##        self.marks=m
##
##    def Details(ref):
##        print(ref.name,ref.marks)
##
##    def Grade(ref):
##        if 550<marks<=600:
##            print('A')
##        elif 500<marks<=550:
##            print('B')
##        elif 400<=marks<=500:
##            print('C')
##        else:
##            print('D')
##        
##name=input()
##marks=int(input())
##
##std1=Student(name,marks)
##std1.Details()
##std1.Grade()

##class BankAct():
##    def __init__(self,name,balance):
##        self.name=name
##        self.balance=balance
##    def Info(self):
##        print(self.name,self.balance)
##    def Deposit(self,amount):
##        self.balance+=amount
##        print('amount success credited')
##    def withdraw(self,amount):
##        self.balance-=amount
##ac1=BankAct('rocky',111)
##ac1.Info()
##ac1.Deposit(5000000)
##ac1.withdraw(5000)

##class BankAct():
##    def __init__(self,name,balance):
##        self.name=name
##        self.__balance=balance
##    def Info(self):
##        print(self.name,self.__balance)
##    def Deposit(self,amount):
##        self.__balance+=amount
##        print('amount success credited')
##    def withdraw(self,amount):
##        self.__balance-=amount
##        print(self.__balance)
##ac1=BankAct('rocky',111111)
####ac1.Info()
####ac1.Deposit(5000000)
####ac1.withdraw(5000)
##ac1.__balance=0
##
##print(ac1.__balance)
##ac1.Info()
##
##ac1._BankAct__balance=100   #mangling
##ac1.Info()

##class BankAct():
##    def __init__(self,name,balance):
##        self.name=name
##        self._age=age
##        self.__balance=b        #private
##    def Info(self):
##        print(self.name,self.__balance,self._age)
##    def Deposit(self,amount):
##        self.__balance+=amount
##        print('amount success credited')
##    def withdraw(self,amount):
##        self.__balance-=amount
##        print(self.__balance)
##ac1=BankAct('rocky',111111)
####ac1.Info()
####ac1.Deposit(5000000)
####ac1.withdraw(5000)
##ac1.__balance=0
##
##print(ac1.__balance)
##ac1.Info()
##
##ac1._BankAct__balance=100   #mangling
##ac1.Info()

'''inheritence'''
'''single inheritence'''
##class Parent():
##    def p1(self):
##        print('this is parent class')
##
##class Child(Parent):
##    def c1(self):
##        print('this is child class')
##ch1=Child()
##ch1.c1()
##ch1.p1()
##print()
##P=Parent()
##p.p1()
##p.c1()

'''multilevel inheritence'''
##class Gparent():
##    def gp(self):
##        print("this is grand parent class")
##class Parent(Gparent):
##    def p(self):
##        print("this is parent class")
##class Child(Parent):
##    def c(self):
##        print("this is child class")
##obj=Child()
##obj.c()
####obj.p()
##obj.gp()
##print()
##pobj=Parent()
##pobj.p()
##pobj.gp()

'''multiple inheritence'''
##class Father():
##    def f(self):
##        print("this is father class")
##class Mother():
##    def m(self):
##        print("This is Mother Class")
##class Child(Father,Mother):
##    def c(self):
##        print("This is Child Class")
##obj=Child()
##obj.c()
##obj.f()
##obj.c()
##
##print()
##
##mobj=Mother()
##mobj.f()           #cant access in multiple in heritence

'''Hybrid inheritence'''
##class Father():
##    def f(self):
##        print("This is Father class")
##class Bro1(Father):
##    def b1(self):
##        print("This is 1st bro's class")
##class Bro2(Father):
##    def b2(self):
##        print("This is 2nd bro's class")
##prop=Bro2()
##prop.f()
###prop.b1()  #cant be done
##prop.b2()

##class Student:
##    def __init__(self, name, email, mobile_no, address, course, graduation):
##        self.name = name
##        self.email = email
##        self.mobile_no = mobile_no
##        self.address = address
##        self.course = course
##        self.graduation = graduation
##    def display(self):
##        print("Student Details")
##        print("Name:", self.name)
##        print("Email:", self.email)
##        print("Mobile No:", self.mobile_no)
##        print("Address:", self.address)
##        print("Course:", self.course)
##        print("Graduation:", self.graduation)
##class Trainer:
##    def __init__(self, name, email, mobile_no, address, tech, bank_act):
##        self.name = name
##        self.email = email
##        self.mobile_no = mobile_no
##        self.address = address
##        self.tech = tech
##        self.bank_act = bank_act
##    def display(self):
##        print("Trainer Details")
##        print("Name:", self.name)
##        print("Email:", self.email)
##        print("Mobile No:", self.mobile_no)
##        print("Address:", self.address)
##        print("Technology:", self.tech)
##        print("Bank Account:", self.bank_act)
##class Developer:
##    def __init__(self, name, email, mobile_no, address, skill, bank_act):
##        self.name = name
##        self.email = email
##        self.mobile_no = mobile_no
##        self.address = address
##        self.skill = skill
##        self.bank_act = bank_act
##    def display(self):
##        print("Developer Details")
##        print("Name:", self.name)
##        print("Email:", self.email)
##        print("Mobile No:", self.mobile_no)
##        print("Address:", self.address)
##        print("Skill:", self.skill)
##        print("Bank Account:", self.bank_act)
##class HouseKeeping:
##    def __init__(self, name, mobile, address, work, bank_act):
##        self.name = name
##        self.mobile = mobile
##        self.address = address
##        self.work = work
##        self.bank_act = bank_act
##    def display(self):
##        print("Housekeeping Details")
##        print("Name:", self.name)
##        print("Mobile:", self.mobile)
##        print("Address:", self.address)
##        print("Work:", self.work)
##        print("Bank Account:", self.bank_act)
##student1 = Student("PK","pk@gmail.com","9876543210","vij","B.Tech","2026")
##trainer1 = Trainer("Ravi","ravi@gmail.com","9876543211","Hyderabad","Python","1234567890")
##developer1 = Developer("Kiran","kiran@gmail.com","9876543212","Vijayawada","Python Developer","1234567891")
##housekeeping1 = HouseKeeping("Suresh","9876543213","Bhimavaram","Cleaning","1234567892")
##student1.display()
##print()
##trainer1.display()
##print()
##developer1.display()
##print()
##housekeeping1.display()

'''With Inheritence'''
##class Person():
##    def __init__(self,name,email,mobile,address):
##        self.name=name
##        self.email=email
##        self.mobile=mobile
##        self.address=address
##
##class Students(Person):
##    def __init__(self,name,email,mobile,address,marks,course,graduation):
##        super().__init__(name,email,mobile,address)
##        self.marks=marks
##        self.course=course
##        self.graduation=graduation
##
##    def Info(self):
##        print(self.name,self.email,self.mobile,self.address,self.marks,self.course,self.graduation)
##
##class Trainers(Person):
##    def __init__(self,name,email,mobile,address,bank_act):
##        super().__init__(name,email,mobile,address)
##        self.bank_act=bank_act
##
##    def Info(self):
##        print(self.name,self.email,self.mobile,self.address,self.bank_act)
##
##class Developers(Person):
##    def __init__(self,name,email,mobile,address,skill,bank_act):
##        super().__init__(name,email,mobile,address)
##        self.skill=skill
##        self.bank_act=bank_act
##
##    def Info(self):
##        print(self.name,self.email,self.mobile,self.address,self.skill,self.bank_act)
##
##class sweepers(Person):
##    def __init__(self,name,email, mobile,address,bank_act):
##        super().__init__(name,email,mobile,address)
##        self.bank_act=bank_act
##
##    def Info(self):
##        print(self.name,self.email,self.mobile,self.address,self.bank_act)
##
##student=Students('PK','pk@gmail.com',567890078,'dfadsof',100,'pfs','complelted')
##trainer=Trainers('hacker','hacker@gmail.com',4567890,'fsaddofj',45678987654)
##developer=Developers('praveeth','prav@gmail.com',567890,'uigedfih','pfs,jfs',3456789009)
##sweeper=sweepers('tfgky','hsdhfsdhfs',3456789,'3rfgm',3456789)
##student.Info()
##trainer.Info()
##developer.Info()
##sweeper.Info()

'''polymorphism'''
##class Father:
##    def f(self):
##        print('This is parent class')
##class Mother(Father):
##    def m(self):
##        print('This is mother class')
##class Child(Mother):
##    def c(self):
##        print('Thiss is child class')
##C=Child()
##C.m()
##C.f()
##
##M=Mother()
##M.f()
##        

'''method overriding'''
##class Father:
##    def y1(self):
##        print('this is parent class')
##class Mother():
##    def m1(self):
##        print('this is mother class')
##
##class Child(Father,Mother):
##    def x1(self):
##        print('this is child class')
##c=Child()
##print(Child.mro())  #method resolution order


##class cash:
##    def payment(self):
##        print('payment method is cash')
##class card:
##    def payment(self):
##        print('payment method is card')
##class upi(cash,card):
##    def payment(self):
##        print('payment method is upi')
##
##obj=upi()
##print(upi.mro())   #mro - Method resolution order
##obj.payment()

'''method overloading'''
##class order:
##    def Items(self,*items):
##        print(*items)
##
##c1=order()
##c1.Items('chicken65','mutton Biryani','soft drinks','ice cream')

'''operator overloading'''
##class Main():
##    def __init__(self,balance):
##        self.balance=balance
##
##    def __add__(self,limit):
##        print(self.balance>0)
##
##obj=Main(199)

##class Online:
##    pass
##    def __init__(self,shirt):
##        self.shirt=shirt
##
##    def __add__(self,new):
##        return self.shirt>500
##obj1=Online(300)
##obj2=Online(200)
##
##print(obj1+obj2)
##print(dir(Online()))

'''Abstraction'''
##from abc import ABC,abstractmethod
##class Main(ABC):
##    @abstractmethod
##    def Hello(self):
##        print('hello this is the main class')
##   # @abstractmethod
##    def My(self):
##        print('this is my class')
##class Main2(Main):
##    def Hello(self):
##        print('this is main2 class')
##    def M(self):
##        print('this is wow class')
##obj=Main2()
##obj.Hello()
##obj.My()

'''contact management'''
class Contacts:
    Phno={}
    def Add(self,name,phone):
        if name not in self.Phno:
            if phone not in self.Phno.values():
                self.Phno[name]=phone
                print('contact added successfully')
            else:
                print('number already exist')
        else:
            print('name already exist')
    def View(self):
        print(self.Phno)
c=Contacts()
while True:
    n=int(input())
    if n==1:
        name=input()
        phone=int(input())
        c.Add(name,phone)
    elif n==2:
        c.View()
    elif n==3:
        n=int(input())
        
    
        
