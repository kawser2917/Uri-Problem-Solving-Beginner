NOTES = float(input())
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(NOTES/100)))
remaining = (NOTES%100)
print("{} nota(s) de R$ 50.00".format(int(remaining/50)))
remaining = (remaining%50)
print("{} nota(s) de R$ 20.00".format(int(remaining/20)))
remaining = (remaining%20)
print("{} nota(s) de R$ 10.00".format(int(remaining/10)))
remaining = (remaining%10)
print("{} nota(s) de R$ 5.00".format(int(remaining/5)))
remaining = (remaining%5)
print("{} nota(s) de R$ 2.00".format(int(remaining/2)))
remaining = (remaining%2)
print("MOEDAS:")
A = NOTES*100
B = int(A)
print("{} moeda(s) de R$ 1.00".format(int(remaining)))
C = B%100
print("{} moeda(s) de R$ 0.50".format(int(C/50)))
C = (C%50)
print("{} moeda(s) de R$ 0.25".format(int(C/25)))
C = (C%25)
print("{} moeda(s) de R$ 0.10".format(int(C/10)))
C = (C%10)
print("{} moeda(s) de R$ 0.05".format(int(C/5)))
C = (C%5)
print("{} moeda(s) de R$ 0.01".format(int(C/1)))









 
 