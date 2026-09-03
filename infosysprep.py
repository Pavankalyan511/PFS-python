'''Reversing an array'''
##N=int(input('Enter no.of elements:'))
##arr=list(map(int,input("Enter elements:").split()))
##left=0
##right=N-1
##while left<right:
##    arr[left],arr[right]=arr[right],arr[left]
##    left+=1
##    right-=1
##print("reversed arr:",arr)

'''Palindrome String Check'''
##s=input().lower()
##if s==s[::-1]:
##    print("yes- it is a palindrome")
##else:
##    print("no- it is not a palindrome")

'''Second largest element in the array'''
##N=int(input())
##arr=list(map(int,input("Enter elements in array:").split()))
##largest=s_largest=float("-inf")
##for i in arr:
##    if i>largest:
##        s_largest=largest
##        largest=i
##    elif largest>i>s_largest:
##        s_largest=i
##if s_largest==float("-inf"):
##    print(-1)
##else:
##    print("second largest element:",s_largest)

'''Duplicates in an array'''
##n = int(input())
##arr = list(map(int, input().split()))
##seen = set()
##duplicates = set()
##for num in arr:
##    if num in seen:
##        duplicates.add(num)
##    else:
##        seen.add(num)
##if duplicates:
##    print(*duplicates)
##else:
##    print(-1)

'''left rotate an array by d positions'''
##N=int(input())
##arr=list(map(int, input().split()))
##D=int(input())
##D=D%N
##rotated=arr[D:]+arr[:D]
##print('Rotated:',rotated)

'''Binary search'''
##N=int(input())
##arr=list(map(int, input().split()))
##target=int(input())
##low,high=0,N-1
##result=-1
##while low<=high:
##    mid=(low+high)//2
##    if arr[mid]==target:
##        result=mid
##        break
##    elif arr[mid]<target:
##        low=mid+1
##    else:
##        high=mid-1
##print(result)

'''finding the missing number(1 to N)'''
##N=int(input())
##arr=list(map(int,input().split()))
##expected_sum=N*(N+1)//2       #''' formula for sum of n numbers'''
##actual_sum=sum(arr)
##missing=expected_sum-actual_sum
##print(missing)

'''Fibonacci series up to N terms'''
##N=int(input())
##a,b=0,1
##res=[]
##for i in range(N):
##    res.append(a)
##    a,b=b,a+b
##print(res)

'''factorial of a number using recursion'''
##def factorial(n):
##    if n==0 or n==1:
##        return 1
##    return n*factorial(n-1)
##n=int(input())
##print(factorial(n))

'''checking strings are anagram or not'''
##s1=input()
##s2=input()
##if len(s1)!=len(s2):
##    print("NO")
##else:
##    if sorted(s1)==sorted(s2):
##        print("YES - ANAGRAM")
##    else:
##        print("NO")

'''count vowels and consonents in a string'''
##s=input().lower()
##v_set=set('aeiou')
##v_count=0
##c_count=0
##for ch in s:
##    if ch.isalpha():
##        if ch in v_set:
##            v_count+=1
##        else:
##            c_count+=1
##print(f"vowels={v_count}, consonents={c_count}")

'''check if a number is prime'''
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
##print("yes it is prime"if is_prime else "No it is not a prime")

'''armstrong num'''
##n=input()
##num_digits=len(n)
##total=sum(int(d) ** num_digits for d in n)
##original=int(n)
##if total==original:
##    print("Yes")
##else:
##    print("No")

'''bubble sort'''
##n=int(input())
##arr=list(map(int, input().split()))
##for i in range(n-1):
##    swapped=False
##    for j in range(n-1-i):
##        if arr[j]>arr[j+1]:
##            arr[j], arr[j+1]=arr[j+1], arr[j]
##            swapped=True
##    if not swapped:
##        break
##print("sorted array:",arr)

'''Character Frequency count in a string'''
##s=input()
##freq={}
##for ch in s:
##    freq[ch]=freq.get(ch,0)+1
##res=" ".join(f"{ch}:{count}"for ch,count in freq.items())
##print(res)

