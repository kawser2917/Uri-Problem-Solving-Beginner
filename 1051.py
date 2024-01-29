sal = float(input())
if(sal>2000 and sal<=3000):
    tsal = sal-2000
    tax = (8*tsal)/100
    print(f"R$ {tax:.2f}")
elif(sal>3000 and sal<=4500):
    tsal = sal-2000
    if(tsal>=1000):
        remainsal = tsal-1000
        firsttax = (8*1000)/100
        tax = ((18*remainsal)/100) + firsttax
        print(f"R$ {tax:.2f}")
elif(sal>4500):
    tsal = sal-2000
    if(tsal>=1000):
        remainsal1 = tsal-1000
        firsttax=(8*1000)/100
        if(remainsal1>=1500):
            remainsal2 = remainsal1-1500
            secondtax = (18*1500)/100
            tax = ((28*remainsal2)/100)+firsttax+secondtax
            print(f"R$ {tax:.2f}")
else:
    print("Isento")