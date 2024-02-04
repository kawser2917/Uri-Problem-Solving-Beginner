count = 0
sum = 0
while True:
    x = float(input())
    if(x>=0 and x<=10):
        sum+=x
        count+=1
    else:
        print("nota invalida")
    if(count==2):
        break
avg = sum/2
print("media = {}".format(avg))