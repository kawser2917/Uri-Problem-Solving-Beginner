while(True):
    try:
        a,b=list(map(int,input().split()))
        if(a>b):
            a,b=b,a
        if(a<=0 or b<=0):
            break
        else:
            sum=0
            result = ''
            for i in range(a,b+1):
                result += str(i)+' '
                sum = sum + i
            result+= 'Sum=%d'
            print(result %sum)
    except EOFError:
        break