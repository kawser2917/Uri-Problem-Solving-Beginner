sal = float(input())
if(sal>=0 and sal<=400):
    percent = (15*sal)/100
    newsal = sal + percent
    perincrement = 15
elif(sal>400 and sal<=800):
    percent = (12*sal)/100
    newsal = sal + percent
    perincrement = 12
elif(sal>800 and sal<=1200):
    percent = (10*sal)/100
    newsal = sal + percent
    perincrement = 10
elif(sal>1200 and sal<=2000):
    percent = (7*sal)/100
    newsal = sal + percent
    perincrement = 7
else:
    percent = (4*sal)/100
    newsal = sal + percent
    perincrement = 4
print(f"Novo salario: {newsal:.2f}\nReajuste ganho: {percent:.2f}\nEm percentual: {perincrement} %")