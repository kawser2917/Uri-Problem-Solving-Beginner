op = input()
M = []
for i in range(12):
    element = []
    for j in range(12):
        v = float(input())
        element.append(v)
    M.append(element)
sum = 0
for i in range(1,11):
    if(i<=5):
        for j in range(i):
            sum+=M[i][j]
    else:
        for j in range(11-i):
            sum+=M[i][j]
if op.upper() == "S":
    print(f"{sum:.1f}")
elif op.upper() == "M":
    print(f"{(sum/30):.1f}")
    
    