x = int(input())
y = int(input())
if(y<x):
    x,y=y,x
for i in range(x+1,y):
    if(i%5==2 or i%5==3 and x!=y):
        print(i)