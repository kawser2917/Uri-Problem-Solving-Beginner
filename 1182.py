M = []
l = int(input())
op = input()
sum = 0
for i in range(12):
    element = []
    for j in range(12):
        v = float(input())
        element.append(v)
    M.append(element)

for i in range(12):
    sum += M[i][l]
if(op.upper() == "S"):
    print(f"{sum:.1f}")
else:
    print(f"{(sum/12):.1f}")