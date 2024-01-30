sum = 0
total=0
avg=0
for i in range(0,6):
    n = float(input())
    if(n>=0):
        total+=n
        sum+=1
        avg = total/sum
print(f"{sum} valores positivos\n{avg:.1f}")