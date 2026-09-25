# l=list(map(str,input().split()))  #[left, right, left]
# current='North'
# for i in l:
#     if current=='North':
#         if i=='left':
#             current='West'
#         else:
#             current='East'
#     elif current=='West':
#         if i=='left':
#             current='South'
#         else:
#             current='North'
#     elif current=='South':
#         if i=='left':
#             current='East'
#         else:
#             current='West'
#     elif current=='East':
#         if i=='left':
#             current='North'
#         else:
#             current='South'
#             
# print(current)
li=list(map(str,input()))
l=['North', 'east', 'south', 'west']
x=l[0]
position=0
for i in li:
    if i=='left':
        position-=1
    else:
        position+=1
    position=position%4
    
    x=l[position]
print(x)

