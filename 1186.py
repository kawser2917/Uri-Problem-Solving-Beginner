op = input()
M = []
for i in range(12):
    element = []
    for j in range(12):
        v = float(input())
        element.append(v)
    M.append(element)
sum=0
n=11
for i in range(1,12):
    for j in range(n,12):
        sum+=M[i][j]
    n-=1
if op.upper() == "S":
    print(f"{sum:.1f}")
elif op.upper() == "M":
    print(f"{(sum/66):.1f}")