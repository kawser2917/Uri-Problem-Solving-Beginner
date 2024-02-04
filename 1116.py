N = int(input())
for i in range(N):
    x,y = list(map(int,input().split()))
    if(y==0):
        print("divisao impossivel")
    else:
        result = x/y
        print(result)