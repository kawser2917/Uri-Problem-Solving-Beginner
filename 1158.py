n = int(input())
for i in range(n):
    x,y = list(map(int,input().split()))
    sum = 0
    if(x%2==0):
        x+=1
    for j in range(0,y):
        sum += x
        x+=2
    print(sum)