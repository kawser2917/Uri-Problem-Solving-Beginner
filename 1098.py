a=0
b=0
i=0
while(i<=2):
    for j in range(1,4,1):
        if((i>0 and i<1) or (i>1 and i<2)):
            print(f"I={i:.1f} J={i+j:.1f}")
        else:
            a = int(i)
            b = int(i+j)
            print(f"I={a:.0f} J={b:.0f}")
    i+=0.2