'''GCD and LCM of two numbers'''
##a=int(input())
##b=int(input())
##def gcd(x,y):
##    while y:
##        x,y=y,x%y
##    return x
##g=gcd(a,b)
##lcm=(a*b)//g
##print(f"GCD={g}, LCM={lcm}")

'''Two sum problem'''
##n=int(input())
##arr=list(map(int,input().split()))
##target=int(input())
##seen={}
##result=None
##for i, num in enumerate(arr):
##    complement=target-num
##    if complement in seen:
##        result=(seen[complement],i)
##        break
##    seen[num]=i
##if result:
##    print("Indices:",result[0],result[1])
##else:
##    print("No pair found")

'''reversing a linkedlist'''
### Node definition for Singly Linked List
##class Node:
##    def __init__(self, data):
##        self.data = data
##        self.next = None
##
##def build_list(values):
##    """Create a linked list from a list of values and return the head."""
##    if not values:
##        return None
##    head = Node(values[0])
##    current = head
##    for v in values[1:]:
##        current.next = Node(v)
##        current = current.next
##    return head
##
##def reverse_list(head):
##    """Reverse the linked list iteratively using three pointers."""
##    prev = None
##    current = head
##    while current:
##        nxt = current.next   # store next node before breaking the link
##        current.next = prev  # reverse the link
##        prev = current       # move prev forward
##        current = nxt        # move current forward
##    return prev              # prev is the new head
##
##def print_list(head):
##    """Traverse and print the linked list elements formatted with arrows."""
##    values = []
##    current = head
##    while current:
##        values.append(str(current.data))
##        current = current.next
##    print(" -> ".join(values))
##
### Main execution
##if __name__ == "__main__":
##    n = int(input())
##    values = list(map(int, input().split()))
##
##    head = build_list(values)
##    new_head = reverse_list(head)
##    print_list(new_head)

'''Maximum sum subarray of size K(sliding window)'''
##n = int(input("Enter number of elements: "))
##arr = list(map(int, input("Enter elements separated by space: ").split()))
##k = int(input("Enter window size K: "))
##window_sum = sum(arr[:k])
##max_sum = window_sum
##for i in range(k, n):
##    window_sum += arr[i] - arr[i - k]
##    max_sum = max(max_sum, window_sum)
##print("Maximum sum of subarray of size K:", max_sum)

'''Longest common subsequnce(LCS)'''
##s1 = input("Enter first string: ")
##s2 =input("Enter second string: ")
##m, n = len(s1), len(s2)
### dp[i][j] = length of LCS of s1[:i] and s2[:j]
##dp = [[0] * (n + 1) for _ in range(m + 1)]
##for i in range(1, m + 1):
##    for j in range(1, n + 1):
##        if s1[i - 1] == s2[j - 1]:
##            dp[i][j] = dp[i - 1][j - 1] + 1 # characters match, extend LCS
##       else:
##            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # take the better of skipping eithercharacter
##print("Length of LCS:", dp[m][n])

'''coin change DP'''
##coins = list(map(int, input().split()))
##
##amount = int(input("Enter target amount: "))
### dp[a] = minimum coins needed to make amount 'a'; start with "infinity"
##dp = [float('inf')] * (amount + 1)
##dp[] = 0 # zero coins needed to make amount 0
##for a in range(1, amount + 1):
##    for coin in coins:
##        if coin <= a:
##dp[a] = min(dp[a], dp[a - coin] + 1)
##
##result = dp[amount] if dp[amount] != float('inf') else -1

##print("Minimum coins required:", result)

'''Balanced Paranthesis'''
##s = input("Enter a string of brackets: ").strip()
##stack = []
#pairs = {')': '(', ']': '[', '}': '{'}
##
##balanced = True
##for ch in s:
##    if ch in "([{":
##        stack.append(ch) # opening bracket, push onto stack
##    elif ch in ")]}":
##        if not stack or stack[-1] != pairs[ch]:
##            balanced = False # mismatched or empty stack
##            break
##        
##stack.pop()
##if stack:
##    balanced = False

##print("YES - Balanced" if balanced else "NO - Not balanced")



























