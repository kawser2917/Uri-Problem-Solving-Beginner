op = input()
M = []
for i in range(12):
    element = []
    for j in range(12):
        v = float(input())
        element.append(v)
    M.append(element)
sum = 0
n = 1
for k in range(12):
    for l in range(n,12):
        sum +=M[k][l]
    n+=1
if (op.upper()== "S"):
    print(f"{sum:.1f}")
elif(op.upper() == "M"):
    print(f"{(sum/66.0):.1f}")