N=int(input())
for i in range(1,N+1):
    x,y,z = list(map(float,input().split()))
    avg = (x*2+y*3+z*5)/10
    print(f"{avg:.1f}")
 