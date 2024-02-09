avg = 0
count = 0
while True:
    age = int(input())
    if(age>0):
        count+=1
        avg+=age
    else:
        break
avg = (avg/count)
print(f"{avg:.2f}")