'''write mode'''
##file=open('mrr.txt',mode='w')
###print(dir(file))
##
##l=['hello\n','how are you\n','where are you ']
##file.writelines(l)
##print(file.tell())
##file.write('python')
##print(file.tell())
##print(file.seek(45))
##print(file.write('adding now'))
##print('sucess')
##file.close()

'''read mode'''
##file=open('mrr.txt',mode='r')
##print(file.read())
##print(file.readline())
##content=file.readlines()
##for i in content:
##    print(i)

'''write+'''
##f=open('just.txt','w+')
##f.read()
##f.write('hello mava how are you')
##f.write('i am fine')
##print('success')
##f.close()
##
##f=open('just.txt','w+')
##f.write('completed')
##print('success')
##
##f.close()

'''read+'''
##doc=open('just.txt','r+')
##print(doc.read())
##doc.write('\n mawa loves java')
##print(doc.read())
##doc.close()

##doc=open('just.txt','a+')
##doc.write('end is adding?')
##print(doc.read())
##print(help(doc.read()))
##print('success')
##doc.close()

