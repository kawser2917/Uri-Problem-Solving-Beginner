list_num = list(map(int,input().split()))
a = list_num[0]
n = 0
sum=0
for i in range(1,len(list_num)):
    b = list_num[i]
    if(b>0):
        n=b
        break
for i in range(n):
    sum+=i+a
print(sum)
