X = int(input())
inn = 0
out = 0
for i in range(0,X):
    N = int(input())
    if(N>=10 and N<=20):
        inn+=1
    else:
        out+=1
print(f"{inn} in\n{out} out")