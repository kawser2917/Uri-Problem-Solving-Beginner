'''
x = []
n = int(input())
for i in range(n):
    num = int(input())
    x.append(num)
low = x[i]
for i in x:
    if i<low:
        low = i
pos = 0
for j in x:
    if(j!=low):
        pos+=1
    else:
        break
print(f"Menor valor: {low}")
print(f"Posicao: {pos}")
'''
n = int(input())
lista = list(map(int,input().split()))
p=0
l=lista[0]
count = 0
for i in lista:
    if(i<l):
        l = i
        p = count
    count+=1
print(f"Menor vlor: {l}")
print(f"Posicao: {p}")
    