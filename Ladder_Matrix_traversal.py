a=[ [1,23,15,8,4],
    [22,2,5,13,7],
    [9,21,18,3,14],
    [16,10,12,20,6],
    [24,19,25,17,11]]

l=[]
for m in range(len(a)):
    c=[]
    x,y=m,0
    while x>=0:
        c.append(a[x][y])
        y+=1
        x=x-1
    l.append(c)
x=len(a)-1
y=1

while y<=x:
    temp=x
    temp2=y
    c=[]
    while temp2 < len(a):
        c.append(a[temp][temp2])
        temp2+=1
        temp=temp-1

    l.append(c)
    y+=1

print(*l,sep="\n")
