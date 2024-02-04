while True:
    count = 0
    sum = 0
    while (count<2):
        x = float(input())
        if(x>=0 and x<=10):
            sum+=x
            count+=1
        else:
            print("nota invalida")
        if(count==2):
            break
    avg = sum/2
    print(f"media = {avg:.2f}")
    t = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        t= int(input())
        if (t == 1 or t== 2):
            break
    if (t == 2):
        break