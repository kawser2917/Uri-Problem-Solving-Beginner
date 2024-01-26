n1,n2,n3 = list(map(int,input().split()))
if(n1<n2 and n1<n3):
    if(n2<n3):
        print(f"{n1}\n{n2}\n{n3}")
    else:
        print(f"{n1}\n{n3}\n{n2}")
if(n2<n1 and n2<n3):
    if(n1<n3):
        print(f"{n2}\n{n1}\n{n3}")
    else:
        print(f"{n2}\n{n3}\n{n1}")
if(n3<n1 and n3<n2):
    if(n1<n2):
        print(f"{n3}\n{n1}\n{n2}")
    else:
        print(f"{n3}\n{n2}\n{n1}")
print()
print(f"{n1}\n{n2}\n{n3}")