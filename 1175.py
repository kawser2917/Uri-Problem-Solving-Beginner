arr = []
for i in range(20):
    element = int(input())
    arr.append(element)
pos=0
for i in (arr[::-1]):
    print(f"N[{pos}] = {i}")
    pos+=1