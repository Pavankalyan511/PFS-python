'''match'''
# import re
# print(help(re.match))
# text='we are learning regular expressions today '
# result=re.match('today',text)
# print(result.start())
# print(result.end())

'''search'''
# import re
# print(help(re.search))
# text='hello hello how are you hello'
# pattern='hello'
# for i in text.split():
#     if re.search(pattern,i):
#         print(i)
# print(re.search(pattern,text))

'''findall'''
# import re
# print(help(re.findall))
# text='hello how are you!hello'
# pattern='hello'
# result=re.findall(pattern,text)
# print(result)

'''finditer'''
# import re
# print(help(re.finditer))
# text='hello how are you! hello'
# pattern='hello'
# for i in re.finditer(pattern,text):
#     print(i.span())

'''sub'''
# import re
# print(help(re.sub))
# text='hello how are you ! hello'
# pattern='hello'
# result=re.sub(pattern,'hi',text)
# print(result)

'''subn'''
# import re
# print(help(re.subn))
# text='hello how are you! hello'
# pattern='hello'
# result=re.subn(pattern,'hi',text)
# print(result)

'''ph num valid or not'''
# import re
# num='9876787612'
# pattern=r'^[6,7,9]+[0-9]{9}'
# if re.fullmatch(pattern,num):
#     print('valid')
# else:
#     print('not valid')

# import re
# text='hello 1 2 3 how are you 12 3 3 4 5'
# pattern=r'[^0-9\W]+'
# print(re.findall(pattern,text))

#import re
# text='python program pro coder paul'
# pattern=r'^[p]+'
# print(re.findall(pattern,text))

#import re
# text="python prgram pro coder paul"
# pattern=r"p\w*"
# print(re.findall(pattern,text))

'''name validation'''
#import re
# text="john"
# pattern=r"[a-zA-z\W]+"
# 
# if re.fullmatch(pattern,text):
#     print("Valid")
# else:
#     print("Not Valid")

'''email validation'''
#import re
#email="pk1@gmail.com"
#pattern=r"^[A-Za-z0-9]{3,}+@[a-z]{5,}+\.[a-z]{2,}"
#
#if re.fullmatch(pattern,email):
#    print("Valid")
#else:
#    print("Not Valid") 

'''password'''
# import re
# pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#%!]).{8,15}$"
# 
# password="Pkrocky1@"
# 
# if re.fullmatch(pattern,password):
#     print("Valid")
# else:
#     print("Not Valid")
