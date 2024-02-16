x = []
n = float(input())
x.append(n)
for i in range(1,100):
    n = n/2
    x.append(n)
pos = 0
for i in x:
    print(f"N[{pos}] = {i:.4f}")
    pos+=1