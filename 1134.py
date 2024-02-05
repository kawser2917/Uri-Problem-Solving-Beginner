x=0
y=0
z=0
while True:
    a = int(input())
    if(a==4):
        break
    elif(a==1):
        x+=1
    elif(a==2):
        y+=1
    elif(a==3):
        z+=1
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool: {}".format(x))
print("Gasolina: {}".format(y))
print("Diesel: {}".format(z))