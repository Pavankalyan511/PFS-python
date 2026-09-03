import os
class Contact():
    def Create(self,name,phone):
        if os.path.exists('contacts.csv'):
            print('exists')
            if os.path.getsize('contacts.csv')==0:
                print('Checking')
                with open('contacts.csv','w') as file:
                    file.write('Name,Phone_number\n')
                    print('success')
            else:
                with open('contacts.csv','a') as file:
                    data=file.readlines()
                    found=True
                    for i in data[1:]:
                        enames=i.split(',')
                        if name==enames[0]:
                            found=False
                if found==True:
                    with open('contacts.csv','a') as file:
                        file.write(f'{name},{phone}\n')
                        print('success')
                else:
                    print(f'{name} already exists')
    def View(self):
        with open('contacts.csv','r') as file:
                data=file.readlines()
                for i in data:
                    print(i)
c=Contact()
while True:
    num=int(input())
    if num==1:
        name=input()
        phone=int(input())
        c.Create(name,phone)
    elif num==2:
        c.View()
