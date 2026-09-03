'''reversing a num'''
##n=int(input())
##original=n
##rev=0
##while n>0:
##    digit=n%10
##    rev=rev*10+digit
##    n//=10
##print(rev)

'''palindrome num'''
##num=int(input())
##original_num=num
##rev_num=0
##while num>0:
##    digit=num%10
##    rev_num=rev_num*10+digit
##    num=num//10
##if original_num==rev_num:
##    print("palindrome")
##else:
##    print("not a palindrome")

'''palindrome string'''
##str=input().lower()
##if str==str[::-1]:
##    print("Palindrome")
##else:
##    print("Not a palindrome")

'''fibonaaci'''
##n=int(input())
##a,b=0,1
##res=[]
##for i in range(n):
##    res.append(a)
##    a,b=b,a+b
##print(res)

'''factorial'''
##def fact(n):
##    if n==0 or n==1:
##        return 1
##    else:
##        return n*fact(n-1)
##print(fact(int(input())))

'''prime'''
##n=int(input())
##is_prime=True
##if n<=1:
##    is_prime=False
##else:
##    i=2
##    while i*i<=n:
##        if n%i==0:
##            is_prime=False
##            break
##        i+=1
##    if is_prime:
##        print("prime")
##    else:
##        print("not a prime")

'''armstrong num'''
##n=int(input())
##temp=n
##count=0
##while temp>0:
##    count+=1
##    temp=temp//10
##temp=n
##armstrong_num=0
##while temp>0:
##    digit=temp%10
##    armstrong_num=armstrong_num+digit**count
##    temp=temp//10
##if n==armstrong_num:
##    print("Armstrong num")
##else:
##    print("Not an Armstrong num")

'''max ele in list'''
##l=list(map(int,input().split()))
##largest=0
##for num in l:
##    if num>largest:
##        largest=num
##print(largest)

##for i in range(1,6):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    print()

##for i in range(4,0,-1):
##    for j in range(i,5):
##        print(j,end=' ')
##    print()

##for i in range(1,5):
##    for j in range(i):
##        print(chr(65+j),end="")
##    print()

##for i in range(68,64,-1):
##    for s in range(i-65):
##        print(" ", end="")
##    for j in range(i,69):
##        print(chr(j),end="")
##    print()

##n=int(input())
##for i in range(1,n+1):
##    print(" "*(n-i)+"*"*(2*i-1))


def print_letter(char):
    for r in range(7):
        for c in range(5):
            if char == "P":
                cond = (
                    c == 0
                    or (c == 4 and (r == 1 or r == 2))
                    or ((r == 0 or r == 3) and c < 4)
                )
            elif char == "A":
                cond = ((c == 0 or c == 4) and r != 0) or (
                    (r == 0 or r == 3) and (0 < c < 4)
                )
            elif char == "V":
                cond = (
                    ((c == 0 or c == 4) and r < 5)
                    or (r == 5 and (c == 1 or c == 3))
                    or (r == 6 and c == 2)
                )
            elif char == "N":
                cond = c == 0 or c == 4 or (r == c)
            elif char == "K":
                cond = c == 0 or (r + c == 4) or (r - c == 2)
            elif char == "L":
                cond = c == 0 or r == 6
            elif char == "Y":
                cond = ((r == c or r + c == 4) and r <= 2) or (
                    c == 2 and r > 2
                )
            else:
                cond = False
            print("*" if cond else " ", end=" ")
        print()
    print(" " * 15) 
name = input().upper()
for letter in name:
    print_letter(letter)

