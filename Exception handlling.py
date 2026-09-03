'''Exception handling'''
##try:
##    a=20
##    print(x)
##except NameError:
##    print('varialbe not defined')
##else:
##    print('executed')
##finally:
##    print('done')

##try:
##    a=20
##    print(a//0)
##except ZeroDivisionError:
##    print('value should not divisible by 0')
##else:
##    print('executed')
##finally:
##    print('done')

##try:
##    a=int(input())
##except ValueError:
##    print('check the value')
##else:
##    print('executed')
##finally:
##    print('done')

##try:
##    a=[1,2,3,4]
##    print(a[7])
##except IndexError:
##    print('Access only in range')
##else:
##    print('executed')
##finally:
##    print('done')

##try:
##    a=20
##    print(x)
##except :
##    print("seyrdy")
##else:
##    print('executed')
##finally:
##    print('done')

try:
    f=open('oops.py')
    try:
        f.write('pk')
    except:
        print('something went wrong in writing in file')
    finally:
        print('Done')
except:
    print('something went wrong in opening file')
finally:
    print('Done')
