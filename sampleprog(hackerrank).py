l=[]
x,y,z,a=1,1,1,2
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=a:
                print([i,j,k])
