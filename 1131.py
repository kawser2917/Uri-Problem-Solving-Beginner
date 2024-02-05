count = 0
inter = 0
gremio = 0
draw = 0
interw =0
gremiow =0
while True:
    x,y = list(map(int, input().split()))
    if(x>y):
        inter+=1
    elif(x<y):
        gremio+=1
    else:
        draw+=1
    interw+=inter
    gremiow+=gremio
    count+=1
    n = int(input("Novo grenal (1-sim 2-nao)\n"))
    if(n==1):
        continue
    if(n==2):
        break
print(f"{count} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{draw}")
if(interw>gremiow):
    print("Inter venceu mais")
elif(interw<gremiow):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
    

        