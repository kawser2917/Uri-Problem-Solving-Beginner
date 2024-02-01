N=int(input())
for i in range(0,N):
    num = int(input())
    if(num>0 and num%2==0):
        print("EVEN POSITIVE")
    elif(num<0 and num%2==0):
        print("EVEN NEGATIVE ")
    elif(num>0 and num%2!=0):
        print("ODD POSITIVE")
    elif(num<0 and num%2!=0):
        print("ODD NEGATIVE")
    else:
        print("NULL")