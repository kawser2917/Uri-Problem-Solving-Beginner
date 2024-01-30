even=0
odd=0
positive=0
negative=0
for i in range(0,5):
    n = int(input())
    if(n%2==0):
        even+=1
    elif(n%2!=0):
        odd+=1
    if(n>0):
        positive+=1
    elif(n<0):
        negative+=1
print(f"{even} valor(es) par(es)\n{odd} valor(es) impar(es)\n{positive} valor(es) positivo(s)\n{negative} valor(es) negativo(s)")