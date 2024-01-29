x,y = map(int,input().split())
if(x<y):
    time = y-x
else:
    time = (y+24)-x
print(time)