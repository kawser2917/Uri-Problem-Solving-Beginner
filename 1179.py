par = []
impar = []
for i in range(15):
    n = int(input())
    if (n % 2 == 0):
        par.append(n)
    else:
        impar.append(n)

    if (len(par) == 5):
        x = 0
        for v in par:
            print(f"par[{x}] = {v}")
            x += 1
        par = []
    if (len(impar) == 5):
        x = 0
        for v in impar:
            print(f"impar[{x}] = {v}")
            x += 1
        impar = []
if (len(impar) > 0):
    x = 0
    for v in impar:
        print(f"impar[{x}] = {v}")
        x += 1

if (len(par) > 0):
    x = 0
    for v in par:
        print(f"par[{x}] = {v}")
        x += 1
 
    