a,b,c,d = map(int,input().split())
# converting hour into minute minute 
diff = (((c*60)+d)-((a*60)+b))
if(diff<=0):
    diff+= 24*60
    # converting a day into minute
hours = diff//60
minute = diff%60
print(f"O JOGO DUROU {hours} HORA(S) E {minute} MINUTO(S)")