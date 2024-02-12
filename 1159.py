while True:
    x = int(input())
    if(x==0):
        break
    if(x%2!=0):
        x+=1
    sum = 0
    for i in range(5):
        sum+=x
        x+=2
    print(sum)