x = int(input())
z = int(input())
while (z<=x):
    z = int(input())
sum = 0
count = 1
for i in range(x,z):
    sum+=i
    if(sum<z):
        count+=1
print(count)
    