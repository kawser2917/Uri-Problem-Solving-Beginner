j=0
loc = 0
for i in range(0,100):
    element = int(input())
    if(element>j):
        j=element
        loc = i
print(j)
print(loc+1)