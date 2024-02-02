n = int(input())
c = 0
r = 0
s = 0
for i in range(n):
    n2,ch = list(map(str,input().split()))
    num = int(n2)
    if(ch == "C"):
        c+=num
    elif(ch == "R"):
        r+=num
    else:
        s+=num
total = c+r+s
PercentualCoelhos = (c*100)/total
PercentualRatos = (r*100)/total
PercentualSapos = (s*100)/total
print("Total: {} cobaias".format(total))
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {PercentualCoelhos:.2f} %")
print(f"Percentual de ratos: {PercentualRatos:.2f} %")
print(f"Percentual de sapos: {PercentualSapos:.2f} %")