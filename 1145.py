# x,y = list(map(int,input().split()))
# c=1
# if(y<x):
#     x,y=y,x
# for i in range(1,y+1):
#     print(f"{c} {c+1} {c+2}")
#     c+=2
#     if(c==y):
#         break

n1,n2 = list(map(int,input().split()))
cont = 1
for i in range(1,(int((n2/n1))+1)):
    r = ""
    for y in range(n1):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])