X = int(input())
Y = int(input())
start = min(X,Y)+1
end = max(X,Y)
sum = 0
for i in range(start,end):
    if(i%2!=0):
        sum+=i
print(sum)
 